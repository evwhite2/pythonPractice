__dirName='C:/Users/evwhi/PythonCamp/fdm-ex-3/'

def sqlToCsv(sqlFile_string, csvFile_string):
    sqlFile = open(__dirName+sqlFile_string)
    fields= list()
    records = dict()
    increment_record=0
    for line in sqlFile:
        f1_left = line.index("(")+1
        f1_right = line.index(")")
        fields = line[f1_left:f1_right]
        fields = fields.split(",")
        line = line[f1_right+1:]
        f2_left = line.index("(")+1
        f2_right = line.index(")")
        record_values = line[f2_left:f2_right]
        record_values = record_values.split(",")
        records[increment_record]= record_values
        increment_record+=1
    sqlFile.close()
    field_string = "index"
    for field in fields:
        field_string=field_string+","+field
    field_string=field_string+"\n"
    csvFile = open(__dirName+csvFile_string, 'w+', encoding='utf-8') 
    csvFile.write(field_string)
    record_string=""
    for key, value in records.items():
        view = str(key)
        for i in value:
            view = view+","+i
        record_string=record_string+view+"\n"
        csvFile.writelines(view+"\n")
    csvFile.close()
    

sqlToCsv('stock_price_SQL_Inserts.txt', 'stock_price.csv')