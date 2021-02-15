#!/usr/bin/env python3
s = input("Enter string ")
v = 0
c = 0
u = 0
l = 0
for i in s:
    if(i in 'aeiouAEIOU'):
        v +=1
    else:
        c +=1
    if(i.isupper() == True):
        u += 1
    else:
        l += 1
print("Vowels " + str(v))
print("Consonants " + str(c))
print("Uppercase " + str(u))
print("Lowercase " + str(l))
