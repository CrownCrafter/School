def calcpow(num, power):
    result = 1
    for i in range(1, power + 1):
        result = result * num
    return result
base = int(input("Enter value for base "))
expo = int(input("Enter power "))
answer = calcpow(base, expo)
print(base , "raised to ", expo, "is", answer)
