x = int(input("Enter num "))
i = 2
while True:
    div = x%i

    if(i == x):
        print("Prime")
        break
    if(div == 0):
        print("Composite")
        break
    i += 1
print("Execution complete")
