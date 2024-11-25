x=7.8
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


# # Importing required library
# from tabulate import tabulate

# # Function to calculate grade based on marks
# def calculate_grade(marks):
#     if marks >= 85:
#         return 'A*'
#     elif 70 <= marks < 85:
#         return 'A'
#     elif 65 <= marks < 70:
#         return 'B'
#     elif 60 <= marks < 65:
#         return 'C'
#     else:
#         return 'F'
