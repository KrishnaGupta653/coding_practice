import re

# a. Matches a string that has an ‘a’ followed by three ‘b’.

string = 'abbb abc abbbb bac babbb'
matches = re.findall('abbb', string)
print("a. Matches for abbb in ",string ,":",matches)

# b. Write a Python program to search for numbers (0-9) of length between 1 and 3 in a given string.
pattern = r'\b\d{1,3}\b'
string = 'no.are: 1983, 187 ,2003, 1033 ,31 '
matches = re.findall(pattern, string)
print(f'b. Matches for "{pattern}" in "{string}": {matches}')

# c. Search for a literal string in a string and also find the location within the original string where the pattern occurs.

string = 'The Ship is sailing in the sea'
match = re.search('the', string)
if match:
    print(f'c. Found "{pattern}" in "{string}" at position {match.start()}')

# d. Find all five-character words in a string.
string = 'Title: The subtle art of not giving  bugss'
matches = re.findall(r'\b\w{5}\b', string)
print(f'd. Matches for "{pattern}" in "{string}": {matches}')

# e. Check if the date of birth entered is valid or not.
pattern = r'^\d{2}-\d{2}-\d{4}$'
dob = input('Enter date of birth in format DD-MM-YYYY: ')
if re.match(pattern, dob):
    print(f'e. Date of birth "{dob}" is valid.')
else:
    print(f'e. Date of birth "{dob}" is not valid.')
