# Python challenges: Drunk Pirate
# http://pythonchallenges.weebly.com/turtle.html
# use turtle module to draw the path of a drunk pirate.
# A drunk pirate makes a random turn and then takes 100 steps forward, repeat

import turtle
import random # this library allows python to return an integer number from the specified range
for i in range(20): 
    turtle.left(random.randint(0, 30))
    turtle.forward(100)
    turtle.right(random.randint(0,30))
