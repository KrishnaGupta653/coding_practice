words = input("Enter comma separated sequence of words: ")

# split the words by comma
word_list = words.split(",")

# create a set to store unique words
unique_words = set()

# loop through the words and add to the set
for word in word_list:
    unique_words.add(word.strip())

# sort the set
sorted_words = sorted(unique_words)

# print the sorted words
print("Sorted unique words: ")
for word in sorted_words:
    print(word)

