n=int(input("Enter DOB (ddmmyyyy)"))
ar=[]
c=0
dob=n
s1,s2=0,0
while(n!=0):
    a=n%10
    ar.insert(0,a)
    n=n//10
    c+=1
if(c==8):
    for i in range(0,c):
        if(i%2==0):
            s1+=ar[i]
        else:
            s2+=ar[i]
    s=s1*3+s2
    if (s%10==0):
        print(dob,",Is a Lucky Number")
    else:
        print(dob,",Is not a Lucky Number")
else:
    print("Invalid Input")