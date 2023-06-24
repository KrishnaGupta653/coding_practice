original_str = "The quick brown fox jumps over the lazy dog"
old_str = "quick"
new_str = "slow"

# Loop through each character in the original string
modified_str = ""
for i in range(len(original_str) - len(old_str) + 1):
    # If the current character and the next characters match the old string
    if original_str[i:i+len(old_str)] == old_str:
        # Append the new string to the modified string
        modified_str += new_str
        # Skip over the old string in the original string
        i += len(old_str) - 1
    else:
        # Append the current character to the modified string
        modified_str += original_str[i]

# Print the modified string
print(modified_str)
