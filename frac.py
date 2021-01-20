def frac(num, de = 1):
    remainder = num % de
    if(remainder != 0):
        quotient = int(num/de)
        print("Mixed fraction=", quotient, "(", remainder, "/", deno, ")")
    else:
        print("Evaluates to whole number")
num = int(input("Enter numerator "))
deno = int(input("Enter denominator "))
print("Entered ", num, "/", deno)
if(num>deno):
    frac(num, deno)
else:
    print("Proper fraction")
