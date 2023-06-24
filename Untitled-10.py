n=int(input("Enter no."))
arr=[]
k=str(n)
for i in k:
        if(n%int(i)==0):
            arr.append(i)
l=len(arr)
if(l==0):
    print("No factors")
else:
    for i in range(l-1,-1,-1):
        print(arr[i],end=" ")

