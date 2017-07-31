# implementation of card game - Memory

import simplegui
import random

click = 0
click2 = 0
# helper function to initialize globals
def new_game():
    global state, exposed, card_deck, click, turn, label
    state = 0
    turn = 0
    exposed = [False for i in range(16)]
    card_deck = [i%8 for i in range(16)]
    random.shuffle(card_deck)
    label.set_text('Turns =' + str(turn))
    
    pass
     
# define event handlers
def mouseclick(pos):
    global state, exposed, click, click2, card_deck, turn
    #exposed = pos
    position =  int(pos[0] / 50)
    
    if state == 0:
        state = 1
        click = position
        exposed[click] = True   
    elif state == 1:
        if not exposed[position]:
            state = 2
            click2 = position
            exposed[click2] = True
            turn += 1 
    elif state == 2:
        if not exposed[position]:
            if card_deck[click] == card_deck[click2]:
                pass
            else: 
                exposed[click] = False
                exposed[click2] = False
            state = 1
            click = position
            exposed[click] = True 
    label.set_text('Turns =' + str(turn))

    
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    for i in range(16):
        if exposed[i]:
            canvas.draw_text(str(card_deck[i]), [50*i+10, 60] , 40, "white")
        else:
            canvas.draw_polygon([(50*i,0), (50*i+50, 0), (50*i+50, 0), (50*i+50,50*100)], 1, "white", "green")

    


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric

