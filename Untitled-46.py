num = int(input("Enter the number of toppers: "))
toppers = []
for i in range(num):
    name = input(f"Enter the name of topper {i+1}: ")
    marks = int(input(f"Enter the marks of topper {i+1}: "))
    toppers.append([name, marks])

print("Current Toppers:")
for topper in toppers:
    print(f"{topper[0]} scored {topper[1]}")



topper_name = input("Enter the name of the topper you want to edit:")


index = -1
for topper in toppers:
    if topper[0] == topper_name:
        index = toppers.index(topper)
        break



if index != -1:
    print(f"Enter the new score for {topper_name}:")
    new_score = int(input())
    toppers[index][1] = new_score
else:
    print("Topper name not found")


print("Updated Toppers:")
for topper in toppers:
    print(f"{topper[0]} scored {topper[1]}")