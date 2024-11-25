# x=7.8
# y=9
# print(int(x+y))

# # Simple Calculator in Python

# def add(x, y):
#     return x + y

# def subtract(x, y):
#     return x - y

# def multiply(x, y):
#     return x * y

# def divide(x, y):
#     if y == 0:
#         return "Error! Division by zero."
#     else:
#         return x / y

# def calculator():
#     print("Select operation:")
#     print("1. Add")
#     print("2. Subtract")
#     print("3. Multiply")
#     print("4. Divide")

#     # Take input from the user
#     choice = input("Enter choice (1,2,3,4): ")

#     if choice in ['1', '2', '3', '4']:
#         num1 = float(input("Enter first number: "))
#         num2 = float(input("Enter second number: "))

#         if choice == '1':
#             print(f"{num1} + {num2} = {add(num1, num2)}")

#         elif choice == '2':
#             print(f"{num1} - {num2} = {subtract(num1, num2)}")

#         elif choice == '3':
#             print(f"{num1} * {num2} = {multiply(num1, num2)}")

#         elif choice == '4':
#             print(f"{num1} / {num2} = {divide(num1, num2)}")
#     else:
#         print("Enter a valid input")


# calculator()

# import math

# def calculate_area(radius):
#     return math.pi * radius ** radius

# # Take radius input from the user
# radius = float(input("Enter the radius of the circle: "))

# # Compute the area
# area = calculate_area(radius)

# # Display the result
# print(f"The area of the circle with radius {radius} is: {area}")


# Importing required library
from tabulate import tabulate

# Function to calculate grade based on marks
def calculate_grade(marks):
    if marks >= 85:
        return 'A*'
    elif 70 <= marks < 85:
        return 'A'
    elif 65 <= marks < 70:
        return 'B'
    elif 60 <= marks < 65:
        return 'C'
    else:
        return 'F'

# Function to create the marksheet
def generate_marksheet():
    # Collecting student's information
    name = input("Enter the student's name: ")
    roll_number = input("Enter the student's roll number: ")

    # Collecting marks for subjects
    ai_marks = float(input("Enter marks for AI: "))
    ms_marks = float(input("Enter marks for Model and Simulation: "))
    cn_marks = float(input("Enter marks for Computer Networking: "))
    se_marks = float(input("Enter marks for Software Re-engineering: "))

    # Preparing data for tabular display
    subjects = ["AI", "Model and Simulation", "Computer Networking", "Software Re-engineering"]
    marks = [ai_marks, ms_marks, cn_marks, se_marks]
    grades = [calculate_grade(ai_marks), calculate_grade(ms_marks), calculate_grade(cn_marks), calculate_grade(se_marks)]

    # Creating the table
    table = [[subjects[i], marks[i], grades[i]] for i in range(4)]

    # Displaying the result in a tabular format
    print("\n\nMARKSHEET")
    print(f"Name: {name}")
    print(f"Roll Number: {roll_number}")
    print(tabulate(table, headers=["Subject", "Marks", "Grade"], tablefmt="grid"))

# Run the program
generate_marksheet()
