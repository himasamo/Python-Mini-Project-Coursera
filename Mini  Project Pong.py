# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400
ball_pos = [WIDTH / 2, HEIGHT / 2]
#paddle2_pos = [0, 0]
ball_vel = [0,0]
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
random_range = [random.randrange(120, 240), random.randrange(80, 180)] 


#paddle var
paddle1_pos = HEIGHT / 2.5
paddle2_pos = HEIGHT / 2.5
paddle1_vel = 0
paddle2_vel = 0
paddle_vel = 5

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel, BALL_RADIUS, random_range  # these are vectors stored as lists
    
    ball_pos[1] <= BALL_RADIUS
    ball_pos[1] >= HEIGHT - BALL_RADIUS
    
    if direction == RIGHT:
        random_range[0] += ball_vel[0]
        random_range[1] += ball_vel[1]
        
    elif direction == LEFT:
        random_range[0] += ball_vel[0]
        random_range[1] += ball_vel[1]
        

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    #spawn_ball() # call spawn_ball function

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, BALL_RADIUS, HEIGHT, paddle1_vel, paddle2_vel

    spawn_ball(LEFT)
    spawn_ball(RIGHT)
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "white")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "white")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "white")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
   
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, 'white', 'white')
    
    # update paddle's vertical position, keep paddle on the screen
    if (paddle1_pos <= HEIGHT - PAD_HEIGHT and paddle1_vel > 0) or (paddle1_pos >= 0 and paddle1_vel < 0):
        paddle1_pos += paddle1_vel
    elif (paddle2_pos <= HEIGHT - PAD_HEIGHT and paddle2_vel > 0) or (paddle2_pos >= 0 and paddle2_vel < 0):
        paddle2_pos += paddle2_vel   
    
    # draw paddles
    canvas.draw_polygon([[0, paddle1_pos], [PAD_WIDTH, paddle1_pos],[PAD_WIDTH, (paddle1_pos) + PAD_HEIGHT ],[0, (paddle1_pos) + PAD_HEIGHT]],1, "green", "white")
    canvas.draw_polygon([[WIDTH, paddle2_pos], [WIDTH - PAD_WIDTH, paddle2_pos], [WIDTH - PAD_WIDTH, paddle2_pos + PAD_HEIGHT], [WIDTH, paddle2_pos + PAD_HEIGHT]],1, "green", "white")
    PAD_WIDTH
    # determine whether paddle and ball collide    
    
    # draw scores
        
def keydown(key):
    global paddle1_vel, paddle2_vel, paddle_vel
    
    #player one
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel = -paddle_vel
    elif key == simplegui.KEY_MAP['s']:
        paddle1_vel = paddle_vel
        
    #player two
    if key == simplegui.KEY_MAP['down']:
        paddle2_vel = paddle_vel
    elif key == simplegui.KEY_MAP['up']:
        paddle2_vel = -paddle_vel    
        
def keyup(key):
    global paddle1_vel, paddle2_vel, paddle_vel 
    #player one
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP['s']:
        paddle1_vel = 0
        
    #player two
    if key == simplegui.KEY_MAP['down']:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP['up']:
        paddle2_vel = 0     


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

# start frame
new_game()
frame.start()
