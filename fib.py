#!/usr/bin/env python3
ter = int(input("Enter limit "))
f = 0
s = 1
x = f + s
print(f)
print(s)
while(x <= ter):
    print(x)
    f = s
    s = x
    x = f+s
