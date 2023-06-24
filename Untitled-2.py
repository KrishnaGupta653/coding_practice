nh=int(input("Enter no. of classes held"))
na=int(input("Enter no. of classes attended"))
m =int(input("student medical proof availability(1(YES)/0(NO))"))
p=na/nh*100
print("percentage of classes attended=",p)
if(p<75):
    if(m==1):
        print("Student is allowed for exam")
    else:
        print("Student is not allowed for exam")
else:
    print("Student is allowed for exam")
