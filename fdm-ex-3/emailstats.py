import statistics
import os
from os import path
__dirName='C:/Users/evwhi/PythonCamp/fdm-ex-3/emails/'
__projNam='C:/Users/evwhi/PythonCamp/fdm-ex-3/'

def writeStats(total, wordCount, avgWordCount, standardDeviation, totalBytes):
    stats="\nTotal emails:\n"+str(total)+"\n"+"Total word count:\n"+str(wordCount)+"\n"+"Avgerage word count per email:\n"+str(avgWordCount)+"\n"+"Standard deviation of word count:\n"+str(standardDeviation)+"\n"+"Total bytes:\n"+str(totalBytes)
    statFile= open(os.path.join(__projNam, 'emails_info.txt'), 'w')
    statFile.write(stats)
    statFile.close()

def writeTable(unique_words):
    result=unique_words
    print(result)

def openAll():
    total=0
    wordCount=0
    avgWordCount=0
    standardDeviation=0.0
    totalBytes=0
    agg_wordCount_data=[]
    unique_wordCount_data=[]
    for file in os.listdir(__dirName):
        total+=1
        with open(os.path.join(__dirName, file), encoding="utf8") as f:
            wordCount=0
            unique_words=[]
            try:
                for line in f:
                    line_data=line.split(" ")
                    counter = wordCounter(line_data)
                    wordCount+=counter[0]
                    bCounter = byteCounter(line)
                    totalBytes+=bCounter
                    for word in counter[1]:
                        uniqueness = isUnique(unique_wordCount_data, word)
                        if isUnique:
                            unique_wordCount_data.append(word)
                        else:
                            continue
            except:
                error_file_name= f.name
                error_local=f.tell
                print("ERROR at file: "+error_file_name+"___at position: "+error_local)
            finally:
                agg_wordCount_data.append(wordCount)
    print("\nWriting stats to files...")
    standardDeviation=round(statistics.stdev(agg_wordCount_data), 2)
    wordCount=(sum(agg_wordCount_data, 0))
    avgWordCount=round(wordCount/total, 2)
    # writeStats(total, wordCount, avgWordCount, standardDeviation, totalBytes)
    unique_wordCount_data.sort()
    unique_wordCount_data=set(unique_wordCount_data)
    writeTable(unique_wordCount_data)

def byteCounter(line):
    count=0
    for b in line:
        count+=1
    return count

def wordCounter(line):
    count=0
    unique_words=[] #NOT SURE WHAT TO DO HERE, WILL REVISIT
    for word in line:
        sub = list(word)
        if sub[-1]=="\n":
            word = "".join(sub[-1:])
            continue
        else:
            count+=1
            unique= isUnique(unique_words, word)
            if unique:
                unique_words.append(word)
            else:
                continue
    return [count, unique_words]

def isUnique(array, word):
    if word in array:
        return 0
    else:
        return 1

openAll()

