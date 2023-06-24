# Define a user-defined function to reverse an integer
def reverse(number):
    reverse = 0

    while number > 0:
        remainder = number % 10
        reverse = (reverse * 10) + remainder
        number = number // 10

    return reverse


# Take input from the user for an integer
num = int(input("Enter an integer: "))

# Call the user-defined function to reverse the integer
reversed_num = reverse(num)

# Print the reversed integer
print("Reversed integer:", reversed_num)
