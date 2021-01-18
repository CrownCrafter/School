
x = int(input("Enter num"))
def factorial(num):
    fact = 1
    if(num > 0):
        for i in range(num, 0, -1):
            fact = fact * i
        print("Fact is " + str(fact))
    elif(x == 0):
        print("1")
    else:
        print("Negative number")
factorial(x)
