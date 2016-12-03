#Day Two: Bathroom Security

##Part One
`You arrive at Easter Bunny Headquarters under cover of darkness. However, you left in such a rush that you forgot to use the bathroom! Fancy office buildings like this one usually have keypad locks on their bathrooms, so you search the front desk for the code.`

`"In order to improve security," the document you find says, "bathroom codes will no longer be written down. Instead, please memorize and follow the procedure below to access the bathrooms."`

`The document goes on to explain that each button to be pressed can be found by starting on the previous button and moving to adjacent buttons on the keypad: U moves up, D moves down, L moves left, and R moves right. Each line of instructions corresponds to one button, starting at the previous button (or, for the first line, the "5" button); press whatever button you're on at the end of each line. If a move doesn't lead to a button, ignore it.`

`You can't hold it much longer, so you decide to figure out the code as you walk to the bathroom. You picture a keypad like this:`

    1 2 3
    4 5 6
    7 8 9

`Suppose your instructions are:`

    ULL
    RRDDD
    LURDL
    UUUUD

`You start at "5" and move up (to "2"), left (to "1"), and left (you can't, and stay on "1"), so the first button is 1.`
`Starting from the previous button ("1"), you move right twice (to "3") and then down three times (stopping at "9" after two moves and ignoring the third), ending up with 9.`
`Continuing from "9", you move left, up, right, down, and left, ending with 8.`
`Finally, you move up four times (stopping at "2"), then down once, ending with 5.`
`So, in this example, the bathroom code is 1985.`

`Your puzzle input is the instructions from the document you found at the front desk. What is the bathroom code?`

###Attempts
* [Overkill](Pointed)
    * Using Visual Studio, C++, and pointers to create a simple solution to the problem.

    The keypad will be stored in a simple, one-dimensional array. Yep. You heard me. To figure out where we need to move, there will be a lookup table (surprise surprise!) for each of the directions that your finger could have to move. The finger will simply look up the direction it needs to move, and then apply that change to its position in the array. A direction of **U**p maps to `-3`, **D**own maps to `3`, **L**eft maps to `-1`, and **R**ight maps to `1`. If the finger movesout of the array, it will go to a special pointer, which points to the previous position.

    So, in memory, everything is represented like so:

        buttons            {1, 2, 3, 4, 5, 6, 7, 8, 9}
        currentButton          ^
        lastButton             ^

    Current button simply stores the address of where the finger (The pointer, get it?) is, and last button stores where the finger _was_ before it started moving. If we try to go up from the address of `2`, the currentButton will have `-3` added to it, and will become `-1`. We will check for this when we are done moving, and simply move it back to the `lastButton` address. Once we are done moving, we will update `lastButton`.

    At the end of a line, we will save the number of that corresponds to the address stored in `lastButton`. Rinse, repeat. 
