import re
__dirName = 'C:/Users/evwhi/PythonCamp/fdm-ex-3/'

static_count=1

def findMissing(stream_data, main_data):
    stream_data_stripped= stripId(stream_data)
    main_data_stripped = stripId(main_data)
    main_idx=0
    while len(stream_data_stripped)>500:
        batch = stream_data_stripped[:1][0]
        main_batch = main_data_stripped[main_idx]
        if str(batch) == str(main_batch):
            exit
        else:
            print("ERROR at "+str(main_idx))
            flagged_idx=[]
            for idx, data in enumerate(batch):
                if data==main_batch[idx]:
                    flagged_idx.append(0)
                else:
                    flagged_idx.append(1)
            if sum(flagged_idx)>1:
                print('SUM: '+ str(sum(flagged_idx)))
                print("STREAM SHOWS: \n"+str(batch))
                print("MAIN SHOWS: \n"+ str(main_batch))
                print("MAIN OPTIONS: \n"+str(main_data_stripped[main_idx+1])+"\n"+str(main_data_stripped[main_idx+2])+"\n\n")
            else:
                exit
        if main_idx==len(main_data_stripped)-1:
            print("STOPPED MAIN")
            exit
        else:
            main_idx+=1
        stream_data_stripped= stream_data_stripped[1:]

def findNegatives(stream_data, main_data):
    found_errors_array= []
    stream_data_in=stream_data
    while len(stream_data_in) > 0:
        batch = stream_data_in[:10]
        for record in batch:
            for data in record:
                if data==str(-1):
                    found_errors_array.append(record)
                else: continue
        stream_data_in= stream_data_in[10:]
    addToCsv(found_errors_array)
    findMissing(stream_data, main_data)

def findErrors(stream_data_file, main_data_file):
    stream_data= []
    main_data= []
    stream_data_file = open(__dirName+stream_data_file, 'r', encoding='utf8')
    main_data_file = open(__dirName+main_data_file, 'r', encoding='utf8')
    for line in stream_data_file:
        line = streamLines(line)
        stream_data.append(line)
    for line in main_data_file:
        line = streamLines(line)
        main_data.append(line)
    stream_data_file.close()
    main_data_file.close()
    field_names="index"
    for field in main_data[0]:
        field_names= field_names+","+field 
    field_names=field_names+"\n"
    file = open(__dirName+'daily_errors.csv', 'w', encoding='utf8')
    file.write(field_names)
    file.close()
    findNegatives(stream_data, main_data)

def streamLines(line):
    list_stream = line.split(",")
    last = list_stream[-1]
    last = re.sub(r"\n$", "", last, flags=re.I)
    list_stream[-1] = last
    return list_stream

def sumErrors(list):
    total = sum(list)
    if total > 0:
        return 1
    else:
        return 0

def stripId(array):
    array= array[1:]
    return array

def addToCsv(data_array):
    file = open(__dirName+'daily_errors.csv', 'a', encoding='utf8') 
    count=static_count
    for record in data_array:
        stringify = str(count)
        for data in record:
            stringify=stringify+","+data    
        stringify=stringify+'\n'
        file.write(stringify)
        count+=1
    file.close()
    

findErrors('daily_trades.csv', 'daily_trades_master.csv')