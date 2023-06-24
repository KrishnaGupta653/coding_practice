n=int(input("Enter no. of times earthquake occurred"))
c,d,e=0,0,0
if(n>0):
    for i in range(0,n):
        print("Enter the magnitude of",i+1,"earthquake in microns")
        a=float(input())
        if(a<=5.4):
            c+=1
        elif(5.4<a<=7.0):
            d+=1
        elif(a>7.0):
            e+=1
    print("Count of low mag. earthquake occured=", c)
    print("Count of med. mag. earthquake occured=",d)
    print("Count of high mag. earthquake occured=",e)
        
elif(n<0):
    print("Invalid Input")
else:
    print("No. earthqauke predicted")


