# # 17-09-26
# # E. Datatypes in Python
# # 1.Simple Types - str(Seq type), number(int,float,complex number)
# # 2.Complex Types/Collection Types - List, Dictionary, Tuples, Set
# # 3.Misc Types - Bool, None, range, bytes, memoryview
#
# # # list- Indexed Sequenced collection of homogeneous(not mandatorily) elements / items
# # list is ordered , mutable and allows duplicates
#
# #indexed example in list
# aspirants_name_list=['Vijay kumar','Meena Velusamy','andrew Prasad','srimanasa']
# aspirants_age_list=[31,22,30,31]
#
# print(aspirants_name_list[0])
# print(aspirants_name_list[1])
#
#
# # sequenced example in list
# for name in aspirants_name_list:
#     print(name.capitalize())
#
# #tuples () - Indexed Sequenced collection of HETROGENEOUS (not mandatorily) elements/items
# #tuples are otherwise called as record/row
# #indexed
# #Indexed? yes, i can access the elements/items using index
# print("Let us see tuple is indexed? yes")
# aspirants_tuple=('Vijay kumar',31,'Chennai','IT Professional')
# print(aspirants_tuple[0])
# print(aspirants_tuple[1])
#
# #Sequenced? yes, i can able to do looping, hence sequenced
# print("Let us see tuple is sequenced? yes")
# for i in aspirants_tuple:
#     print(str(i).capitalize())
#
# #dictionary
# #dict {key1:val1,key2:val2} - Sequenced collection of key value pairs
#
# # Dictionary stores data in key-value pairs. Keys must be unique, and
# # we access values using the key instead of an index.Dictionary stores data in key-value pairs.
# # Keys must be unique,and we access values using the key instead of an index.
#
# aspirants_name_age_dict={'Vijay kumar':31,'Meena Velusamy':22,'andrew Prasad':30,'srimanasa':31}
# print(aspirants_name_age_dict)
#
# #Sequenced? yes, i can able to do looping, hence sequenced
# print("printing keys alone")
# for name in aspirants_name_age_dict:#It  returns keys alone
#     print(name.capitalize())
# print("printing values alone")
# for age in aspirants_name_age_dict.values():#It  returns values alone
#     print(age)
# print("printing both keys and values (items)")
# for name,age in aspirants_name_age_dict.items():#It  returns items alone
#     print(name,age)

# List          → Column
# Dictionary    → Key → Value lookup
# Tuple         → One row
# List of Tuple → Multiple rows + columns
# -------------------------------------------------------------------------------------------------
# 18/09/26
# Tuple → Store the details of one student: (name, age, course).
# Set → Store the unique courses taken by students.
# Dictionary → Store each student's name and their marks.
# #
# stu_lst = ['arun','rajesh','praveen','deeksha','angel']
# stu_details =[('arun',19,'de'),('rajesh',22,'python'),('praveen',24,'sql'),
#               ('deeksha',25,'sql'),('angel',24,'data science')]
# course={'de','python','sql','sql','data science'}
# marks = {
#     'arun': 85,
#     'rajesh': 80,
#     'praveen': 70,
#     'deeksha': 50,
#     'angel': 86
# }
# # list seq
# for i in stu_lst:
#     print(i)
#
# #list index
#
# print( stu_lst[5])
#
# # # is list is mutable? yes
# # replace
# stu_lst[2]='kavi'
#
# # append - new data
# stu_lst.append('priya')
#
# # remove - one data
# stu_lst.remove('priya')
#
# # delete student value using index
# del students[3]
#
# #if spelling mistake
# stu_lst[1] = "rajeshhhn"
# # ------------------------------------------------------------------------------------
# # list of tuple is sequence
# for stu in stu_details:
#     print(stu)
# #
# # del
# del stu_details[0]
# print(stu_details)
#
# # checking for tuple
# tuple_lst = ('arun',19,'de'),('rajesh',22,'python'),('praveen',24,'sql')
# print(tuple_lst)
# tuple_lst = ('varun',29,'ds')
# print(tuple_lst)
# tuple_lst.append(('deeksha',25,'sql'))
# for stu in tuple_lst:
#     print(stu)



# ------------------------------------------------------------------------------------
# Use Case 1: Internet Data Usage Calculator
# Write a program that asks the user for:
# Total monthly data limit (in GB)
# Data used so far (in GB)
#
#
# Calculate using arithmetic operators:
#  Remaining data = limit - used
#  Usage percentage = (used / limit) * 100
# Print:
# Remaining data
# Usage percentage rounded to 2 decimals
#
#
# If usage percentage is greater than or equal to 80, print:
#  "Warning: High usage, consider upgrading your plan."
#
# monthly_data = int(input("Enter monthly data limit: "))
# data_used = int(input("Enter data used: "))
# Remaining_data = monthly_data - data_used
# Usage_percentage = (data_used / monthly_data) * 100
# print('remaining data is :',Remaining_data)
# print('usage percentage is:',round(Usage_percentage, 2))
# if Usage_percentage >= 80:
#     print('Warning: High usage, consider upgrading your plan.')

# -----------------------------------------------------------------------------------------
# Write a program that takes:
# Original price (float)
# Discount percent (int)
#
#
# Using assignment and arithmetic operators, calculate:
#  Discount amount = (price * discount_percent) / 100
#  Final price = price - discount_amount
# Print:
#  Original price, discount applied, and final payable amount.

# original_price = float(input("Enter original price: "))
# discount_percent = int(input("Enter discount percent: "))
#
# Discount_amount = (original_price * discount_percent) / 100
# Final_price = original_price - Discount_amount
# print('orignal price is:',original_price)
# print('discount applied:',Discount_amount)
# print('Final payable anount is:',Final_price)
#
# ----------------------------------------------------------------------------------------------
#
#
# # The following code should determine voting eligibility, but it contains operator mistakes. Fix it.
# # Incorrect code:
# age = int(input("Enter age: "))
# citizen = input("Are you an Indian citizen? (yes/no)")
# if age > 18 and citizen == "yes":
#     print("Eligible to vote")
# else:
#     print("Not eligible")
# # Expected behavior:
# # Convert age to integer before comparison.
#
# #
# # Only print "Eligible to vote" if age is 18 or above AND citizen input is "yes" (case-insensitive).
#
#
# age = int(input("Enter age: "))
# citizen = input("Are you an Indian citizen? (yes/no)")
# if age > 18 and citizen == "yes":
#     print("Eligible to vote")
# else:
#     print("Not eligible")

# Use Case 1: Banking Eligibility Check
# Write a program that asks the user for:
# Age
# Monthly income
#
#
# Conditions:
# If age < 18: print "Not eligible for a bank account."
# If age >= 18 and income < 15000: print "Eligible for basic savings account."
# If age >= 18 and income between 15000 and 50000: print "Eligible for savings + salary account."
# If age >= 18 and income > 50000: print "Eligible for premium account."
try:
    age = int(input("Enter age: "))
    monthly_income=float(input("Enter monthly income: "))
    if age<18:
        print("not eligible for a bank account")
    elif monthly_income <= 0:
        print("Please enter a valid monthly income")
    elif age>=18 and monthly_income < 15000:
        print("eligible for bank savings account")
    elif age>=18 and monthly_income < 50000:
        print("eligible for savings + salary account")
    elif age>=18 and monthly_income > 50000:
        print("eligible for premium account")
except ValueError:
    print("Please enter numbers only")







































