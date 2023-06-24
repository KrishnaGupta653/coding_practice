numbers = list(map(int, input().split()))
print(numbers)
even_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
print(even_numbers)

