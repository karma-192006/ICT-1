student_list = [] #creates an empty list so that we can add student name 
student_age = set() #creates an empty set so that we can add student ages
student_grade = set() #creates an empty set so that we can add student grades
student_dict = {} #creates an empty dictionary so that we can add student details 

#Student 1
student_list.append ("Karma Wangdi")
student_age.add (22)
student_grade.add ("A")
student_dict ["Karma Wangdi"] = (22, "A")

#Student 2
student_list.append ("Dorji")
student_age.add (21)
student_grade.add ("A")
student_dict ["Dorji"] = (21, "A")

#Student 3
student_list.append ("Jetsun Pema")
student_age.add (19)
student_grade.add ("A")
student_dict ["Jetsun Pema"] = (19, "A")

#Student 4
student_list.append ("Sonam Tobgay")
student_age.add (25)
student_grade.add ("A")
student_dict ["Sonam Tobgay"] = (25, "A")
#I have added 4 students with their name, age, and grade to the list, set, and dictionary respectively. I have used the append() method to add student name to the list, add() method to add student age and grade to the set. I have also used dictionary to store all the details of the students with their name as the key and their age and grade as the value in the form of a tuple.





#Adding a new student name, age, and grade to the existing list, set, and dictionary
print() #printing a blank space to look clean and organized
print("----------------------------------------------------------------------------------------------------")
add_name=input("To add the name of student, 'Enter the Name' or To SKIP just 'ENTER':")
add_age=int(input("Enter the age of the student:"))
add_grade=input("Enter the grade of the student:")
print() #printing a blank space to look clean and organized
print("----------------------------------------------------------------------------------------------------")
if add_name:
    student_list.append(add_name)
    student_age.add(add_age)
    student_grade.add(add_grade)
    student_dict[add_name] = (add_age, add_grade)
    print(f"""Student added successfully with:
NAME: {add_name}  
AGE: {add_age} 
GRADE: {add_grade}""")
    
else:
    print("No student added!")
print() #printing a blank space to look clean and organized
print("----------------------------------------------------------------------------------------------------")

#To add new name, age, and grade into the existing list, i have used input function to take input from the user and then used if statement to check if the user has entered the name of the student or not. If the user has entered the name of the student, then i have used append() method to add the name to the list, add() method to add the age and grade to the set, and also added the details of the student to the dictionary with their name as the key and their age and grade as the value in the form of a tuple. If the user has not entered the name of the student, then i have printed a message "No student added!"





#Search for a student
searching_of_newly_added_name = input("Enter the name of the student to search:")
print("----------------------------------------------------------------------------------------------------")
if searching_of_newly_added_name in student_list:
    print(f"""STUDENT FOUND!          
Here are the details of the student: 
                   
The age of '{searching_of_newly_added_name}' is {student_dict[searching_of_newly_added_name][0]} 
The grade of '{searching_of_newly_added_name}' is {student_dict[searching_of_newly_added_name][1]}""")
else:
    print("Student not found")
print() #printing a blank space to look clean and organized


#To search for a student, i have used input function to take input from the user and then used if statement to check if the user has entered the name of the student or not. If the user has entered the name of the student, then i have used in operator to check if the name is present in the list or not. If the name is present in the list, then i have printed the details of the student from the dictionary using their name as the key. If the name is not present in the list, then i have printed a message "Student not found!"







#remove a student from the list, set, and dictionary
remove_name = input("Enter the name of the student to remove or enter to skip:")
print() #printing a blank space to look clean and organized

if remove_name in student_list:
    student_list.remove(remove_name)
    student_age.remove(student_dict[remove_name][0])
    student_grade.remove(student_dict[remove_name][1])
    del student_dict[remove_name]

    print("STUDENT REMOVED SUCCESSFULLY!")
    print() #printing a blank space to look clean and organized
    print("----------------------------------------------------------------------------------------------------")

    print("""Students left with their details are:
          
""", student_dict)
    print() #printing a blank space to look clean and organized

    print("""List of remaining students are:
          
""", student_list)
    print() #printing a blank space to look clean and organized

   
else:
    print("Student not found!")

print("----------------------------------------------------------------------------------------------------")

#Finally to remove a student, i have used input function to take input from the user and then used if statement to check if the user has entered the name of the student or not. If the user has entered the name of the student, then i have used in operator to check if the name is present in the list or not. If the name is present in the list, then i have used remove() method to remove the name from the list, remove() method to remove the age and grade from the set, and also used del statement to remove the details of the student from the dictionary using their name as the key. If the name is not present in the list, then i have printed a message "Student not found!"