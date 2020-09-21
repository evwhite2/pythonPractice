def addAnyNumber(a, *b):
    sum =0
    for i in b:
        sum+=i
    print(a+sum)

# addAnyNumber(1, 2, 100, 200, 1)


def printStar(last, **num):
    print(num)

# printStar("White", first=0, second=100)


def total(*prices):
    price= 0
    for p in prices:
        price+=p
    tax = 0.10 * price
    total = price + tax
    return price, tax, total

print(total(100.50, 45.66))