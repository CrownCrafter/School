#!/usr/bin/env python3
lis = ["blue", "1", "bangalore", "Hello world"]
while(True):
    print("1)Add Element at Position")
    print("2)Append Element")
    print("3)Modify Element")
    print("4)Delete Element by Position")
    print("5)Delete Element by Value")
    print("6)Sort in Ascending")
    print("7)Sort in Descending")
    print("8)Add a list")
    print("9)Exit")
    print(f"The list has the following elements: {lis}")
    oper = int(input("Enter Operation "))
    if(oper == 1):
        lis.insert(int(input("Enter Position ")), input("Enter Element "))
        print(lis)

    if(oper == 2):
        lis.append(input("Enter Element "))
        print(lis)

    if(oper == 3):
        pos = int(input("Enter position "))
        ele = input("Enter element")
        lis[pos] = ele
        print(lis)


    if(oper == 4):
        lis.pop(int(input("Enter Position ")))
        print(lis)

    if(oper == 5):
        ele = input("Enter Element ")
        if ele in lis:
            lis.remove(ele)
        print(lis)

    if(oper == 6):
        lis.sort()
        print(lis)

    if(oper == 7):
        lis.sort(reverse = True)
        print(lis)
        
    if(oper == 8):
        newList = input("Enter the list to be appended(Do not use quotes, and use (,) for separating the elements): ")
        lis.extend(list(newList.split(",")))
        print("The list has been appended\n")

    if(oper == 9):
        break
