# Prompt the user to enter a list of numbers
numbers = eval(input("Enter a list of numbers (separated by spaces): "))

# Convert the list of strings to a list of integers

# Make a new tuple that has only positive values from the list
pn = ()
for num in numbers:
    if num > 0:
        pn+= (num,)

# Print the original list of numbers and the new tuple of positive numbers
print("Original list of numbers: ", numbers)
print("Tuple of positive numbers: ", pn)
