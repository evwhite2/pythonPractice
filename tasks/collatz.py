def collatz(x):
    sequence=[x]
    for i in sequence:
        if i==1:
            print("\nSequence completed after "+str(len(sequence))+" iterations: \n")
        else:
            if i%2==0:
                y=i/2
                sequence.append(int(y))
            else:
                y=3*i+1
                sequence.append(int(y))
    print(sequence)

collatz(1000000)