string1="RANDALL SKEFFINGTON"
string2="Is my Favorite Zombie"
string1 = string1.lower()
string2 = string2.upper()
print(string1)
print(string2)

# '\n' = new line & '\t' = tab
print("Streams:\n\tJava\n\tITSM\n\tData Analysis") 

name="Ellen Victoria White" 
print("-----------")
print(name[0:5]+" "+name[6]+".")

print(string1.title()) #case conversion

string2.strip() # =>same is string.trim() in JS

eatables={
    'foods':[
    {'name': 'apple', 'color': 'red'},
    {'name':'broccoli', 'color':'green'}
    ],
    'drinks':[
        {'name':'coffee', 'color': 'black'},
        {'name':'tea', 'color': 'brown'}
    ]}
eatables = str(eatables)
# print(eatables)

print(string1.replace('f', 'p'))
print(string1.split(" "))

hasNumber= "Thi5 5tring contain5 number5" 
noNumber= "This string has no numbers"
isNumber= "1234"
print(hasNumber.isdigit()) #returns false, beacuse it is also alpha
print(noNumber.isdigit()) #returns false
print(isNumber.isdigit()) #returns true

