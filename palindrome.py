#!/usr/bin/env python3

a = input("Enter string")
i = 0
j = len(a) - 1
while(True):

    if(a[i] == a[j]):
        i += 1
        j -= 1
        continue
        if(len(a) == (i+1)):
            print("It is a palindrome")
            break
    else:
        print("Not a palindrome")
        break
