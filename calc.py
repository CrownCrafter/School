while(1 == 1):
    a = int(input("Type the first number "))
    b = int(input("Type the second number "))
    print("\n")
    print("1)Add numbers")
    print("\n")
    print("2)Subtract num2 from num1")
    print("\n")
    print("3)Multiply num1 with num2")
    print("\n")
    print("4)Divide num1 with num2")
    print("\n")
    oper = int(input(""))
    if(oper == 1):
        print(a+b)
    elif(oper == 2):
        print(a-b)
    elif(oper == 3):
        print(a*b)
    elif(oper == 4):
        print(a/b)
    else:
        print("Wrong choice, exiting program")
        break        
        
