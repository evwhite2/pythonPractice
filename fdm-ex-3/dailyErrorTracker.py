import re
__dirName = 'C:/Users/evwhi/PythonCamp/fdm-ex-3/'

static_count=1

def findMissing(stream_data, main_data):
    stream_data_stripped= stripId(stream_data)
    main_data_stripped = stripId(main_data)
    while len(stream_data_stripped)>0:
        batch = stream_data_stripped[:10]
        print(batch) # BROKEN, WORKING ON THIS
        for (idx, data) in batch:
            if data != main_data_stripped[idx]:
                    print("ERROR: \n STREAM: "+str(data)+"\n MAIN"+ main_data_stripped[idx]+'\n')
                    print("NEXT LINE IN STREAM: \n"+stream_data_stripped[idx+1])
                    print("NEXT LINE IN MAIN: \n"+main_data_stripped[idx+1])
            else: continue
        stream_data_stripped= stream_data_stripped[10:]

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