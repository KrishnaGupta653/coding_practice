print("Programming Courses : 1, Robotics : 2, Academic Writing : 3")
n=int(input("Enter product code (1/2/3)"))
fee=int(input("Enter amount of fees to be paid"))
if(n==1):
    if(fee>1000):
        fee-=(10/100)*fee
        print("Fee to be paid=",fee)
    else:
        print("Fee to be paid=",fee)
elif(n==2):
    if(fee>750):
        fee-=(5/100)*fee
        print("Fee to be paid=",fee)
    else:
        print("Fee to be paid=",fee)
elif(n==3):
    if(fee>500):
        fee-=(10/100)*fee
        print("Fee to be paid=",fee)
    else:
        print("Fee to be paid=",fee)
else:
    print("Invalid input")
