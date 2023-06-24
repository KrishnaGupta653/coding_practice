# Get the dimensions of the matrix from the user
rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))

matrix = []

# Get the matrix elements from the user
for i in range(rows):
    row = []
    for j in range(columns):
        element = int(input("Enter the element at position",(i+1 ,j+1)))
        row.append(element)
    matrix.append(row)

# Print the matrix
print("Matrix:")
for row in matrix:
    print(row)
