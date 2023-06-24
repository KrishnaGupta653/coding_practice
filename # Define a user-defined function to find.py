# Define a user-defined function to find the largest number among three numbers
def largest():
    # Take input from the user for three numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3 = float(input("Enter the third number: "))

    # Compare the numbers to find the largest one
    largest = num1
    if num2 > largest:
        largest = num2
    if num3 > largest:
        largest = num3

    # Print the largest number
    print("The largest number is:", largest)

# Call the user-defined function to find the largest number
largest()
