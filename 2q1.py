n = int(input("Enter no. of terms"))
l = []
b = 2
i = 2
while True:
    c = 0
    for j in range(2, i):
        if(i % j == 0):
            c = c+1
    if c == 0:
        l.append(i)
    i = i+1
    if n == len(l):
        break
print(l, len(l))
