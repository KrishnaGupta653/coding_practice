input_str = "abcdefgabc"
char_count = {}

for char in input_str:
    char_count[char] = char_count.get(char,0) + 1
    print(char_count)

for char, count in char_count.items():
    print(f"{char},{count}")