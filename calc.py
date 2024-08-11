def Calculator(a,b,vibor):
    if vibor == "+":
        return str(a+b)
    elif vibor == "-":
        return str(a-b)
    elif vibor == "/":
        if b == 0:
            return "dont"
        else:
            return str(a/b)
        
    elif vibor == "*":
        return str(a*b)
    else:
        return "!"
    
while True:
    primer = (input("Pishi primer cherez probel esli stop off: "))
    primeru = primer.split(" ")
    if primeru[0] == "off":
        break
    #try:
    a=int(primeru[0])
    b=int(primeru[2])
    right_answer = Calculator(a,b,primeru[1]) 
    answer = input("Poprobui otwetit sam")
    print("Right Answer: ",right_answer)
    if answer == right_answer:
        print("Krasavchik")
    else:
        print("Ychi matematicu")
    #except:
        #print("Pishi normalno")
    