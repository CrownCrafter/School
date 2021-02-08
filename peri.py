#!/usr/bin/env python3

sha = input("Enter type of shape ")
if(sha == "square"):
    l = float(input("Enter side "))
    print("Perimeter is "+ str(4 * l) + "Area is " + str(l**2))

elif(sha == "rectangle"):
    l = float(input("Enter Length "))
    b = float(input("Enter Breadth "))
    print("Perimeter is "+ str(2*(l+b)) + "Area is " + str(l*b))


elif(sha == "circle"):
    r = float(input("Enter Radius "))
    print("Perimeter is "+ str(2*3.14*r) + "Area is " + str(3.14*r*r))


elif(sha == "triangle"):
    h = float(input("Enter Height "))
    l = float(input("Enter Base "))
    m = float(input("Enter Second Side "))
    n = float(input("Enter Third Side "))
    print("Perimeter is "+ str(l+m+n) + "Area is " + str(0.5*h*l))
