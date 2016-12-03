#Day One: No Time for a Taxicab

##Part One
`Santa's sleigh uses a very high-precision clock to guide its movements, and the clock's oscillator is regulated by stars. Unfortunately, the stars have been stolen... by the Easter Bunny. To save Christmas, Santa needs you to retrieve all fifty stars by December 25th.`

`Collect stars by solving puzzles. Two puzzles will be made available on each day in the advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!`

`You're airdropped near Easter Bunny Headquarters in a city somewhere. "Near", unfortunately, is as close as you can get - the instructions on the Easter Bunny Recruiting Document the Elves intercepted start here, and nobody had time to work them out further.`

`The Document indicates that you should start at the given coordinates (where you just landed) and face North. Then, follow the provided sequence: either turn left (L) or right (R) 90 degrees, then walk forward the given number of blocks, ending at a new intersection.`

`There's no time to follow such ridiculous instructions on foot, though, so you take a moment and work out the destination. Given that you can only walk on the street grid of the city, how far is the shortest path to the destination?`

`For example:`

`Following R2, L3 leaves you 2 blocks East and 3 blocks North, or 5 blocks away.`
`R2, R2, R2 leaves you 2 blocks due South of your starting position, which is 2 blocks away.`
`R5, L5, R5, R3 leaves you 12 blocks away.`
`How many blocks away is Easter Bunny HQ?`

###Attempts
* [Naive approach](naive.py) [Python]
    * Uses a simple parsing function to parse the inputs, then traverses a grid and figures out where the end point is. Then it adds the absolute values of the cartesian cooridinates up to provide a minimum number of steps.

    In order to keep track of which direction our [turtle](https://en.wikipedia.org/wiki/Turtle_(robot)) is facing, we will have a list containing all of the directions, **N**orth, **E**ast, **S**outh, **W**est. For each instruction, we will increment the direction one index for every `R` command, which will turn our turtle clockwise, and decrement one index for each `L` command, which will turn our turtle counter-clockwise. 
    
    Then the turtle will walk along the cartesian plane the specified number of steps. It will do this by looking up the direction in a dictionary, which will be mapped to a differential corresponding to the `x` and `y` values of the turtle. For instance, if the turtle is facing **W**est, it will look up `W` in the dictionary, and see that it needs to add `-1` to its `x` cooridnate and `0` to its `y` coordinate.

    This will allow us to also move diagonally if we need to add that in the future.
    
    So, if the turtle is facing **N**orth, the command `L4` will decrement the index in our list of directions, making it face **W**est, and then find that it needs to add `-1` to its `x` coordinate and `0` to its `y` coordinate `4` times.

    The instruction parsing method will simply take the first character of an instruction, and split that from the remaining characters. Then, the remaining characters will be converted into an integer. If it can't, the instruction will be thrown out.

    Incidentally, there is not a single `if` statement in the main body of this code. I'm not sure if that's a good thing or a bad one, but I thought  it was interesting that I thought that way.

##Part Two
`Then, you notice the instructions continue on the back of the Recruiting Document. Easter Bunny HQ is actually at the first location you visit twice.`

`For example, if your instructions are R8, R4, R4, R8, the first location you visit twice is 4 blocks away, due East.`

`How many blocks away is the first location you visit twice?`

###Attempts
* [Naive approach](naive.py) [Python]
    * Uses the same program as before. I'm just adding a dictionary that counts the number of times you visit a particular spot.