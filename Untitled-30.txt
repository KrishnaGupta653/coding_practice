r1=int(input("Enter no. of rows in matrix 1"))
c1=int(input("Enter no. of columns in matrix 1"))
r2=int(input("Enter no. of rows in matrix 2"))
c2=int(input("Enter no. of columns in matrix 2"))
l1,l2=[],[]
for i in range(r1):          
    a =[]
    for j in range(c1):      
         a.append(int(input()))
    l1.append(a)
for i in range(r2):          
    a =[]
    for j in range(c2):      
         a.append(int(input()))
    l2.append(a)
mul = [[0 for _ in range(c2)] for _ in range(r1)]
print(l1,l2,mul)
if(c1!=r2):
    print("Invalid")
else:
    for i in range(0,r1):
        for j in range(0,c2):
            for k in range(0,c1):
                mul[i][j]+=l1[i][k]*l2[k][j]
for i in range(r1):
    for j in range(c2):
        print(mul[i][j], end = " ")
    print()
