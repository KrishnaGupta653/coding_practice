# Define a user-defined function to sort strings
def sort_strings(strings):
    n = len(strings)

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if strings[j] > strings[j + 1]:
                strings[j], strings[j + 1] = strings[j + 1], strings[j]

    return strings


# Take input from the user for five strings
strings = []
for i in range(5):
    string = input("Enter a string: ")
    strings.append(string)

# Call the user-defined function to sort the strings
sorted_strings = sort_strings(strings)

# Print the sorted strings
print("Sorted strings:")
for string in sorted_strings:
    print(string)
