n=int(input("enter"))
c=0
for i in range(2,n):
        if n%i==0:
            c=c+1
if c==0:
    print("prime")
else:
    print("composite")