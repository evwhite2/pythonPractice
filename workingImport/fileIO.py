import csv

#PYTHON 3 VERSION
with open('workingImport/AppleStore_short.csv') as f:
    read_file = csv.reader(f, delimiter=',')
    for row in read_file:
        print(row[0],row[1],row[2],)
    f.close()

