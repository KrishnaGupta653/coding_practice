n=eval(input("enter"))
if isinstance(n, float) or n<0:
    print("invalid input")
else:
    if n!=2:
       print("odd")
    else:
       print("even")