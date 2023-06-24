with open("my_event.txt", "w") as f:
    f.write("Ayush,BCE,20000")
    f.write("Krishna,BBS,10000")
    f.write("Harsh,BDS,80000")
    f.write("Kavi,BKT,90000")
# Open the file and count the number of non-alphabetic characters
with open("my_event.txt", "r") as file:
    content = file.readlines()
    print(content)
    for char in content:
        print(char)
        #  h=(char.split(","))
        # a,b,c=h
        # print(b)
