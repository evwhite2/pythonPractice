__dirName = 'C:/Users/evwhi/PythonCamp/fdm-ex-3/'

found_errors= []

def findNegatives(stream_data, main_data):
    while len(stream_data) > 0:
        batch = stream_data[:10]
        # print("BATCH")
        stream_data= stream_data[10:]

def findErrors(stream_data_file, main_data_file):
    found_errors=dict()
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
    findNegatives(stream_data, main_data)

def streamLines(line):
    list_stream = line.split(",")
    return list_stream

def sumErrors(list):
    total = sum(list)
    if total > 0:
        return 1
    else:
        return 0


findErrors('daily_trades.csv', 'daily_trades_master.csv')