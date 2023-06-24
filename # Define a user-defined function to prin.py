# Define a user-defined function to print the multiplication table
def multiplication_table(num, n):
    print("Multiplication table for", num, ":")
    if n <= 0:
        print("invalid input")
    else:
        for i in range(1, n+1):
            result = num * i
            print(num, "x", i, "=", result)


# Take input from the user for an integer
number = int(input("Enter an integer: "))
k = int(input("Enter limit: "))

# Call the user-defined function to print the multiplication table
multiplication_table(number, k)
