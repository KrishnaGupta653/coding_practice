from random import *
l = {0: "sanke", 1: "water", -1: "gun"}
c = randint(-1, 1)
print(l[c])
n = int(input('0:"sanke",1:"water",-1:"gun"'))


def check(c, n):
    if (c == n):
        return 0
    elif (c == 0 and n == 1):
        return -1
    elif (c == 1 and n == -1):
        return -1
    elif (c == -1 and n == 0):
        return -1
    else:
        return 1


a = check(c, n)
print(c, n)
if (a == 0):
    print("draw")
elif(a == 1):
    print("won")
elif(a == -1):
    print("lose")
