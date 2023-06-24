dis=int(input("Enter the distance travelled by vehicle (km) "))
if(dis<=1000):
    print("Total charge to be paid for",dis,"km =",0)
elif(1000<dis<=10000):
    print("Total charge to be paid for",dis,"km =",50)
elif(10000<dis<=20000):
    print("Total charge to be paid for",dis,"km =",150)
elif(20000<dis<=40000):
    print("Total charge to be paid for",dis,"km =",250)
elif(40000<dis<=60000):
    print("Total charge to be paid for",dis,"km =",350)
else:
    print("Total charge to be paid for",dis,"km =",500)