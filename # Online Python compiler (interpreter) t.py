# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
input_string = "The quick brown fox jumps over the lazy dog"

# Convert the input string to lowercase
input_string = input_string.lower()

# Initialize a list containing all the alphabets of the English language
alphabet = list("abcdefghijklmnopqrstuvwxyz")

# Initialize an empty list to store the letters that are used in the input string
used_letters = []

# Iterate over each character in the string
for char in input_string:
    # Check if the character is an alphabet and it is not already in `used_letters`
    if char.isalpha() and char not in used_letters:
        # Append the character to `used_letters`
        used_letters.append(char)

# Sort the `used_letters` list
used_letters.sort()

# Check if `used_letters` and `alphabet` are equal
if used_letters == alphabet:
    print("The input string is a pangram")
else:
    print("The input string is not a pangram")
