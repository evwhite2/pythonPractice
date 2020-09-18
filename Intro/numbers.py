import random as rd



randomFloat = rd.random() # between 0 & 1
print(randomFloat)

floatBetweenTwo = rd.uniform(2, 6)
print(floatBetweenTwo)

newList= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100, 200, 300, 400, 500, 1000, 2000, 3000]
rd.shuffle(newList)
print(newList)
print(rd.choice(newList)) #chooses from list at random

randomlyInRange= rd.randrange(1000, 10000, 1010) #(beg, end, [step?])
print(randomlyInRange)

makeString = str(randomFloat)
print("Look I can concatinate this now..."+makeString)
print(type(makeString))