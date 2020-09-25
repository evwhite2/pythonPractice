import os
from os import path
__dirName='C:/Users/evwhi/PythonCamp/fdm-ex-3/emails/'

def getStats(total, wordCount, avgWordCount, standardDeviation, totalBytes):
    stats="\nTotal emails: "+str(total)+"\n"+"Word count:  "+str(wordCount)+"\n"+"Avg word count:  "+str(avgWordCount)+"\n"+"Standard deviation  "+str(standardDeviation)+"\n"+"Bytes:   "+str(totalBytes)
    print(stats)

def openAll():
    total=0
    wordCount=0
    avgWordCount=0.0
    standardDeviation=0.0
    totalBytes=0
    files_data=[]
    for file in os.listdir(__dirName):
        total+=1
        with open(os.path.join(__dirName, file, ), encoding="utf8") as f:
            try:
                for line in f:
                    line_data=line.split(" ")
                    counter = wordCounter(line_data)
                    wordCount+=counter
            except:
                error_file_name= f.name
                print("ERROR at file: "+error_file_name)
            finally:
                continue
    print("\n.....getting stats")
    getStats(total, wordCount, avgWordCount, standardDeviation, totalBytes)

def wordCounter(line):
    count=0
    for word in line:
        if word=="\n":
            continue
        else:
            count+=1
    return count

openAll()

