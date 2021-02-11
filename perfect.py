#!/usr/bin/env python3
x = int(input("Enter number "))
p = x
i = 1
sum = 0
while(True):
    if(x // (10 ** i) == 0):
        dig = i
        break

    i += 1
i = 1
factors=[]
while(i < x):
    if(x % i == 0):
        factors.append(i)
    i += 1
for i in range(0, len(factors)):
    sum += factors[i]
if(sum == x):
    print("It is perfect number")
else:
    print("It is not a perfect number")
