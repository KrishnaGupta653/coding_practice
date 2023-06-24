string = input("Enter a string: ")
sorted_string = ""
while string:
    smallest_char = string[0]
    for char in string:
        if char < smallest_char:
            smallest_char = char
    sorted_string += smallest_char
    string = string.replace(smallest_char, "", 1)
print("Sorted string:", sorted_string)

string=input("enter a string:")
sorted_string=""
while string:
    smallest_char=string[0]
    for char in string:
        if char<smallest_char:
            smallest_char=char
sorted_string+=smallest_char
string=string.replace(smallest_char," ",1)
print("sorted string:", sorted_string)