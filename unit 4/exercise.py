name = input("Enter your name: ")

# Ask for marks in three subjects
m1 = float(input("Enter your mark in Subject 1: "))
m2 = float(input("Enter your mark in Subject 2: "))
m3 = float(input("Enter your mark in Subject 3: "))

#fuction to calulate total marks
def calculate_total(m1,m2,m3):
    return m1+m2+m3
total =calculate_total(m1,m2,m3)
print("The total mark obtained of",m1,m2,"and", m3, "is:", total)

#function to calculate average
def calculate_average(m1,m2,m3):
     return (m1+m2+m3)/3
average =calculate_average(m1,m2,m3)
print("The total average mark is:", average)

#print the result to show, average>=50: retuen pass, else return fail
if average >= 50:
    print("Result: Pass")
else:
    print("Result: Fail")

#returning even and odd number
def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
num = int(input("Enter a number to check Even/Odd: "))
print("The number is:", check_even_odd(num))

