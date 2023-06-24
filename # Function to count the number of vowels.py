# Function to count the number of vowels in a given string
def vowels(string):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    for char in string:
        if char in vowels:
            vowel_count += 1
    return vowel_count

# Function to count the number of digits in a given string
def digits(string):
    digit_count = 0
    for char in string:
        if char.isdigit():
            digit_count += 1
    return digit_count

# Function to replace a character with a symbol in a given string
def replace_character(string, character, symbol):
    new_string = string.replace(character, symbol)
    return new_string

# Create a bio data file
with open("bio_data.txt", "w") as file:
    file.write("Name: Yogiraj Mantri\n")
    file.write("Age: 32\n")
    file.write("Address: A-Block Baltimore Road Vellore\n")
    file.write("Email: yogiraj12@hotmail.com\n")
    file.write("Phone: 987654321\n")
    file.write("Profession: Professor \n")
# Read the contents of the bio data file
with open("bio_data.txt", "r") as file:
    bio_data = file.read()

# Count the number of vowels in the bio data
vowel_count = vowels(bio_data)
print("Number of vowels:", vowel_count)

# Count the number of digits in the bio data
digit_count = digits(bio_data)
print("Number of digits:", digit_count)

# Replace a character in the bio data with a symbol
character_to_replace = "o"
replacement_symbol = "*"
new_bio_data = replace_character(bio_data, character_to_replace, replacement_symbol)
print("Updated bio data:\n", new_bio_data)
