

n=int(input("Enter DOB (ddmmyyyy)"))
ar=[]
so,se=0,0
k=str(n)
for i in k:
    ar.append(int(i))
print(n)
print(ar)
if(len(k)==8):
    for i in range(0,len(k)):
        if(i%2==0):
            so+=ar[i]
        else:
            se+=ar[i]
    s=so*3+se
    if (s%10==0):
        print(n,",Is a Lucky Number")
    else:
        print(n,",Is not a Lucky Number")
else:
    print("Invalid Input")