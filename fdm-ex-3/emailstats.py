import statistics
import os
from os import path
__dirName='C:/Users/evwhi/PythonCamp/fdm-ex-3/emails/'

def getStats(total, wordCount, avgWordCount, standardDeviation, totalBytes):
    stats="\nTotal emails: "+str(total)+"\n"+"Word count:  "+str(wordCount)+"\n"+"Avg word count:  "+str(avgWordCount)+"\n"+"Standard deviation  "+str(standardDeviation)+"\n"+"Bytes:   "+str(totalBytes)
    print(stats)

def openAll():
    total=0
    wordCount=0
    avgWordCount=0
    standardDeviation=0.0
    totalBytes=0
    files_data=[]
    for file in os.listdir(__dirName):
        total+=1
        with open(os.path.join(__dirName, file), encoding="utf8") as f:
            wordCount=0
            try:
                for line in f:
                    line_data=line.split(" ")
                    counter = wordCounter(line_data)
                    wordCount+=counter
                    bCounter = byteCounter(line)
                    totalBytes+=bCounter
            except:
                error_file_name= f.name
                error_local=f.tell
                print("ERROR at file: "+error_file_name+"___at position: "+error_local)
            finally:
                files_data.append(wordCount)
    print("\n.....getting stats")
    standardDeviation=round(statistics.stdev(files_data), 2)
    wordCount=(sum(files_data, 0))
    avgWordCount=round(wordCount/total, 2)
    getStats(total, wordCount, avgWordCount, standardDeviation, totalBytes)

def byteCounter(line):
    count=0
    for b in line:
        count+=1
    return count

def wordCounter(line):
    count=0
    for word in line:
        if word=="\n":
            continue
        else:
            count+=1
    return count

openAll()

