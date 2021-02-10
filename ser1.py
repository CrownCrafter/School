#!/usr/bin/env python3

x = int(input("Enter x "))
n = int(input("Enter n "))
s = 1
i = 1
sign = 1
while i <= n:
    s += x ** i
    i += 1
print(s)
