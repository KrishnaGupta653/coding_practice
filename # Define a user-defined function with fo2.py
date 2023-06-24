# Define a user-defined function with four arguments and default values
def my_function(arg1, arg2, arg3=0, arg4=1):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)
    print("arg4:", arg4)
    print("")


for i in range(3):
    print("Test case", i+1)
    arg1 = input("Enter argument 1: ")
    arg2 = input("Enter argument 2: ")
    arg3 = input("Enter argument 3: ")
    arg4 = input("Enter argument 4: ")
    my_function(arg1, arg2, arg3, arg4)
