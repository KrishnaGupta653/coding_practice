l = eval(input("Enter elements in list"))
n = (input("enter the element to find in list"))
k = len(l)
c = 0
for i in range(0, k):
    if(n == str(l[i])):
        print(i)
        c += 1
print(c)
