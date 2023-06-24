# Create two sets of squares and cubes in range 1-20
squares = set()
cubes = set()

for i in range(1, 21):
        squares.add(i**2)
        cubes.add(i**3)

# Demonstrate the use of update(), pop(), remove(), add(), and clear() methods
print("Initial squares set:", squares)
print("Initial cubes set:", cubes)

# Add a new element to the squares set
if 400 not in squares:
    squares.add(400)
print("After adding 400 to squares set:", squares)

# Remove an element from the cubes set
if 1728 in cubes:
    cubes.remove(1728)
print("After removing 1728 from cubes set:", cubes)

# Update the squares set with elements from the cubes set
squares.update(cubes)
print("After updating squares set with elements from cubes set:", squares)

# Remove and return an arbitrary element from the cubes set

popped = cubes.pop()
print("Popped element from cubes set:", popped)
print("After popping an element from cubes set:", cubes)

# Clear the squares set
squares.clear()
print("After clearing squares set:", squares)
