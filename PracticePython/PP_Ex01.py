# Exercise 01 - CHARACTER INPUT | https://www.practicepython.org/exercise/2014/01/29/01-character-input.html
# write a program which asks a user for their name and age.
# print a message telling the user the year which they turn 100 years old 

# asks user to input name and age. Prints the result of both inputs
name = input("What's your name? ")
age = input("What's your age? ")
print("Your name is " + name + " and you're " + age + " Years old")

#Variable converting string into integer
int_age= int(age)
# subtract integers, then convert result into string
until_100 = str(100 - int_age)

# adding the result with the other strings
# Printing calculation to tell user how many years until 100
print("You will be 100 in " + until_100 + " years!")

