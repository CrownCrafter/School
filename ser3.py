x = int(input("Enter x "))
n = int(input("Enter n "))
s = x
i = 1
sign = 1
for i in range(2, n+1):
    s += (sign* ((x**i)/i))
    sign *= -1
print(s)
