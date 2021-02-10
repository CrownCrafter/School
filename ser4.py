#!/usr/bin/env python3

import math
x = int(input("Enter x "))
n = int(input("Enter n "))
s = x
i = 2
sign = 1
while i <= n:
    f = math.factorial(i)
    if(sign == 1):
        s += (x**i)/f
        sign = 0
    else:
        s -= (x**i)/f
        sign = 1
    i += 1
print(s)
