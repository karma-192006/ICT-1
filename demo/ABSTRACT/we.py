students_list = []
students_dict = {}

while True:
    name = input("Enter student name: ")
    age = input("Enter age: ")
    grade = input("Enter grade: ")

    students_list.append(name)
    students_dict[name] = {"Age": age, "Grade": grade}

    print("Student added successfully!\n")

    choice = input("Do you want to add another student? (yes/no): ")
    if choice.lower() != "yes":
        break

# Display all students
print("\nAll Students:")
for name, details in students_dict.items():
    print("Name:", name)
    print("Age:", details["Age"])
    print("Grade:", details["Grade"])
    print()