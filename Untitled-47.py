# dictionary of student names and their marks in 4 subjects
marks = {
    'Krishna': [80, 90, 100, 70],
    'Bob': [60, 70, 75, 80],
    'Charlie': [90, 80, 85, 95],
    'David': [70, 75, 65, 80],
    'Emma': [85, 90, 80, 85],
    'Frank': [75, 80, 70, 75],
    'Grace': [95, 85, 90, 95],
    'Harry': [60, 65, 70, 75],
    'Ivy': [80, 85, 80, 75],
    'Jack': [90, 95, 85, 90]
}

# dictionary to store student names and their total marks
tm = {}

# calculate the total marks for each student
for n,s in marks.items():
    tm[n] = sum(s)

# print the dictionary of total marks
print("Total marks for each student:")
print(tm)

# find the topper and their score
topper = max(tm, key=tm.get)
top_score = tm[topper]

# print the topper and their score
print("The topper is ",topper, " with a score of ",top_score)
