def calculating(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        return a / b
def operating():     
    a = int(input("give a first number \n"))
    shouldEnd = True
    while shouldEnd:
            
        operation = input("What do you want? + or - or * or /")
        b = int(input("give a second number\n"))
        z = calculating(a, b, operation)
        print(z)
        restart = input("Want to restart? If you want type Y, if not type N.")

        if restart == "n":
            
            print(f"Ans = {z}`")
            a = z 
            shouldEnd = True
        elif restart == "y":
            shouldEnd = False
            
            operating()
        
            
            
operating()