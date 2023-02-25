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





