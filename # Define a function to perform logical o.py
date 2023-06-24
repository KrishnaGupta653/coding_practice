# Define a function to perform logical operations on two arguments
def logical(arg1, arg2):
    _and = arg1 and arg2
    _or = arg1 or arg2
    _not1 = not arg1
    _not2 = not arg2
    _xor = arg1 ^ arg2
    
    return _and, _or, _not1, _not2, _xor

# Prompt the user to input values for the two arguments
operand1 = bool(int(input("Enter the first operand(1/0): ")))
operand2 = bool(int(input("Enter the second operand(1/0): ")))

# Call the function and store the results in variables
result1, result2, result3, result4, result5 = logical(operand1, operand2)

# Print the results
print("AND:", result1)
print("OR:", result2)
print("NOT operand1:", result3)
print("NOT operand2:", result4)
print("XOR:", result5)
