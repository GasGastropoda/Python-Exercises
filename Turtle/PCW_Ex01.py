# Python challenges: Say hello
# Exercise 1: Match the length of the text so that the underline matches what you wrote
import turtle
j = input("What would you like me to write? ") # assigns the user prompt to input text to variable

# bit values are smaller than pixels, so multiply by 5 to get the line to move by 5 per value
text_length = int(len(j)) * 5  # finds the length of the user input and multiplies by 5 to get a proper line length

turtle.write(j) # tells turtle to write whatever text input was assigned to variable
turtle.forward(text_length) # tells turtle to move to the length which matches user input
turtle.shape("turtle") # changes the turtle into a turtle shape
turtle.done() # Keeps the window open
