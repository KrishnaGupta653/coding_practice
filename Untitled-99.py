# Recursive function to find the sum of first N natural numbers
def sum(n):
    if n == 1:
        return 1
    else:
        return n + sum(n - 1)

# Recursive function to calculate the power of a number
def power(b, e):
    if e == 0:
        return 1
    else:
        return b * power(b, e - 1)

# Recursive function to generate the Fibonacci sequence
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Menu-driven script
while True:
    print("MENU:")
    print("1. Calculate sum of first N natural numbers")
    print("2. Calculate power of a number")
    print("3. Generate Fibonacci sequence")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        n = int(input("Enter the value of N: "))
        result = sum(n)
        print("The sum of first", n, "natural numbers is:", result)

    elif choice == '2':
        b = int(input("Enter the base number: "))
        e = int(input("Enter the exponent: "))
        result = power(b, e)
        print(b, "raised to the power", e, "is:", result)

    elif choice == '3':
        n = int(input("Enter the value of N: "))
        print("Fibonacci sequence:")
        for i in range(n):
            fib = fibonacci(i)
            print(fib, end=" ")

    elif choice == '4':
        print("Exiting the program...")
        break

    else:
        print("Invalid choice! Please enter a valid option (1-4).")
