# implementation of card game - Memory

import simplegui
import random

list = range(0,8)
list.extend(range(0,8))
exposed = []
state = 0
counter = 0
# helper function to initialize globals
def new_game():
    global exposed, counter
    exposed = []
    counter = 0
    state = 0
    random.shuffle(list)  
    for i in range(len(list)):
        exposed.append(False)
    
# define event handlers
def mouseclick(pos):
    # add game state logic here
    vert = pos[0]
    card_pos = vert // 50 + 1
    #print "card position:", card_pos
#    if not exposed[card_pos-1]:
#        exposed[card_pos-1] = True
#        print exposed[card_pos-1]  
    global state, first_pos, second_pos, counter
    if state == 0:
        if not exposed[card_pos-1]:
            exposed[card_pos-1] = True
            first_pos = card_pos - 1
            #print first_pos
            state = 1
    elif state == 1:
        
        if not exposed[card_pos-1]:
            exposed[card_pos-1] = True
            second_pos = card_pos - 1  
            #print second_pos
            state = 2
            counter += 1
    else:
        
        #print "this time number", list[card_pos-1]
        #print "first number", list[first_pos]
        #print "second number", list[second_pos]
        if not exposed[card_pos-1]:
            exposed[card_pos-1] = True
            if list[first_pos] != list[second_pos]:
                exposed[first_pos] = False
                exposed[second_pos] = False
            state = 1
            first_pos = card_pos - 1
            second_pos = -1
        
        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    for i in range(len(list)):
        canvas.draw_text(str(list[i]),[(18+50*i), 58], 30, 'WHITE')
        
        if not exposed[i]:
            canvas.draw_line((25+50*i, 0), (25+50*i, 100), 50, 'Green')
        
        
        canvas.draw_line((50+50*i, 0), (50+50*i, 100), 1, 'Black')
    
    label.set_text("Turns = " + str(counter))

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