# Define a user-defined function to perform logical operations
def logical_operations(arg1, arg2):
    logical_and = arg1 and arg2
    logical_or = arg1 or arg2
    logical_not_arg1 = not arg1
    logical_not_arg2 = not arg2

    return logical_and, logical_or, logical_not_arg1, logical_not_arg2

# Take input from the user for two arguments
arg1 = 
bool(input("Enter the first argument (True/False): "))
arg2 = bool(input("Enter the second argument (True/False): "))

# Call the function to perform logical operations
result1, result2, result3, result4 = logical_operations(arg1, arg2)

# Print the results
print("Logical AND:", result1)
print("Logical OR:", result2)
print("Logical NOT of arg1:", result3)
print("Logical NOT of arg2:", result4)
