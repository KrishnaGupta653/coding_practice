# Ask the user for the dimensions of the matrix
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

# Create an empty matrix
matrix = []

# Ask the user to enter the elements of the matrix
for i in range(rows):
    row = []
    for j in range(cols):
        element = int(input("Enter the element at position ({}, {}): ".format(i, j)))
        row.append(element)
    matrix.append(row)

# Print the matrix
print("The matrix is:")


for row in matrix:
    print(row)
