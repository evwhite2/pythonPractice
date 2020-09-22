def sumMultiplesOf3and5(x):
    sum=0
    for i in range(1, x):
        if i%3==0 or i%5==0:
            sum+=i
    print(sum)

sumMultiplesOf3and5(10000)