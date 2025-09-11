try:
    user_input = input("Enter text to write to the file:")
    with open("output.txt", "w") as file:
        file.write(user_input+ "\n")
    print("Data successfully written to output.txt")

    add_input = input("Enter additional text to append:")
    with open("output.txt", "a") as file:
        file.write(add_input+ "\n")
    print("Data successfully appended")

    with open("output.txt", "r") as file:
        content = file.read()
        
    print("Final Content of output.txt:")
    print(content)

except FileNotFoundError:
    print("The file 'output.txt' was not found.")