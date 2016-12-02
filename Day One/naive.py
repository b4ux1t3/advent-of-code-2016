# This is a naive approach at figuring out how far away the end point is.
# It will take the starting point (0, 0), and then parse the input given in
# input.txt to find the location of Easter Bunny HQ, then will just simply
# return the sum of the X and Y coordinates, giving us the shortest path to
# the destination.

# We need a turtle. We'll store it in a class, which will have three 
# member variables: x coordinate, y coordinate, direction. That's all we 
# need to figure out where we are and where we are going.
# We'll also store some class variables here. All turtles have a sense of 
# direction, and an idea for how to move in those directions. So, we'll 
# give them a string that lists the directions in order, and we'll give 
# them a dictionary that maps velocities to directions.
class Turtle:

    # List of our directions
    directions = "NESW"

    # Dictionary storing our directional "velocities"
    velocities = {"N": [0, 1], "E": [1, 0], "S": [0, -1], "W": [-1, 0]}

    # Dictionary of rotational movement
    rotation = {"R": 1, "L": -1}

    # All turtles will start off at position (0, 0) and facing North.
    def __init__(self):
        self.x = 0
        self.y = 0
        self.direction = "N"
    
    # The turtle needs a way to figure out whereit is going.
    # This method takes in an instruction as a string, returns a tuple with 
    # the direction and amplitude of the instruction
    # To do this, the turtle first pulls out the first character, then 
    # tries to convert the remaining characters to an integer. If it can't 
    # get an integer, it will set the amplitude to 0, meaning the 
    # instruction will not be executed by the walkPath method
    def parseInstruction(self, instruction):
        rotation = instruction[0]

        try:
            amplitude = int(instruction[1:])

        except ValueError:
            amplitude = 0

        completedInstruction = (rotation, amplitude)

        return completedInstruction

    # The turtle takes a direction, then looks up which way he should change his direction to.
    def turn(self, whichWay):
        # Set currentDirection equal to the index of that direction in the 
        # directions list
        currentDirection = self.directions.index(self.direction)
        print "Turning " + whichWay
        # Look up whichWay (which should be either "R" or "L") in the 
        # rotation dictionary, and then add the result to the current index,
        # giving the new direction
        # TODO: Catch the exception if the key doesn't exist
        self.direction = self.directions[(currentDirection + self.rotation[whichWay]) % len(self.directions)]
        print "Facing " + self.direction



    # The turtle takes the number of steps he needs in a the direction he's 
    # facing, and uses the velocities dictionary to tell him which 
    # positions he should change
    def step(self):
        self.x += self.velocities[self.direction][0]
        self.y += self.velocities[self.direction][1]

    # Now the turtle has to walk the path described in the instructions. Th 
    # turtle will go through each instruction in the list he is given, 
    # parse them using his parseInstruction method, and then execute that 
    # instruction by adding the velocity described by the instruction to 
    # his position
    def walkPath(self, instructions):
        # Each instruction is in the format (rotation, steps), where rotation is a single character and steps is an integer.
        for instruction in instructions:
            # Parse the instruction, turn, and then take n steps
            nextInstruction = self.parseInstruction(instruction)
            self.turn(nextInstruction[0])
            print "Taking " + str(nextInstruction[1]) + " steps"
            for steps in range(nextInstruction[1]):
                self.step()
            print "Now at (" + str(self.x) + ", " + str(self.y) + ")"

if __name__ == "__main__":
    # Hello bob.
    bob = Turtle()

    # Load our instructions from "input.txt"
    with open("input.txt", "r") as inputFile:
        instructions = inputFile.read()

    # Split the instructions into a list.
    instructions = instructions.split(", ")

    bob.walkPath(instructions)

    print "It will take " + str(abs(bob.x) + abs(bob.y)) + " steps totake the most efficient route."
