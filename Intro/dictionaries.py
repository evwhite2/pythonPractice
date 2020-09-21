studentsbyId= {
    100: 'Ellen',
    105: 'Cater', 
    110: 'Monica', 
    115: 'Evan',}

print(studentsbyId[100])

#del studentsbyId[110] #removes corresponding key-value pair

#print(studentsbyId.values())

if 110 in studentsbyId:
    print("Found: "+studentsbyId.get(110))
else:
    print("not found")

#constructor
expertise= dict([(100, 'Python'), (105, "JavaScript"), (110, "Java"), (115, "Python")])

print(expertise.values())
