def fahtocel(temp):
    x = float(temp)
    converted=round((x-32)*(5/9), 2)
    printed = "\nTemperature in Celcius: "+str(converted)
    return [converted, printed]

def celtofah(temp):
    x = float(temp)
    converted=round((x*(9/5))+32, 2)
    printed = "\nTemperature in Farenheit: "+str(converted)
    return [converted, printed]
