# Define a user-defined function with four arguments and default values
def my_function(arg1, arg2, arg3=0, arg4=1):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)
    print("arg4:", arg4)
    print("")


# Call the function with different arguments
my_function(1, 2)  # arg1 = 1, arg2 = 2, arg3 and arg4 use default values
my_function(3, 4, 5)  # arg1 = 3, arg2 = 4, arg3 = 5, arg4 uses default value
# arg1 = 6, arg2 = 7, arg3 uses default value, arg4 = 8
my_function(3, 4, 5, 1)
my_function(6, 7, arg4=8)
my_function(arg2=9, arg1=10, arg3=11, arg4=12)  # using keyword arguments
