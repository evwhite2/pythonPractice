import re
__dirName = 'C:/Users/evwhi/PythonCamp/fdm-ex-3/'


def findNegatives(stream_data, main_data):
    found_errors=""
    found_errors_array= []
    while len(stream_data) > 0:
        batch = stream_data[:10]
        for record in batch:
            for data in record:
                if data==str(-1):
                    found_errors=found_errors+"\n"+str(record)
                    found_errors_array.append(record)
                else: continue
        stream_data= stream_data[10:]
    addToCsv(found_errors, found_errors_array)

def findErrors(stream_data_file, main_data_file):
    # found_errors=dict()
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

def addToCsv(data_string, data_array):
    file = open(__dirName+'daily_errors.csv', 'a', encoding='utf8') 
    count=1
    for record in data_array:
        stringify = str(count)
        for data in record:
            stringify=stringify+","+data    
        stringify=stringify+'\n'
        file.write(stringify)
        count+=1
    

findErrors('daily_trades.csv', 'daily_trades_master.csv')

# field_string = "index"
#     for field in fields:
#         field_string=field_string+","+field
#     field_string=field_string+"\n"
#     csvFile = open(__dirName+csvFile_string, 'w+', encoding='utf-8') 
#     csvFile.write(field_string)
#     record_string=""
#     for key, value in records.items():
#         view = str(key)
#         for i in value:
#             view = view+","+i
#         record_string=record_string+view+"\n"
#         csvFile.writelines(view+"\n")
#     csvFile.close()