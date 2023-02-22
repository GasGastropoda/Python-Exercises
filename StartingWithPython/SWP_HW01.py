# Page 37: Program 2-1 | output.py
# This is a simple program which prints out a name and two address lines.
print('Kate Austen')
print('123 Full Circle Drive')
print('Asheville, NC 28899')
# The printed results are string values. 
# string literals must be in quotation marks. 

# Page 37: Program 2-2 | double_quotes.py
# simple program which prints strings surrounded in double quotes
print("Kate Austen")
print("123 Full Circle Drive")
print("Asheville, NC 28899")
# shows that strings can be surrounded by either single or double quotes

# Page 38: Program 2-3 | apostrophe.py
# A program which explains that apostrophes can be used in strings, but they must be surrounded by double quotes
print("Don't fear!")
print("I'm here!")

# Page 38: Program 2-4 | display_quote.py
# A program which explains that quotes can be used in strings, but they must be surrounded by single quotes.
print('Your assignment is to read "Hamlet" by tommorow')

# checkpoint:
# 2.7 Write a program that displays your name
print('Maria de los Angeles')
# 2.8 Write a statement that displays the following text: Python's the best!
print("Python's the best!")
# 2.9 Write a statement that displays the following text: The cat said "meow".
print('The cat said "meow".')

# Page 39: Program 2-5 | comment1.py
# This program explains the use of comments
# but I've been using them all along. so no point in trying to explain them now.

# Page 40: Program 2-6 | comment2.py
# This program explains the use of end-line comments
print('Kate Austen') # Displays the name
print('123 Full Circle Drive') # Displays the address
print('Asheville, NC 28899') # Displays the city, state, and zip

# Page 42: Program 2-7 | variable_demo.py
# This program demonstrates a variable
room = 503
print('I am staying in room number')
print(room)

# Page 42: Program 2-8 | variable_demo2.py
# Creates two variables: top_speed and distance
top_speed = 160
distance = 300
# Display the values referenced by variables
print('the top speed is')
print(top_speed)
print('the distance traveled is')
print(distance)

# Page 45: Program 2-9 | variable_demo3.py
# Program which prints several items in one function
# This program demonstrates a variable
room = 503
print('I am staying in room number', room)

# Page 46: Program 2-10 | variable_demo4.py
# Program which shows how to reassign variables
# This program demonstrates variable assignment
# Assign a value to the dollars variable
dollars = 2.75
print('I have', dollars, 'in my account.')
# Reassign dollars so it references a different value
dollars = 99.95
print('But now I have', dollars, 'in my account!')

# Page 48: Program 2-11 | string_variable.py
# This is a program which shows how to store strings within variables
# Create variables to reference two strings
first_name = 'Kathryn'
last_name = 'Marino'
# Display the values referenced by the variables
print(first_name, last_name)

# Page 50: Program 2-12 | string_input.py
# This is a program which allows user input and converts it into a string
first_name = input('Enter your first name: ')  # Get the user's first name
last_name = input('Enter your last name: ')  # Get the user's last name
print('Hello', first_name, last_name)  # Print a greeting to the user

# Page 52: Program 2-13 | input.py
# This is a program which converts string input into an integer
# Get the user's name, age, and income
name = input('What is your name? ')
age = int(input('What is your age? '))
income = float(input('What is your income? ')) # In order to include a float, you need to convert the string into it. So surround the input with float()
# Display the data
print('Here is the data you entered:')
print('Name:', name)
print('Age:', age)
print('Income:', income)

# Page 54: Program 2-14 | simple_math.py
# This is a program which does basic arithmetic 
salary = 2500.0  # Assign a value to the salary variable
bonus = 1200.0 # Assign a value to the bonus variable
pay = salary + bonus
print('Your pay is', pay)  # Display the pay

# Page 55: Program 2-15 | sale_price.py
# This is a program which calculates the sale price of an object 
# This program gets an item's original price and calculates its sale price with a 20% discount
original_price = float(input("Enter the item's original price: "))  # Get the item's original price
discount = original_price * 0.2  # Calculate the amount of the discount
sale_price = original_price - discount  # Calculate sale price
print('The sale price is', sale_price)  # Display sale price

# Page 59: Program 2-16 | test_score_average.py
# a program which shows the order of operations in python
# Order of Operations is refered to as Operator precedence in python.
# the presendence is exponentiation, multiplication, division, and remainder, and finally addition and subtraction
# Get three test score and assign them variables
test1 = float(input('Enter the first test score: '))
test2 = float(input('Enter the second test score: '))
test3 = float(input('Enter the third test score: '))
# Calculate the average of all three scores
average = (test1 + test2 + test3) / 3.0
# Display the average
print('The average score is', average)

# Page 63: Program 2-18 | future_value.py
# This is a program which converts an algebraic statement into executable code
# Get the desired future value
future_value = float(input('Enter the desired future value: '))
# Get the annual interest rate
rate = int(input('Enter the annual interest rate: '))
# Get the number of years that the money will appreciate
years = int(input('Enter the number of years the money will grow: '))
#calculate the amount needed to deposit
present_value = future_value / (1.0 + rate)**years
# Display the amount needed to deposit
print('you will need to deposit this amount:', present_value)

# Page 66: Program 2-19 | concatenation.py
# This is a program showing how strings concatenate (add)
# This program demonstrates string concatenation
first_name = input('Enter your first name: ')
last_name = input('Enter your last name: ')
# Combine the names with a space between them
full_name = first_name + '' + last_name
# Display the user's full name
print('Your full name is ' + full_name)

# Page 72: Program 2-20 | f_string_no_formatting.py
# This is a program using an f-string (formatted string literal) without formatting a floating-point
# f-strings are a way to formate the output shown with the print function. They can create messages including variable content. 
# To use an f-string, use an f before the string you want to display. ie. f'hello world'
# When the f is used, it will replace the variable placeholder with the actual value it addresses
amount_due = 5000.0
monthly_payment = amount_due / 12.0
print(f'The monthly payment is {monthly_payment}.')

# Page 72: Program 2-21 | f_string_rounding.py
# demonstrates how a floating point number can be rounded.
# you can append the format specifier .2f inside of the placeholder
amount_due = 5000.0
monthly_payment = amount_due / 12.0 
print(f'The monthly payment is {monthly_payment:.2f}.')

# Page 73: Program 2-22 | dollar_display.py
# python is weird about how commas are printed. in order to print the comma, you include it before rounding the decimal within the placeholder's format specifier
monthly_pay = 5000.0
annual_pay = monthly_pay * 12
print(f'Your annual pay is ${annual_pay:,.2f}')

# Page 76: Program 2-23 | columns.py
# this program shows how python creates columns of data are made
# The program displays numbers in two columns
num1 = 127.899
num2 = 3465.148
num3 = 3.776
num4 = 264.821
num5 = 88.081
num6 = 799.999
# Each number is displayed in a field of 10 spaces and rounded to two decimal places
print(f'{num1:10.2f}{num2:10.2f}')
print(f'{num3:10.2f}{num4:10.2f}')
print(f'{num5:10.2f}{num6:10.2f}')
