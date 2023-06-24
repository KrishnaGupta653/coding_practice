# Create two sets of your own choice
set1 = {1, 2, 3, 4, 5,6}
set2 = {4, 5, 6, 7, 8,9}

# Find the union of the two sets
union_set = set1.union(set2)
print("Union of the two sets:", union_set)

# Find the intersection of the two sets
intersection_set = set1.intersection(set2)
print("Intersection of the two sets:", intersection_set)

# Find the difference of the two sets
difference_set = set1.difference(set2)
print("Difference of the two sets (set1 - set2):", difference_set)

# Find the symmetric difference of the two sets
symmetric_difference_set = set1.symmetric_difference(set2)
print("Symmetric difference of the two sets:", symmetric_difference_set)
