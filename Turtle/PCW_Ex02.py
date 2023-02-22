# Python challenges: Turtle shapes
# http://pythonchallenges.weebly.com/shapes.html
import turtle

# Introduces how to use python loops
# i is a placeholder for an imaginary number. The loop will continue until a condition is statisfied
# adjust the code to create an 8 sided shape
# below is the original code
'''
for i in range (4):
    turtle.forward(50)
    turtle.right(90)
'''
for i in range(8): # repeat this 8 times to create the 8 sides
    turtle.forward(50)
    turtle.right(45) # 90 degrees would just make a square. half the degrees to allow a new shape
