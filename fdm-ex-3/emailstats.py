import statistics
import re
import os
import operator
from os import path
__dirName='C:/Users/evwhi/PythonCamp/fdm-ex-3/emails/'
__projNam='C:/Users/evwhi/PythonCamp/fdm-ex-3/'


def writeStats(total, wordCount, avgWordCount, standardDeviation, totalBytes):
    stats="\nTotal emails:\n"+str(total)+"\n"+"Total word count:\n"+str(wordCount)+"\n"+"Avgerage word count per email:\n"+str(avgWordCount)+"\n"+"Standard deviation of word count:\n"+str(standardDeviation)+"\n"+"Total bytes:\n"+str(totalBytes)
    statFile= open(os.path.join(__projNam, 'emails_info.txt'), 'w')
    statFile.write(stats)
    statFile.close()

def writeTable(unique_words, all_words):
    unique_words.sort()
    all_words.sort()
    instances = dict()
    lengths = dict()
    __sort=0
    for w in all_words:
        if w in instances:
            instances[w]= instances[w]+1
        else:
            instances[w]=1
    for w in all_words:
        w_sub= list(w)
        word_length = len(w_sub)
        if word_length in lengths:
            lengths[word_length]=lengths[word_length]+1
        elif word_length==0:
            continue
        else:
            lengths[word_length]=word_length
    uniqueFile = open(os.path.join(__projNam, 'emails_tables.txt'), 'w')
    uniqueFile.write("\n\nTable 1: Unique Word Count\nTOTAL: "+str(len(unique_words))+"\n\n")
    for key, value in instances.items():
        uniqueFile.write('%s:%s\n' % (key, value))
    uniqueFile.write("\n\nTable 2: Word Length Count\n\n")
    for key, value in lengths.items():
        uniqueFile.write('%s:%s\n' % (key, value))
    uniqueFile.close()

def openAll():
    total=0
    wordCount=0
    avgWordCount=0
    standardDeviation=0.0
    totalBytes=0
    agg_wordCount_data=[]
    unique_wordCount_data=[]
    all_words_data=[]
    for file in os.listdir(__dirName):
        total+=1
        with open(os.path.join(__dirName, file), encoding="utf8") as f:
            wordCount=0
            all_words=[]
            try:
                for line in f:
                    line_data=line.split(" ")
                    line_data = prepLine(line_data) #scrubbing line data with regEx
                    counter = wordCounter(line_data) 
                    wordCount+=counter
                    bCounter = byteCounter(line)
                    totalBytes+=bCounter
                    for w in line_data:
                        all_words.append(w)
            except:
                error_file_name= f.name
                error_local=f.tell
                print("ERROR at file: "+error_file_name+"___at position: "+error_local)
            finally:
                agg_wordCount_data.append(wordCount)
                for word in all_words:
                    all_words_data.append(word)
                    uniqueness = isUnique(unique_wordCount_data, word)
                    if uniqueness:
                        unique_wordCount_data.append(word)
                    else:
                        continue
    print("\nWriting stats to files...")
    standardDeviation=round(statistics.stdev(agg_wordCount_data), 2)
    wordCount=(sum(agg_wordCount_data, 0))
    avgWordCount=round(wordCount/total, 2)
    writeStats(total, wordCount, avgWordCount, standardDeviation, totalBytes)
    writeTable(unique_wordCount_data, all_words_data)

def byteCounter(line):
    count=0
    for b in line:
        count+=1
    return count

def prepLine(line):
    scrubbedLine= []
    for word in line:
        word = word.lower()
        word = re.sub(r'\W', '', word, flags=re.I)
        scrubbedLine.append(word)
    return scrubbedLine

def wordCounter(line):
    count=0
    for word in line:
        count+=1
    return count

def isUnique(array, word):
    if word in array:
        return 0
    else:
        return 1

openAll()

