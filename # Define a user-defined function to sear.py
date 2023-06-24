# Define a user-defined function to search for a friend
def search(friend, name):
    if name in friend:
        return friend[name]
    else:
        return "Friend not found."

# Create a dictionary to store your friends' details
fdict = {}

# Take input from the user for your friends' details
n = int(input("Enter the number of friends: "))
for i in range(n):
    name = input("Enter the name of a friend: ")
    age = input("Enter the age of {} : ".format(name))
    phone = input("Enter the phone number of {} : ".format(name))
    fdict[name] = {"Age": age, "Phone": phone}

# Take input from the user for the friend to search
search_name = input("Enter the name of the friend to search: ")

# Call the function to search for the friend
f_details = search(fdict, search_name)

# Print the result
print(fdict)
print(f_details)
