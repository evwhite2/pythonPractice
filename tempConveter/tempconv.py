import tempfunc as conv

temp = input("\nInput temp to be converted:   ")
toVal = input("\nWould you like to convert to Farenheit or Celcius (Enter 'F' or 'C'):   ")
toVal=toVal.strip().upper()

answer=""

if toVal=="F":
    answer=conv.celtofah(temp)[1]
elif toVal=="C":
    answer=conv.fahtocel(temp)[1]
else:
    print("invalid character")

print(answer)