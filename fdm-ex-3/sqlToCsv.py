__dirName='C:/Users/evwhi/PythonCamp/fdm-ex-3/'

def sqlToCsv(sqlFile_string, csvFile_string):
    sqlFile = open(__dirName+sqlFile_string)
    csvFile = open(__dirName+csvFile_string, 'a')
    fields= list()
    records = dict()
    for line in sqlFile:
        f1_left = line.index("(")+1
        f1_right = line.index(")")
        field_names = line[f1_left:f1_right]
        field_names = field_names.split(",")
        fields = field_names
        line = line[f1_right+1:]
        f2_left = line.index("(")+1
        f2_right = line.index(")")
        record_values = line[f2_left:f2_right]
        record_values = record_values.split(",")
        #UNFINISHED
        csvFile.writelines(record_values)
    csvFile.close()
    sqlFile.close()
        

        


sqlToCsv('stock_price_SQL_Inserts.txt', 'stock_price.csv')