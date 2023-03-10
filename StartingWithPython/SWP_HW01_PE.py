# write a program which displays name, address, city, state, and zip
name = input('what is your name? ')
address = input('What is your address? (include your city, state and zip)')
number = input('what is your phone number? ')
major = input('What is your major? ')
print('Hello ' + name + '!')
print( 'your address is ' + address + '.')
print('your phone number is ' + number + '.')
print('and your major is ' + major + '.')

# Write a program that asks the user to enter the amount of total sales, and then displays the profit made from the amount
projected_amount = int(input('Enter the amount of total sales:'))
total_sales = projected_amount * 0.23
print(f'The total profit is ${total_sales:.2f}')

# Write a program which calculates the amount of acres in the inputted tract
tract_amount = int(input('Enter the amount of square feet in the tract: '))
total_acres = tract_amount / 43560
print(f'the total amount of acres in {tract_amount} square feet is {total_acres:.2f} acres')

# Write a program which calculates the various speeds which a car travels
distance_6 = 70 * 6
distance_10 = 70 * 10
distance_15 = 70 * 15
print(f'If traveling at 70mph for 6 hours, the distance traveled is {distance_6} miles')
print(f'If traveling at 70mp for 10 hours, the distance traveled is {distance_10} miles')
print(f'If traveling at 70mph for 15 hours, the distance traveled is {distance_15} miles')

# Write a program which calculates sales tax and total cost of their purchase
before_tax = int(float(input('Enter the amount of your purchase before tax: ')))
states_tax = before_tax * 0.025
county_tax = before_tax * 0.05
total_tax = states_tax + county_tax
total_cost = before_tax + total_tax
print(f'state tax is ${states_tax:.2f}')
print(f'county tax is ${county_tax:.2f}')
print(f'The total purchase with state and county tax included is ${total_cost:.2f}')

# Write a program which converts celsius to fahrenheit
celsius = int(float(input('Enter the temperature in celsius: ')))
fahrenheit = (celsius * 9 / 5) + 32
print(f'{celsius:.1f} degrees celsius is {fahrenheit:.1f} degrees fahrenheit')

# This a program which adjusts ingredients to how many cookies they want to make
# I realized that the values are scaled in terms of a ratio. This would mean you'd divide the amount you want by the predetermined recipe, and ratio the rest of the ingredients by that amount.
# ie. 24/28 is 1/2, so you'd scale the recipe by multiplying the ingredient to be a half of their original value. The same would apply to increasing the ingredients (if you have enough faith in python)
cookies_desired = int(float(input('Enter the amount of cookies you want to bake: ' )))
ratio = cookies_desired / 48 
ratioed_sugar = ratio * 1.5
ratioed_butter = ratio * 1
ratioed_flour = ratio * 2.75
print(f'if you want to make {cookies_desired} cookies, you will need: ')
print(f'{ratioed_sugar:.2f} cups of sugar, {ratioed_butter:.2f}, and {ratioed_flour:.2f} cups of flour.')

# Writes a program which asks a user for the number of males and number of females in their class.
# Display the percentage of males and females in the class
males = int(input('How many male students are in your class? '))
females = int(input('How many female students are in your class? '))
total_students = males + females 
male_percent = (males/total_students)*100
female_percent = (females/total_students)*100
print(f'out of {total_students}, {male_percent}% are male, and {female_percent}% are female.')

# Writes a program which compounds interest over a specific amount of time
#acquire all needed information from the user
starting_amount = int(float(input('How much money did you deposit into the account? ')))
annual_interest = int(float(input('What is the annual interest rate?  ')))
converted_interest = annual_interest/100 # converts the interest from a percentage to a decimal
times_compounded = int(float(input('How many months in a year is your interest compounded? ')))
number_of_years = int(float(input('How long will the account be left to accrue interest? (in years) ')))
amount_after_years = starting_amount*(1+(converted_interest/times_compounded)**(times_compounded*number_of_years))
print(f'After {number_of_years} years with an interest rate of {annual_interest:.2f}, you will have ${amount_after_years:.2f} in your account.')
