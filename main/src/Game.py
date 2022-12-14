# from sre_parse import State
# from src.Deck import Deck
# from src.StateMachine import StateMachine


# # class BlackJack:

# #     def __init__(self, deck, walletStart=1000, betStart=100):

# #         self.wallet = walletStart
# #         self.bet_amount = betStart
# #         self.deck = deck

# #         self.playerHand = 0
# #         self.dealerHand = 0

# #     def play(self):
# #         while True:
# #             print(f"Your wallet: ${self.wallet}")

# #             bet_amount = self.validateInput("Bet Amount:\n",int)
            
# #             while bet_amount > self.wallet:
# #                 print("bet amount too high.")
# #                 bet_amount = self.validateInput("Bet Amount:\n",int)

# #             self.wallet -= bet_amount

# #             result = self.playRound()
# #             if result[0]:
# #                 self.wallet += bet_amount*2
# #                 print(f"{result[1]} +${bet_amount*2}")
# #             else:
# #                 print(f"{result[1]} -${bet_amount}")

# #             _input = self.validateInput("play again? (y/n)\n",str,"y","yes","n","no")
# #             if _input == "n" or _input == "no":
# #                 return

# #             self.deck.resetDeck()
# #             self.playerHand = 0
# #             self.dealerHand = 0

# #     def playRound(self):
# #         ''' returns True/False according to player win, with a message'''

# #         #deal 1 card to player
# #         #deal 1 to dealer
# #         #deal 1 to player
# #         self.dealCard_Player()
# #         self.dealCard_Dealer()
# #         self.dealCard_Player()

# #         #player hits until bust or stands
# #         while True:
# #             _input = self.validateInput("Hit or Stand?\n", str, "hit","stand")

# #             if _input == "hit":
# #                 self.dealCard_Player()
# #                 win = self.checkHand(self.playerHand)
# #                 if win is not None:
# #                     if win:
# #                         return (True, "You have blackjack")
# #                     else:
# #                         return (False, "Bust!")

# #             elif _input == "stand":
# #                 break

# #         #dealer hits until 17 or bust
# #         while self.dealerHand < 17:
# #             print("Dealer Hits.")
# #             self.dealCard_Dealer()
# #             win = self.checkHand(self.dealerHand)
# #             if win is not None:
# #                 if win:
# #                     return (False,"Dealer has blackjack.")
# #                 else:
# #                     return (True, "Dealer Bust!")

# #         print("Dealer Stands.")

# #         #compare hands, round winner decided
# #         win = self.compareHands(self.playerHand,self.dealerHand)
# #         if win:
# #             return (True,"You win. ")
# #         else:
# #             return (False,"Dealer wins. ")

# #     def dealCard(self):

# #         card = self.deck.getRandomCard()
# #         print("")
# #         print(card,end="", flush=True)

# #         return card

# #     def dealCard_Dealer(self):
# #         card = self.dealCard()
# #         self.dealerHand += card.getValue(self.dealerHand)
# #         print(f"Dealer hand: {self.dealerHand}")

# #     def dealCard_Player(self):
# #         card=self.dealCard()
# #         self.playerHand += card.getValue(self.playerHand)
# #         print(f"Your hand: {self.playerHand}")

# #     def checkHand(self,hand):
# #         '''
# #         returns True if hand has blackjack, False if hand is a bust, None otherwise
# #         '''
        
# #         if hand < 21:
# #             return None
# #         if hand > 21:
# #             return False
# #         if hand == 21:
# #             return True

# #     def compareHands(self, hand1, hand2):
# #         if hand1 >= hand2:
# #             return True
# #         return False
            
# #     def validateInput(self, message, _type, *argv):
# #         while True:
# #             _input = input(message)
# #             try:
# #                 _input = _type(_input)
# #             except ValueError:
# #                 print("invalid input, try again.\n")
# #                 continue

# #             if type(_input) is str:
# #                 _input = _input.lower().strip()

# #             if len(argv) == 0:
# #                 return _input

# #             for arg in argv:
# #                 if _input == arg:
# #                     return _input
            
# #             print("invalid input, try again.\n")

# class BlackJack:

#     def __init__(self, deck:Deck, animator, playerSlot, dealerSlot, walletStart=1000, betStart=100):

#         self.wallet = walletStart
#         self.bet_amount = betStart

#         self.deck = deck

#         self.playerHand = 0
#         self.dealerHand = 0

#         self.player_slot = playerSlot
#         self.dealer_slot = dealerSlot
#         self.animator = animator
#         self.state_machine = StateMachine()

#         self.playerDeal()
#         #self.dealerDeal()
#         #self.playerDeal()

#     def dealCard(self, hand, destination, speed=0.5):
#         card = self.deck.pop()
#         self.animator.lerp(card, destination, speed)
#         return card.getValue(hand)

#     def playerDeal(self):
#         self.playerHand += self.dealCard(self.playerHand,(self.player_slot[0]+5, self.player_slot[1]+5))
#         self.player_slot = (self.player_slot[0]- 110, self.player_slot[1])

#     def dealerDeal(self):
#         self.dealerHand += self.dealCard(self.dealerHand,(self.dealer_slot[0]+5, self.dealer_slot[1]+5))
#         self.dealer_slot = (self.dealer_slot[0]- 110, self.dealer_slot[1])

#     def playRound(self):
#         pass

#     def update(self):
#         self.state_machine.update()