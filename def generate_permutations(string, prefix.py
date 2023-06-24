def generate_permutations(string, prefix=""):
    if len(string) == 0:
        print(prefix)
        return

    for i in range(len(string)):
        rem = string[:i] + string[i+1:]
        generate_permutations(rem, prefix + string[i])

# Example usage
input_string = input("Enter a string: ")
generate_permutations(input_string)
