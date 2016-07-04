# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import random
import math
import simplegui
# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number
    secret_number = 0
    global range_number
    range_number = 100
    range100()
    
    # remove this when you add your code    
    


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global secret_number
    secret_number = random.randrange(0, range_number)
    global count
    count = int(math.ceil(math.log(range_number - 0 + 1, 2)))
    print "New game. Range is from 0 to",range_number
    print "Nmuber of remaining guesses is", count
    print ""
    # remove this when you add your code    
    

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global range_number
    range_number = 1000
    global secret_number
    secret_number = random.randrange(0, range_number)
    global count
    count = int(math.ceil(math.log(range_number - 0 + 1, 2)))
    print "New game. Range is from 0 to",range_number
    print "Nmuber of remaining guesses is", count
    
def input_guess(guess):
    # main game logic goes here	
    guess_number = int(guess)
    print "Guess was", guess_number
    global count
    count -= 1
    print "Nmuber of remaining guesses is", count
    if count >= 0:
        if guess_number < secret_number:
            print "Higher"
        elif guess_number > secret_number:
            print "Lower"
        elif guess_number == secret_number:
            print "Correct"
            print ""
            new_game()
    else:
        print "You ran out of guesses. The number was", secret_number
        print ""
        new_game()
    print ""
    # remove this when you add your code
    

    
# create frame
frame = simplegui.create_frame("Guess the number",400,400)

# register event handlers for control elements and start frame
frame.add_button("Range is [0,100)",range100,200)
frame.add_button("Range is [0,1000)",range1000,200)
frame.add_input("Enter a guess: ", input_guess,200)


# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
