# Mini-project #6 - Blackjack
# Created by sianios

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0

dist = 30

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        # create Hand object
        self.cards = []

    def __str__(self):
        # return a string representation of a hand
        result = ""
        for i in range(len(self.cards)):
            result += self.cards[i].suit + self.cards[i].rank + " "
        return result

    def add_card(self, card):
        # add a card object to a hand
        self.cards.append(card)

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        ace = False
        hand_sum = 0
        for i in range(len(self.cards)):
            hand_sum += VALUES[self.cards[i].rank]
            if self.cards[i].rank == 'A':
                ace = True
        if ace and hand_sum + 10 <= 21:
            hand_sum += 10
        return hand_sum
   
    def draw(self, canvas, pos):
        # draw a hand on the canvas, use the draw method for cards
        for i in range(1, len(self.cards)):
            self.cards[i].draw(canvas, [pos[0] + CARD_CENTER[0] + i * (dist + CARD_SIZE[0]), pos[1] + CARD_CENTER[1]])
 
        
# define deck class 
class Deck:
    def __init__(self):
        # create a Deck object
        self.deck = []
        for i in range(len(SUITS)):
            for j in range(len(RANKS)):
                self.deck.append(Card(SUITS[i], RANKS[j]))

    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.deck)

    def deal_card(self):
        # deal a card object from the deck
        card_deal = self.deck.pop(0)
        return card_deal
    
    def __str__(self):
        # return a string representing the deck
        results = ""
        for i in range(len(self.deck)):
            results += self.deck[i].suit + self.deck[i].rank + " "
        return results


#define event handlers for buttons
def deal():
    global outcome, in_play, player, dealer, deck, score
    outcome = ""
    
    if in_play:
        outcome = "You lost the round!"
        score -= 1
        
    in_play = True
    
    # your code goes here
    deck = Deck()
    deck.shuffle()
    #outcome = ""
    
    player = Hand()
    player.add_card(deck.deal_card())
    player.add_card(deck.deal_card())
    
    dealer = Hand()
    dealer.add_card(deck.deal_card())
    dealer.add_card(deck.deal_card())
    #

def hit():
    # if the hand is in play, hit the player
   
    # if busted, assign a message to outcome, update in_play and score
    global outcome, in_play, score
    
    if player.get_value() <= 21:
        player.add_card(deck.deal_card())
    elif player.get_value() > 21:
        outcome = "You have busted!"
        in_play = False
        score -= 1
       
def stand():
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score
    global outcome, score, in_play
    
    if not in_play:
        outcome = "You lost the round!"
    else:
        while dealer.get_value() < 17:
            dealer.add_card(deck.deal_card())
            
        if dealer.get_value() > 21:
            outcome = "Dealer is busted!"
            score += 1
        else:
            if player.get_value() > dealer.get_value():
                outcome = "Player wins!"
                score += 1
            else:
                outcome = "Dealer wins!"
                score -= 1
    in_play = False

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    #messages
    canvas.draw_text("Blackjack", (230, 40), 40, "black")
    canvas.draw_text("Score " + str(score), (260, 80), 30, "black")
    canvas.draw_text("Dealer", (50, 120), 25, "black")
    canvas.draw_text(outcome, (260, 120), 25, "black")
    canvas.draw_text("Player", (50, 340), 25, "black")

    #hide image
    if in_play:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [CARD_BACK_SIZE[0], 120 + CARD_BACK_SIZE[1]], CARD_SIZE)
    else:
        dealer.cards[0].draw(canvas, [CARD_CENTER[0], 120 + CARD_CENTER[1]])
    
    #dealer cards
    dealer.draw(canvas, [0, 118])
    
    #texts
    if in_play:
        canvas.draw_text("Hit or stand?", (260, 340), 25, "black")
    else:
        canvas.draw_text("New Deal?", (260, 340), 25, "black")
    
    #player cards
    player.cards[0].draw(canvas, [CARD_CENTER[0], 370 + CARD_CENTER[1]])
    player.draw(canvas, [0, 370])


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric
