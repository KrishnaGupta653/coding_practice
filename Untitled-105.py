def characters(file_name):
    with open(file_name, 'r') as file:
        content = file.read()
        character_count = len(content)
    return character_count


def words(file_name):
    with open(file_name, 'r') as file:
        content = file.read()
        words = content.split()
        word_count = len(words)
    return word_count


def lines(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        line_count = len(lines)
    return line_count


def copy_file(source_file, destination_file):
    with open(source_file, 'r') as source:
        with open(destination_file, 'w') as destination:
            content = source.read()
            destination.write(content)
    print("File copied")


while True:
    print("\n---- File Operations Menu ----")
    print("1. Count Characters")
    print("2. Count Words")
    print("3. Count Lines")
    print("4. Copy File")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        file_name = input("Enter the name of the file: ")
        character_count = characters(file_name)
        print("Number of characters:", character_count)

    elif choice == '2':
        file_name = input("Enter the name of the file: ")
        word_count = words(file_name)
        print("Number of words:", word_count)

    elif choice == '3':
        file_name = input("Enter the name of the file: ")
        line_count = lines(file_name)
        print("Number of lines:", line_count)

    elif choice == '4':
        source_file = input("Enter the name of the source file: ")
        destination_file = input("Enter the name of the destination file: ")
        copy_file(source_file, destination_file)

    elif choice == '5':
        print("Exiting the program...")
        break

    else:
        print("Invalid choice! Please enter a valid option (1-5).")
