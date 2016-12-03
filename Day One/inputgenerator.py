# This program will output a list of instructions for other people to try.

from naive import Turtle
import random
f = open("custominput.txt", "w")

delimiter = ", "

directions = "RL"

number = 1000

output = ""

for i in range(number):
    if i != number - 1:
        output += random.choice(directions) + str(random.randrange(number)) + delimiter
    else:
        output += random.choice(directions) + str(random.randrange(number))

f.write(output)

f.close()

# Hello bob.
bob = Turtle()

# Load our instructions from "input.txt"
with open("custominput.txt", "r") as inputFile:
    instructions = inputFile.read()

# Split the instructions into a list.
instructions = instructions.split(", ")

# Okay, bob, time to go for a little walk.
bob.walkPath(instructions)

print "It will take " + str(abs(bob.x) + abs(bob.y)) + " steps totake the most efficient route."

print "First crossed our own path at position at " + str(bob.firstCrossedPoint) + ", which is " + str(abs(bob.firstCrossedPoint[0]) + abs(bob.firstCrossedPoint[1])) + " blocks away from the start."