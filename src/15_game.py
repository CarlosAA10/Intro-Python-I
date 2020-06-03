#guessing game 

#what does it do? 
# we'll write a program that plays a guessing game with a user 
# Would be useful to have the program print out the rules at the beginning 
# How does the user communicate to the program that the program didn't guess the number right?
# we can have the user specify that the program's guess was too high, too low, or equal 
# After the program makes a guess, it will wait on user input form the command line
# Player types in "low", "high", or "equal"
# program reads in that input and acts on it
# if the player says the number is too low, then program knows it needs to guess higher 
# How does the program generate a guess? 


# what are the rules? 
# The user will think of a number, the program has to guess it
# Is there a range of possible numbers or can we allow any number? 
# Lets say the range is between 1 and 100

print("Think of a number between 1 and 100, and I'll guess it.")
print("You have to tell me if my guess is less than, greater than, or equal to your number")

# How does the game actually run? 
# Loop until the program exits
# When does the program exit? 
# Either when the user terminates it, or when the program has successfully guessed the player's number

#variables to store the floor and ceiling range
floor = 1
ceiling = 100
# boolean value to indicate whether the program has guessed the number or not 
got_it = False

#In the loop 
while not got_it:

    # Game generates a guess between 1 and 100
        # Should it guess a totally random number between this range?
        # should we have it guess a bit smarter
        # guess the halfway point between the range 
        # we'll have it guess halfway between 1 and 100
    # using a midpoint formula
    # in Python, '//' that's floor division (always rounds down)
    guess = (floor + ceiling) // 2

    #print out the guess to the user
    print(f"I'm guessing {guess}.")

    # wait for the user's input to tell the program if its guess was high , low , or equal
    result = input("Is my guess less, greater, or equal to your number?")

    # format the result for ease 
    # lowercase result
    result = result.lower()
    # let's just grab the first letter of the input
    result = result[0]

    #read in user's input 

    # act according to the user's input 

    # if input == "high"
    if result == 'h':
        # we need to guess lower for the next guess
        # narrow the range accordingly
        # set the "ceiling" of the range equal to guess -1
        ceiling = guess - 1
    
    #if input == "low"
    elif result == 'l':
        # we need to guess higher for the next guess
        # narrow the range accordingly
        # set the "floor" of the range to equal guess + 1
        floor = guess + 1

    #if input == "equal"
    elif result == 'e':
        # print " I guessed your number!"
        # quit the game loop
        got_it = True
        print("I guessed your number")

    # if result isn't any of the above, then print an error message

    else: 
        print("I don't know what that means, try again please. ")

    # Go on to the next loop iteration
    # our range has been updated according to the user's input 

