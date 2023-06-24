n=int(input("Enter no.of storage points"))
l=0
ml=0
for i in range(0,n):
    print("Enter oil from",i+1,"storage points in l")
    n1=int(input())
    print("Enter oil from",i+1,"storage points in ml")
    n2= int(input())
    l+=n1
    ml+=n2
s=l*1000+ml
l=s//1000
ml=s%1000
print("Total quantity both in L amd ml of oil is",l,"L",ml,"ml")