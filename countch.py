#!/usr/bin/env python3
def charCount(ch, st):
    count = 0
    for character in st:
        if character == ch:
            count += 1
    return count
st = input("Enter a string ")
ch = input("Find character to be searched ")
print(charCount(ch, st))
