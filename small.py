#!/usr/bin/env python3
lis = []
while(True):
    x = int(input("Enter number "))
    lis.append(x)
    i = input("Finished? ")
    if(i == 'y'):
        break
print(min(lis))
print(max(lis))
