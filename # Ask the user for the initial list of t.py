# Ask the user for the initial list of toppers
toppers = []
n = int(input("Enter the number of toppers: "))
for i in range(n):
    name = input("Enter the name of topper {}: ".format(i+1))
    marks = []
    for j in range(3):
        mark = int(input("Enter the mark of subject {}: ".format(j+1)))
        marks.append(mark)
    toppers.append([name] + marks)

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
