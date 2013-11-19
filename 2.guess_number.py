# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import random
import simplegui

# initialize global variables used in your code

secret_num = 0
flag = 1
guesses = 0

# helper function to start and restart the game
def new_game():
    global flag, secret_num
    if flag == 1:
        secret_num = range100()
    elif flag == 2:
        secret_num = range1000()


# define event handlers for control panel
def range100():
    # button that changes range to range [0,100) and restarts
    global flag, guesses
    flag = 1
    guesses = 7
    print
    print 'New game. Range is from 0 to 100'
    print 'Number of remaining guesses is', guesses
    return random.randint(0, 100)

def range1000():
    # button that changes range to range [0,1000) and restarts
    global flag, guesses
    flag = 2
    guesses = 10
    print
    print 'New game. Range is from 0 to 1000'
    print 'Number of remaining guesses is', guesses
    return random.randint(0, 1000)
    
def input_guess(guess):
    # main game logic goes here
    global secret_num, guesses
    guess = int(guess)
    guesses-=1
    print
    print 'Guess was,', guess
    print 'Number of remaining guesses is,', guesses
    if (secret_num > guess):
        print 'Higher!'
    elif (secret_num < guess):
        print 'Lower!'
    elif (secret_num == guess):
        print 'Correct!'
    if (guesses == 0):
        print 'Out of guesses'
        new_game()
        

# create frame

frame = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements

frame.add_button('Range is [0, 100)', range100, 150)
frame.add_button('Range is [0, 1000)', range1000, 150)
frame.add_input('Enter a guess', input_guess, 150)

# call new_game and start frame
new_game()
frame.start()

# always remember to check your completed program against the grading rubric
