from random import randrange
from Card import Card

class Deck:

    suites = ["♤","♥","♧","♢"]
    values = [2,3,4,5,6,7,8,9,10,"J","Q","K","A"]

    def __init__(self):

        # card, isInDeck
        self.deck = [None]*52

        self.generateDeck()

    def generateDeck(self):

        i = 0
        for suite in self.suites:
            for value in self.values:
                self.deck[i] = [Card(suite=suite, value=value), True]
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