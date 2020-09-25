import os
from os import path
__dirName='C:/Users/evwhi/PythonCamp/fdm-ex-3/emails/'

def openAll():
    total=0
    wordCount=0
    avgWordCount=0.0
    standardDeviation=0.0
    totalBytes=0
    files_data=[]
    for file in os.listdir(__dirName):
        if file.endswith('.txt'):   
            total+=1
            file_content= []
            with open(os.path.join(__dirName, file)) as f:
                for line in f:
                    # print(line)
                    file_content.append({line})
            files_data.append(file_content)
            f.close()
        else:
            continue
    print(files_data)
    # getStats(total, wordCount, avgWordCount, standardDeviation, totalBytes)

def getStats(total, wordCount, avgWordCount, standardDeviation, totalBytes):
    # stats = dict({
    # "Total emails": total,
    # "Word count": wordCount,
    # "Avg word count": avgWordCount,
    # "Standard deviation":standardDeviation,
    # "Bytes": totalBytes
    # })
    stats="\nTotal emails: "+str(total)+"\n"+"Word count:  "+str(wordCount)+"\n"+"Avg word count:  "+str(avgWordCount)+"\n"+"Standard deviation  "+str(standardDeviation)+"\n"+"Bytes:   "+str(totalBytes)
    print(stats)

openAll()

