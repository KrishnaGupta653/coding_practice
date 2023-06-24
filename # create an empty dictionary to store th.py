# create an empty dictionary to store the Fibonacci terms
f= {}

# initialize the first two terms of the sequence
f[1] = 0
f[2] = 1

# generate the remaining terms and store them in the dictionary
for i in range(3, 21):
    a = f[i-1]
    b = f[i-2]
    c = a + b
    f[i] = c

# print the resulting dictionary
print(f)
