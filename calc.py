def Calculator(a,b,vibor):
    if znac == 1:
        return str(a+b)
    elif znac == 2:
        return str(a-b)
    elif znac == 3:
        if b == 0:
            return "dont"
        else:
            return str(a/b)
        
    elif znac == 4:
        return str(a*b)
    else:
        return "!"
    
a = b = znac = 0
while True:
    znac=int(input("+=1, -=2, /=3, *=4, exit=5"))
    if znac == 5:
        break
    a=int(input("first number"))
    a=int(input("second number"))
    print("Answer:"Calculator(a,b,znac))

    
        
    

    