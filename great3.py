#!/usr/bin/env python3

a = int(input("Enter Number "))
b = int(input("Enter Number "))
c = int(input("Enter Number "))
if(a>=b and a>=c):
    print("Largest is " + str(a))

elif(b>=a and b>=c):
    print("Largest is " + str(b))


else:
    print("Largest is " + str(c))

if(a<=b and a<=c):
    print("Smallest is " + str(a))
elif(b<=a and b<=c):
    print("Smallest is " + str(b))
else:
    print("Smallest is " + str(c))
