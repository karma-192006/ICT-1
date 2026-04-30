# Lab02_pairNumber.py
# Smart Classroom Quiz & Performance Analyzer
# Each step is explained with comments

# Step 1: collecting of last 2 digtits from student ID
student1_id = int(input("Enter Student 1 ID: "))
student2_id = int(input("Enter Student 2 ID: "))

# Take last 2 digits
last_two_1 = student1_id % 100
last_two_2 = student2_id % 100

# Generate unique value
unique_value = (last_two_1 + last_two_2) % 10
print(f"Unique value generated: {unique_value}")

# Step 2: prompt names
students = {}
while True:
 name = input("Enter student name (or type 'exit' to stop): ").strip()
 if name.lower() == "exit":
  break
 if name == "":
  print("Warning: Blank name entered. Skipping...")
 continue
 students[name] = 0 # 0 score initialized 

# Step 3: show names of students
print("Registered Students:")
for student in students.keys():
 print(student)

# Step 4: Conduct quiz for each student
for student in students.keys():
 print(f"Quiz for {student}:")
 score = 0