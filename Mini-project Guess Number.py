# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import random
import math
import simplegui

num_range = 100
secret_number = 0
count = 0

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number
    global num_range
    secret_number = random.randrange(0, num_range)
    count = math.ceil(math.log(2))
    
    print "New game!. Range if from 0 to 100"
    print "Number of remaing guesses is 7"
    return secret_number
     

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    new_game()
    num_range = 100
    print "This game in range (0, 100)"
      
def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    new_game()
    num_range = 1000
    print "This game in range (0, 1000)"
    
def input_guess(guess):
    # main game logic goes here	
    #new_game()
    num = int(guess)
    print "Guess was", guess
    
    if num == secret_number:
        #print "Number of remaining guesses is"
        print "Correct"
    elif num > secret_number:
        #print "Number of remaining guesses is"
        print "Higher"
    elif num < secret_number:
        #print "Number of remaining guesses is"
        print "Lower"
    elif not num == secret_number:
        print "Out of guesses"
    print ""    

    
# create frame
f = simplegui.create_frame("Guess Number Template", 200, 200)
f.add_button("Range is [0,100)", range100 ,200)
f.add_button("Range is [0,1000)", range1000 ,200)
f.add_input("Guess Number", input_guess ,200)


# register event handlers for control elements and start frame
f.start()

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
