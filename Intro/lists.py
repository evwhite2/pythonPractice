
languages= ["Cantonese", "English", "Swahili", "French", "Spanish", "Dutch", "Thai", "Russian", "Arabic", "Xhosa", "Mandarin", "German"]

print(languages[::2]) # print first in list, then every second element

numbers= list()
for i in range(10):
    numbers.append(i/2)
    numbers.append(i*3)

languages.sort() #sorts alphanumerically
numbers.sort()

languages.pop() #removes last
numbers.remove(3) #removes first instance of the element in ()
print(numbers.index(1.0))
languages.insert(1, "Farsi") #inserts element into index 1, shifts all other elements 1 index





