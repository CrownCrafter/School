#!/usr/bin/env python3

p = float(input("Enter Principal "))
r = float(input("Enter Interest Rate "))
t = float(input("Enter Time "))
print("Simple Interest " + str((p*r*t)/100))
print("Compound Interest " + str(p*(1 + (r/100))**t))
