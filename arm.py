#!/usr/bin/env python3
x = int(input("Enter number "))
i = 1
while(True):
    if(x // (10 ** i) == 0):
        dig = i
        break
    i += 1
lis = []
for i in str(x):
    lis.append(int(i))
i = 0
arm = 0
while(i < len(lis)):
    arm += lis[i] ** dig
    i += 1
if(arm == x):
    print("It is Armstrong number")
else:
    print("It is not Armstrong number")
