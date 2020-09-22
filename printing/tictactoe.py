

def printBoard():
    output=[]
    lines=1
    while lines<=5:
        if lines%2==0:
            output.append("-----------")
        else:
            output.append("   |   |   ")
        lines +=1
    else:
        print "\n".join(output)
        
printBoard()