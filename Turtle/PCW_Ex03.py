# Python challenges: Any shape
# use turtle so that when you ener a number it creates a polygon with that many sides

import turtle
# prompts a user to input how many sides their shape has.
# converts the string input into an integer
# assigns that value to the "sides" variable.
sides = int(input("How many sides does your shape have?: "))

for i in range(sides): # repeat this loop for the amount of sides determined by user
    turtle.forward(50) # move the turtle by 50px
    turtle.right(360/sides) # all shapes add up to 360 degrees. so divide 360 by desired sides to find at what angle the turtle needs to turn.
