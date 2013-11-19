# implementation of card game - Memory

import simplegui
import random

img0 = simplegui.load_image("https://fbcdn-sphotos-a-a.akamaihd.net/hphotos-ak-ash3/1457521_10152110650414059_218016184_n.jpg")
img1 = simplegui.load_image("https://fbcdn-sphotos-g-a.akamaihd.net/hphotos-ak-prn2/1457489_10152110650424059_552213507_n.jpg")
img2 = simplegui.load_image("https://fbcdn-sphotos-h-a.akamaihd.net/hphotos-ak-ash3/558943_10152110650439059_1963009224_n.jpg")
img3 = simplegui.load_image("https://fbcdn-sphotos-b-a.akamaihd.net/hphotos-ak-ash3/1454972_10152110650574059_933840497_n.jpg")
img4 = simplegui.load_image("https://fbcdn-sphotos-c-a.akamaihd.net/hphotos-ak-frc1/995565_10152110650589059_743068735_n.jpg")
img5 = simplegui.load_image("https://fbcdn-sphotos-e-a.akamaihd.net/hphotos-ak-prn2/1425797_10152110650619059_2062623829_n.jpg")
img6 = simplegui.load_image("https://fbcdn-sphotos-g-a.akamaihd.net/hphotos-ak-ash3/1450983_10152110650659059_1222146311_n.jpg")
img7 = simplegui.load_image("https://fbcdn-sphotos-a-a.akamaihd.net/hphotos-ak-prn2/1452082_10152110650669059_685885479_n.jpg")

list1 = [img0, img1, img2, img3, img4, img5, img6, img7]
list2 = [img0, img1, img2, img3, img4, img5, img6, img7]
list1.extend(list2)
exposed = [False] * 16
cards = {0:50, 1:100, 2:150, 3:200, 4:250, 5:300, 6:350, 7:400, 8:450, 9:500, 10:550, 11:600, 12:650, 13:700, 14:750, 15:800}
turn = 0
card1 = None
card2 = None
counter = 0

# helper function to initialize globals
def new_game():
    global exposed, turns, counter
    random.shuffle(list1)
    exposed = [False] * 16
    turns = 0
    card1 = None
    card2 = None
    counter = 0
    label.set_text("Turns = 0")

# define event handlers
def mouseclick(pos):
    # add game state logic here
    global turn, card1, card2, counter
    num = pos[0]
    for i in range(16):
        if num>cards.get(i)-50 and num<cards.get(i):
            if exposed[i] == False:
                counter+=1
                exposed[i] = True
                if turn == 0:
                    turn = 1
                    card1 = i
                elif turn == 1:
                    turn = 2
                    card2 = i
                else:
                    turn = 1
                    if list1[card1] != list1[card2]:
                        exposed[card1] = False
                        exposed[card2] = False
                        card2 = None
                    card1 = i
    mes="Turns = "+str(counter)
    label.set_text(mes)
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    canvas.draw_image(img1, (50/2, 100/2), (50, 100), (25, 50), (50,100))
    x = 25
    for i in range(16):
        element = list1[i]
        canvas.draw_image(list1[i], (50/2, 100/2), (50, 100), (x, 50), (50,100))
        x+=50
        
    x = 0
    for i in range(25, 800, 50):
        if exposed[x] == False:
            canvas.draw_line((i, 0), (i, 100), 50, "Green")
        x+=1
        
    for i in range(0, 800, 50):    
        canvas.draw_line((i, 0), (i, 100), 1, "white")
        

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric
