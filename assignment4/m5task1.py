try:
    with open("sample.txt", "r") as file:
        content = file.read()
        print("Reading file content:")
        print(content)

except FileNotFoundError:
    print("The file 'sample.txt' was not found.")
    