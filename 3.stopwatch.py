# template for "Stopwatch: The Game"
import simplegui
# define global variables
message = "0:00.0"
message2 = "0/0"
time = 0
timer_on = False
y = 0
x = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global message
    minutes = t / 600
    t = t % 600
    seconds = t / 10
    t = t % 10
    message = str(minutes) + ":" + str(seconds) + "." + str(t)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global timer_on
    timer_on = True
    timer.start()
    
def stop():
    global timer_on
    score(time)
    timer_on = False
    timer.stop()
    
def reset():
    global time, message, message2, x, y
    message = "0:00.0"
    message2 = "0/0"
    x = 0
    y = 0
    time = 0

# keep track of scores    
def score(t):
    global message2, y, x
    if timer_on == True:
        y+=1
        if (t % 5) == 0:
            x+=1
    message2 = str(x) + "/" + str(y)

# define event handler for timer with 0.1 sec interval
def time_handler():
    global time
    time += 1

# define draw handler
def draw(canvas):
    format(time)
    canvas.draw_text(message, [70, 110], 36, "white")
    canvas.draw_text(message2, [150, 25], 24, "green")
    
# create frame
frame = simplegui.create_frame('Stopwatch: The Game', 200, 200)

# register event handlers
frame.add_button('Start', start, 50)
frame.add_button('Stop', stop, 50)
frame.add_button('Reset', reset, 50)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(100, time_handler)

# start frame
frame.start()

# Please remember to review the grading rubric

