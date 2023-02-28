# Program 1: Day of the week 
# Write a program that asks the user for a number in the range of 1 through 7.
# The program should display the corresponding day of the week, where 1 = monday, 7 = sunday, etc
# program should display error message if the user enters a number outside the range

# ask the user for input
user_input = input("Enter the number you'd like to know it's corresponding day: ")

#check input against predetermined values 
# Prepares a dictionary which assigns all days their values
dict = {
    "null" : 0,
    "Monday" : 1,
    "Tuesday" : 2,
    "Wednesday" : 3,
    "Thursday" : 4,
    "Friday" : 5,
    "Saturday" : 6,
    "Sunday" : 7
}

if user_input in range(1,7): # checks to see if the user input falls within the desired range
    print('This number matches: ', list(dict.keys())[int(user_input)]) # prints the successful message if the key within the list matches the user input
else:
    print('This number is not in range!') # if the user input does not fall within the range, then print the other message


# Program 3: Age Classifier
# Write a program that asks the user to enter a person's age.
# Program displays whether the person is an infant, a child, a teenager, or an adult 
# !!!come back to this later!!!
user_input = input("Enter someone's age: ")

dict = {
    "infant" : [0, 1],
    "child" : [2,3,4,5,6,7,8,9,10,11,12],
    "teenager" : [13,14,15,16,17,18,19],
    "adult" : [20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100]

}
if user_input in range(1,100):
    print('That person is a(n): ', list(dict.keys())[int(user_input)])
else:
    print('This number is not in range!')

# Program 4: Roman Numerals
# write a program that prompts the user to enter a number within the range of 1-10
# The program should display the roman numeral version of that number.
# if the number is outside of the range, display an error message
# !!! come back to this later !!!
user_input = input('Enter the number you\'d like to see its numeral: ')
dict = {
    "null": 0,
    "I": 1,
    "II": 2,
    "III": 3,
    "IV": 4,
    "V": 5,
    "VI": 6,
    "VII": 7,
    "VIII": 8,
    "IX": 9,
    "X": 10
}
if int(user_input) > 0 and int(user_input) < 10:
    print('This number matches: ', list(dict.keys())[int(user_input)])
else:
    print('This number is not in range!')

# program 5: Mass and Weight
# write a program that asks the user to enter an object's mass, then calculate the weight.
# if the object weighs more than 500 newtons, print that its too heavy
# if the object weighs less than 100 newtons, print that its too light
# formula for weight is mass(9.8)
mass = int(input('Enter the object\'s mass: '))
weight = mass*9.8

if weight > 500:
    print('this object is too heavy!')
elif weight < 100:
    print('This object is too light!')
else:
    print('This value is not in range!')


