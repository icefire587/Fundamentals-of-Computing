# template for "Stopwatch: The Game"
import simplegui
# define global variables
score = 0
counter = 0
total_ticks = 0
# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    minutes = int(t // 600)
    B = int(t / 100) % 6
    C = int(t / 10) % 10
    last = t % 10
    return str(minutes) + ":" + str(B) + str(C)+ "." + str(last)
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()
   
def stop():
    timer.stop()
    global counter
    counter += 1
    if total_ticks % 10 == 0:
        global score
        score += 1
    
def reset():
    timer.stop()
    global total_ticks, counter, score
    total_ticks = 0
    counter = 0
    score = 0
# define event handler for timer with 0.1 sec interval
def tick():
    global total_ticks
    total_ticks += 1

# define draw handler
def draw_handler(canvas):
    canvas.draw_text(format(total_ticks), [100, 100], 48,"white")
    canvas.draw_text(str(score) + "/" +str(counter), [240, 40], 36,"green")
# create frame
frame = simplegui.create_frame("Stopwatch", 300, 200)
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)
# register event handlers
frame.set_draw_handler(draw_handler)
timer = simplegui.create_timer(100, tick)
# start frame
frame.start()

# Please remember to review the grading rubric
