# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
playeroutcome = ""
score = 0

# define globals for cards clubs spades hearts diamonds 
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
        self.hand_cards = []	# create Hand object

    def __str__(self):
        string =  "Hand contains"	# return a string representation of a hand
        if not self.hand_cards == []: 
            for x in self.hand_cards:
                string = string + " " + str(x)
        return string
    def add_card(self, card):
        self.hand_cards.append(card)	# add a card object to a hand

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        total_value = 0
        has_A = False
        for x in self.hand_cards:
            if x.rank == "A":
                has_A = True
            total_value += VALUES[x.rank]
        if has_A:
            if total_value + 10 <= 21:
                total_value += 10
        return total_value
   
    def draw(self, canvas, pos):
    # draw a hand on the canvas, use the draw method for cards
        ori_pos0 = pos[0]
        for num in range(len(self.hand_cards)):
            pos[0] = ori_pos0 + (CARD_SIZE[0] + 30)*num
            #print pos[0]
            self.hand_cards[num].draw(canvas, pos)
            
# define deck class 
class Deck:
    def __init__(self):
        self.deck_cards = []	# create a Deck object
        for i in SUITS:
            for j in RANKS:
                self.deck_cards.append(Card(i, j))
    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.deck_cards)    # use random.shuffle()

    def deal_card(self):
        return self.deck_cards.pop()	# deal a card object from the deck
    
    def __str__(self):
        string =  "Deck contains"	
        if not self.deck_cards == []: 
            for x in self.deck_cards:
                string = string + " " + str(x)
        return string	# return a string representing the deck



#define event handlers for buttons
def deal():
    global outcome, playeroutcome, in_play, playerHand, dealerHand, deck, score
    if in_play:
        score -= 1
    
    playerHand = Hand()
    dealerHand = Hand()
    deck = Deck()
    deck.shuffle()
    playerHand.add_card(deck.deal_card())
    playerHand.add_card(deck.deal_card())
    dealerHand.add_card(deck.deal_card())
    dealerHand.add_card(deck.deal_card())
    #print dealerHand.hand_cards[0],dealerHand.hand_cards[1]
    #print playerHand.hand_cards[0],playerHand.hand_cards[1]
    outcome = ""
    playeroutcome = "Hit or Stand?"
    in_play = True

def hit():
    global playerHand, outcome, deck, score, in_play, playeroutcome
    if in_play:	# replace with your code below
        playerHand.add_card(deck.deal_card())
        print playerHand.get_value()
        if playerHand.get_value() <= 21:
            playeroutcome =  "Hit or Stand?"
        else:
            outcome =  "Player are BUSTED!Player lose!"
            playeroutcome =  "New deal?"
            in_play = False
            score -= 1
    
    
def stand():
    # replace with your code below
    global playerHand, dealerHand, outcome, deck, in_play, score
    if in_play:
        while dealerHand.get_value() < 17:
            dealerHand.add_card(deck.deal_card())
        if dealerHand.get_value() > 21:
            outcome = "Dealer are BUSTED!Player Win"
            playeroutcome =  "New deal?"
            score += 1
        elif playerHand.get_value() > dealerHand.get_value():
            outcome = "Player Win"
            playeroutcome =  "New deal?"
            score += 1
        else:
            outcome = "Dealer Win"
            playeroutcome =  "New deal?"
            score -= 1
        in_play = False
    
# draw handler    
def draw(canvas):
    global outcome, playeroutcome, score
    # test to make sure that card.draw works, replace with your code below
    canvas.draw_text("Blackjack", (100, 100), 36, "Aqua")
    canvas.draw_text("Score " + str(score), (400, 100), 30, "Black")
    canvas.draw_text("Dealer", (80, 200), 30, "Black")
    canvas.draw_text(outcome, (200, 200), 30, "Black")
    canvas.draw_text("Player", (80, 400), 30, "Black")
    canvas.draw_text(playeroutcome, (200, 400), 30, "Black")
    
    
        #(120, 280)
    dealerHand.draw(canvas, [80, 240])
    if in_play:
        canvas.draw_image(card_back, (CARD_BACK_CENTER[0]+CARD_BACK_SIZE[0], CARD_BACK_CENTER[1]), CARD_BACK_SIZE, (117, 287), CARD_BACK_SIZE)
    playerHand.draw(canvas, [80, 440])   
     
    
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