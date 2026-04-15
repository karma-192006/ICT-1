# Creating an empty list to store student names
students_list = []

# Creating an empty dictionary to store student information
# Key:student name and value:age and grade
students_dict = {}

#Asking the user to enter their name, age and grade.
Name=input("Enter your name: ")
age=int(input("Enter your age: "))
grade=input("Enter your grade: ")

#Adding the input in lists and dictionaries
students_list.append(Name)
students_dict[Name]={"Age": age, "Grade":grade}

# Printing a success message
print("Student information added successfully!")

# Additionally, printing the items of the dictionary to view student details. 
print("Student Details:")
for key, value in students_dict.items():
    print("Name:", key)
    print("Age:", value["Age"])
    print("Grade:", value["Grade"])
    print()

# Searching for a student by name
search_name = input("Enter student's name to search: ")

#Giving the information of the student if the student searched is found 
if search_name in students_dict:
    print("Name:", search_name)
    print("Age:", students_dict[search_name]["Age"])
    print("Grade:", students_dict[search_name]["Grade"])
# If the student searched is not found, displaying that the searched student is not found
else:
    print("Student not found.")

# Removing the student information typed by the user
remove_name = input("Enter name to remove: ")

if remove_name in students_dict:
    students_list.remove(remove_name)
    del students_dict[remove_name]
    print("Student removed successfully!")
else:
    print("Student not found.")

