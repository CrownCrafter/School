x = int(input("Enter num"))
fact = 1
if(x > 0):
    for i in range(1, x + 1):
        fact = fact * i
    print("Fact is " + str(fact))

elif(x == 0):
    print("1")


else:
    print("Negative number")
