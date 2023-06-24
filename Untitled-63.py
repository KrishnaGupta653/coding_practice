def biggest_number():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3 = float(input("Enter the third number: "))

    biggest = max(num1, num2, num3)
    print("The biggest number is:", biggest)

# Calling the function to find the biggest number
biggest_number()
