#factors
def factors():
    a = int(input("Type num"))
    factors = [1]
    i = 2
    while(i <= a):
        if(a%i == 0):
            factors.append(i)

        i += 1
    print(factors)
factors()
