import re
__dirName = 'C:/Users/evwhi/PythonCamp/fdm-ex-3/'

def findJulianErrors(stream_data, main_data):
    deminishing_stream= stream_data
    while len(deminishing_stream)>990:
        batch = deminishing_stream[:10]    
        # for record in batch:
        #     record_id = int(record[0])
        #     julian_stream = float(record[3])
            # matching = main_data(filter(None, batch))
        deminishing_stream=deminishing_stream[10:]

def findMissing(stream_data, main_data):
    missing_ids=[]
    missing_records=[]
    for (idx, record) in enumerate(stream_data):
        end = idx+1
        if end>=len(stream_data):
            exit
        else:
            step = int(stream_data[idx+1][0])-int(record[0])
            if step > 1:
                missing_ids.append(int(record[0])+1)
    for (idx, record) in enumerate(main_data):
        try:
            for id in missing_ids:
                if record[0]== str(id):
                    missing_records.append(record)
        except:
            continue
    addToCsv(missing_records, "Missing from stream")
    findJulianErrors(stream_data, main_data)

def findNegatives(stream_data, main_data):
    found_errors_array= []
    deminishing_stream = stream_data
    while len(deminishing_stream) > 0:
        batch = deminishing_stream[:10]
        for record in batch:
            for data in record:
                if data==str(-1):
                    found_errors_array.append(record)
                else: continue
        deminishing_stream= deminishing_stream[10:]
    addToCsv(found_errors_array, "-1 Error")
    findMissing(stream_data, main_data)

def collectData(stream_data_file, main_data_file):
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
    field_names=""
    for field in main_data[0]:
        field_names= field_names+","+field 
    field_names=field_names+",error_note\n"
    file = open(__dirName+'daily_errors.csv', 'w', encoding='utf8')
    file.write(field_names)
    file.close()
    main_data= main_data[1:]
    stream_data= stream_data[1:]
    findNegatives(stream_data, main_data)

def streamLines(line):
    list_stream = line.split(",")
    last = list_stream[-1]
    last = re.sub(r"\n$", "", last, flags=re.I)
    list_stream[-1] = last
    return list_stream

def addToCsv(data_array, note):
    file = open(__dirName+'daily_errors.csv', 'a', encoding='utf8') 
    for record in data_array:
        stringify = ""
        for data in record:
            stringify=stringify+","+data    
        stringify=stringify+","+note+"\n"
        file.write(stringify)
    file.close()
    

collectData('daily_trades.csv', 'daily_trades_master.csv')