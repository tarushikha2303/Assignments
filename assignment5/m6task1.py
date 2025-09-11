students = {
    "Alice": 85,
    "Ram": 92,
    "Sita": 78,
    "Arjun": 96,
    "Bheem": 88
}

try:
    name = input("Enter the student's name: ")

    if name in students:
        print(f"{name}'s marks: {students[name]}")
    else: 
        raise KeyError("Student not found!")
except KeyError as e:
    print(f"Error: {e}")