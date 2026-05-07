file = open('Students.xlsx', 'w')
file.write("Name, ID\n")
file.write("seday, 08250268\n")
file.write("karma, 08250269\n")
file.write("pema, 08250270\n")
file.write("dorji, 08250271\n")
file.write("choden, 08250272\n")
file.close()
file = open('Students.xlsx', 'r')
students = file.read()
print(students)
file.close()
searchN = input("Enter a name to search: ")
found = False
with open('Students.xlsx', 'r') as file:
    for student in file:
        if searchN.lower() in student.lower():
            print(student)
            found = True
            break
if not found:
    print("Name doesn't exit")
print()
