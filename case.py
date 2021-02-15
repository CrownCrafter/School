#!/usr/bin/env python3
x = input("Enter String ")
st = ''
for i in x:
    if(i.islower()):
        i = i.upper()
    else:
        i = i.lower()
    st += i
print(st)
