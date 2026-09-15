'''A. Python is an indent based programming language
The following program throws an indentation error. Correct it and make sure it prints p'''

# teams = ['Data', 'AI', 'DevOps']
# for t in teams:
#     print('Hello', t, 'Team from Inceptez Technologies')
#     print('Keep Learning and Exploring!')

'''Use Case 1:
Add single-line and multi-line comments to describe what the below code does for Inceptez Technologies’ training tracker.'''

# # number of students declared as a variable
# students = 100
# #number of trainers declared in variable called trainers
# trainers = 2
# #calculate total students and trainers declared as a variable called total then print the value
# total = students + trainers
# print(total)


#C. Playing with Quotes
#This is Inceptez's "Python" class for Data Engineers & AI Engineers


'''Welcome to Inceptez Technologies!
Python Training: Basics
Enjoy your learning journey'''

'''D. Let's learn all about VARIABLES
Use Case 1:
Declare variables to store the following details:
- Student Name
- Course Name (e.g., “Python Fundamentals”)
- Training Institute Name (Inceptez Technologies)

Then print a formatted message:

Name: Arun is learning the course Python Fundamentals at the institute Inceptez Technologies'''


# student = 'Arun'
# course_name = 'Python Fundamentals'
# training_institute = 'Inceptez Technologies'
# print (f"{student} is learning the course {course_name} at the institute {training_institute}")
#
# fee = 45000
# print(type(fee))
# print(fee)
#
# fee =str(fee)
# print(type(fee))
# print(fee)

#Variables Naming Conventions
# student = 'Ravi'
# _student_id = 1001
# studentName = 'Priya'
# name = 'Python'
# inceptez_batch = 'Morning'
# print(student)
# print(_student_id)
# print(name)
# print(inceptez_batch)

#PascalCase: DataEngineeringBatch -PascalCase → First letter Capital
#camelCase: dataEngineeringBatch-camelCase → First letter small, remaining words Capital
#snake_case: data_engineering_batch-snake_case → Words connected with underscore

#variable naming conventions
# 2student = indhu - (its not valid in variable)
# # class name = 'Python' (this is built-in-concepts of oops . this is n)
# age = input("Enter employee's age:")
# print(type(age))

##########################################################################################
#today
# F. Type identification & Casting

# age = input("Enter employee's age")
# age = int(age)
# retire_age=60
# years_pending = retire_age - age
# print(f"you will retire in {years_pending} in years")

# Fix the type error in the following code for salary calculation:

# salary = '50000'
# salary = int(salary)
# bonus = 10000
# print('Total Salary in Inceptez:', salary + bonus)

# G. Data types and casting

# Use Case 1 — Employee Salary Breakdown Using Numeric & String Types
# Employee Salary Breakdown
# a. Write a program that asks the user for:
# employee_name (string)
# base_salary (float)
# hra_percent (integer)
# bonus_amount (float)

# emp_name = input('Enter your name: ')
# base_salary= float(input ('Enter your salary: '))
# hra_percent = int(input('Enter your hra percentage: '))
# bonus_amount=float(input('Enter your bonus amount: '))
# HRA = base_salary * (hra_percent / 100)
# Total_Salary = base_salary + HRA + bonus_amount
# print('employee:',emp_name)
# print('Base salary:',base_salary)
# print('HRA @', hra_percent, "%:", HRA)
# print('Bonus:',bonus_amount)
# print('Total salary payable: ₹',Total_Salary)

# B. Convert inputs to the correct datatype if required.
# Calculate:
#  HRA = base_salary * (hra_percent / 100)
#  Total Salary = base_salary + HRA + bonus_amount

# C. Print the output like this:
# Employee: Arun
# Base Salary: 40000.0
# HRA @ 20%: 8000.0
# Bonus: 5000.0
# Total Salary Payable: ₹53000.0

# Use Case 2: Student Result Classification
# a. Write a program that takes marks as input (initially as a string).
# B. Check if the value can be converted to float.
# C. Then classify (try using if condition with the help of AI, however we will learn about if condition soon):
# Marks >= 90 --> Outstanding
#  Marks >= 75 --> Excellent
#  Marks >= 50 --> Pass
#  Marks < 50 --> Fail
# D. If the input is not numeric, print:
#  Invalid marks entered — Please provide numeric input
try:
    mark= float(input("Enter your mark: "))
    if mark >=90:
        print('outstanding')
    elif mark >=75:
        print('excellent')
    elif mark >=50:
        print('pass')
    else:
        print('fail')

except ValueError:
    print ("Invalid marks entered — Please provide numeric input.")


# Use Case 3: Bug Fixing — Datatype Mismatch
# # The below code is intended to calculate total price, but it has datatype errors. Fix it.
# # Incorrect code:

# Expected output after fixing:
# item_name = input("Enter product name: ")
# price = float(input("Enter price per item: "))
# quantity = int(input("Enter quantity: "))
# total_cost = price * quantity
# print("You purchased " , quantity , " units of " , item_name)
# print("Total payable: " ,total_cost ,'INR')
# Enter product name: Notepad
#  Enter price per item: 35.50
#  Enter quantity: 3
# You purchased 3 units of Notepad
#  Total payable: 106.5 INR



















