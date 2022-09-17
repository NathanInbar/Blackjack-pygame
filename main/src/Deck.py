from inspect import CORO_CLOSED
from random import randrange
from src.Card import Card

class Deck:

    suits = {"♠":(0,0,0),"♥":(230,20,40),"♣":(0,0,0),"♦":(230,20,40)}
    values = [2,3,4,5,6,7,8,9,10,"J","Q","K","A"]

    def __init__(self, coordinates):

        self.deck = [None]*52# card, isInDeck
        self.coordinates = coordinates

        self.generateDeck()

    def generateDeck(self):

        i = 0
        for suit,suit_color in self.suits.items():
            for value in self.values:
                self.deck[i] = [Card(suit=suit, suit_color=suit_color, value=value, coordinates= self.coordinates), True]
                i+=1


    def getRandomCard(self):
        i = randrange(0,len(self.deck))
        count = 1
        while not self.deck[i][1]: #selected card not in deck
            i = randrange(0,len(self.deck))
            count+=1
            if count == 52: #we have run out of cards in the deck
                return None

        self.deck[i][1] = False #card is getting removed from the deck
        return self.deck[i][0]

    def resetDeck(self):
        for i in range(len(self.deck)):
            self.deck[i][1] = True

    def render(self,win):

        for card,isInDeck in self.deck:
            card.render(win, isInDeck)
