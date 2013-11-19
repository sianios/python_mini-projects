# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

ball_pos = [0, 0]
ball_vel = [0, 0]

paddle1_pos = 100
paddle1_vel = 0

paddle2_pos = 100
paddle2_vel = 0
times = 2

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball():#(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH/2, HEIGHT/2]
    ball_vel[0] = -2
    ball_vel[1] = -1


# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    score1 = 0
    score2 = 0
    paddle1_pos = 100
    paddle2_pos = 100
    paddle1_vel = 0
    paddle2_vel = 0
    spawn_ball()

def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, times
 
        
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[1] += ball_vel[1]
    ball_pos[0] += ball_vel[0]
    
    #pano
    if ball_pos[1]-BALL_RADIUS == 0:
        ball_vel[1] -= ball_vel[1] * times
    #kato
    elif ball_pos[1]+BALL_RADIUS == HEIGHT:
        ball_vel[1] -= ball_vel[1] * times
    #aristera
    elif ball_pos[0]-BALL_RADIUS == PAD_WIDTH:
        if (paddle1_pos <= ball_pos[1]) and (paddle1_pos+PAD_HEIGHT >= ball_pos[1]):
            ball_vel[0] -= ball_vel[0] * times
        else:
            score2+=1
            spawn_ball()
    #deksia
    elif ball_pos[0]+BALL_RADIUS == WIDTH-PAD_WIDTH:
        if (paddle2_pos <= ball_pos[1]) and (paddle2_pos+PAD_HEIGHT >= ball_pos[1]):
            ball_vel[0] -= ball_vel[0] * times
        else:
            score1+=1
            spawn_ball()
    
    # draw ball
    c.draw_circle(ball_pos, BALL_RADIUS, 1, "white", "white")
    
    # update paddle's vertical position, keep paddle on the screen
    
    if (paddle1_pos < 0):
        paddle1_pos = 0
    elif (paddle1_pos+PAD_HEIGHT > 400):
        paddle1_pos = 320
        
    if (paddle2_pos < 0):
        paddle2_pos = 0
    elif (paddle2_pos+PAD_HEIGHT > 400):
        paddle2_pos = 320
        
    paddle1_pos += paddle1_vel        
    paddle2_pos += paddle2_vel
    
    # draw paddles
    c.draw_line([1, paddle1_pos], [1, paddle1_pos+PAD_HEIGHT], PAD_WIDTH, "red")
    c.draw_line([WIDTH-1, paddle2_pos], [WIDTH-1, paddle2_pos+PAD_HEIGHT], PAD_WIDTH, "red")
    
    # draw scores
    c.draw_text(str(score1), [150, 100], 50, "blue")
    c.draw_text(str(score2), [450, 100], 50, "blue")
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel += 5
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel -= 5
        
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel += 5
    elif key == simplegui.KEY_MAP["w"]:
        paddle1_vel -= 5
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel -= 5
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel += 5
        
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel -= 5
    elif key == simplegui.KEY_MAP["w"]:
        paddle1_vel += 5


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", new_game, 100)
#frame.add_button("respawn", spawn_ball, 100)


# start frame
new_game()
frame.start()
