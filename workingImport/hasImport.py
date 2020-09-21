import csv 
from csv import reader

# transforming/reading data fro csv
# CONFIGURATIONS FOR PYTHON 3 MUST BE SHUT OFF TO RUN THIS CODE
opened_file= open('workingImport/AppleStore.csv')
read_file = reader(opened_file)
apps_data=list(read_file)

# slicing

print(apps_data[:5]) # prints first 5 rowa
print(len(apps_data)) # prints length = 7198
print(apps_data[1:3]) 

# loops

rating_sum=0
total=0
for i in apps_data[1:]:
    rating=float(i[7])
    total+=1
    rating_sum+=rating
    
avg_rating=rating_sum/int(total)

print(total)
print(rating_sum)
print(avg_rating)

all_ratings = list()

for i in apps_data[1:]:
    rating=float(i[7])
    all_ratings.append(rating)

avg_rating= sum(all_ratings) / len(all_ratings)
print(avg_rating)