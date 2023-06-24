x = float(input("Enter the value of x in radians: "))
n = int(input("Enter the number of terms to compute: "))

result = x
sign = -1
factorial = 1

for i in range(2, 2*n+1, 2):
    sign *= -1
    factorial *= i * (i-1)
    term = sign * x**i / factorial
    result += term

print("sin({}) = {}".format(x, result))
