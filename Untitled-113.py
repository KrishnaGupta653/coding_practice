number = input("Enter a number: ")

if "." in number:
    print("Input is a float")
elif int(number) < 0:
    print("Input is a negative integer")
else:
    if int(number) % 2 == 0:
        print("Input is an even integer")
    else:
        print("Input is an odd integer")
