# Define a user-defined function to sort strings2
def sort_strings(s):
    n = len(s)
    temp=''
    for i in range(n-1):
            if s[i] > s[i + 1]:
                s[i]=temp
                s[i]=s[i+1]
                s[i+1]=temp

    return s


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
