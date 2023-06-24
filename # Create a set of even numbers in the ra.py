# Create a set of even numbers in the range 1-10 using if condition
even_numbers = set()
for i in range(1, 11):
    if i % 2 == 0:
        even_numbers.add(i)

# Create a set of composite numbers in the range 1-20 using if condition
composite_numbers = set()
for num in range(1, 21):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                composite_numbers.add(num)
                break
# Demonstrate the use of all(), issuperset(), len(), and sum() functions
print("Set of even numbers: ", even_numbers)
print("Set of composite numbers: ", composite_numbers)
print("Are all numbers in the even set even? ", all(num % 2 == 0 for num in even_numbers))
print("Is the even set a superset of the composite set? ", even_numbers.issuperset(composite_numbers))
print("Length of the even set: ", len(even_numbers))
print("Sum of the composite set: ", sum(composite_numbers))
