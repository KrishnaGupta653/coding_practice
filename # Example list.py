# Example list
my_list = [1, 2, 3, 4, 5]

# Remove element at index 2
index_to_remove = 2
my_list = my_list[:index_to_remove] + my_list[index_to_remove+1:]

print(my_list)
