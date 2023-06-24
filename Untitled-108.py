number = int(input("enter no."))
digit_count = 0
if number == 0:
    digit_count = 1
else:
    if number < 0:
        number = -number



    while number != 0:
        number //= 10
        digit_count += number
        print(number)

print("Number of digits:", digit_count)
