numberSet1 = {0, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 20, 20, 20}
numberSet2 = {0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 20, 22}
numberSet3 = {0, 2, 4, 6, 8, 10}
numberSet4 = {100, 200, 300}

# print(1 in numberSet1) #returns true
# print(3 in numberSet2) #returns false

# print(numberSet1<= numberSet2) #return false
# print(numberSet3 <= numberSet2) #return true, numberSet3 is a subset of numberSet2 (all values in 3 are valus of 2)
# OR....
numberSet1.issubset(numberSet2) # returns false
numberSet3.issubset(numberSet2) # reutrns true

unionSet = numberSet1| numberSet2
unionSetAlso = numberSet1.union(numberSet2)

intersectionSet = numberSet1 & numberSet2
intersectionSetAlso = numberSet1.intersection(numberSet2)

# numberSet3 |= numberSet1 
# # SAME AS:
numberSet3.update(numberSet1)
print(numberSet3)

#symmetricDifferenceOfSets = numberSet3 ^ numberSet4
#SAME AS:
symmetricDifferenceOfSets = numberSet3.symmetric_difference(numberSet4)

a = { x for x in 'abracadabra' if x not in 'ab'}
print(a)