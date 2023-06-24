import math
nl=int(input("Enter length of ladder in feet= "))
na=int(input("Enter angle in degrees= "))
na=(3.14)/180*na
h=nl*math.sin(na)
print("Enter height of tower= %0.2f" %h)