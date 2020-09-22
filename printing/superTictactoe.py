def printBoard():
    output=[]
    lines=1
    while lines<=17:
        if lines%6==0:
            output.append("=========+========+=========")
        else:
            for i in range(0,27):
                if i%3==0 and i>=3:
                    if i%9==0 and i>=3:
                        output.append("H")
                    else:
                        if lines%2==0:
                            output.append("+")
                        else:
                            output.append("|")
                else:
                    if lines%2==0:
                        output.append("-")
                    else:
                        output.append(" ")
        output.append('\n')
        lines+=1
    print "".join(output)
        
printBoard()
        