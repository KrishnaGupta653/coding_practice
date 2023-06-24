# Create a nested list to store toppers details
toppers = [
    ["Alice", 95, 98, 97],
    ["Bob", 92, 94, 90],
    ["Charlie", 88, 90, 91],
    ["David", 93, 91, 95]
]

# Print the initial list of toppers
print("Initial List of Toppers:")
for topper in toppers:
    print(topper)

# Ask the user for the index of the topper to be edited
index = int(input("Enter the index of the topper to be edited (0 to {}): ".format(len(toppers) - 1)))

# Ask the user for the new details of the topper
name = input("Enter the new name of the topper: ")
marks = []
for i in range(3):
    mark = int(input("Enter the new mark in subject {}: ".format(i + 1)))
    marks.append(mark)

# Update the details of the topper in the nested list
toppers[index][0] = name
toppers[index][1:] = marks

# Print the updated list of toppers
print("Updated List of Toppers:")
for topper in toppers:
    print(topper)
