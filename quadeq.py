def func(a, b, c):
    deter = b**2 - 4*a*c
    if(deter > 0):
        print("Distinct real roots")
    elif(deter == 0):
        print("One real root")
    else:
        print("Complex root")
a = int(input("First Coef"))

b = int(input("Second Coef"))

c = int(input("Third Coef"))
func(a, b, c)
