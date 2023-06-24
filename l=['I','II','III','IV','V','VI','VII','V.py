l=['I','II','III','IV','V','VI','VII','VIII','IX','X']
n=int(input("Enter two digi no."))
a=n//10
b=n%10
if(b==0):
    x=(a*l[9])
    print(x)
else:
    x=((a)*l[9]+l[b-1])
    print(x)