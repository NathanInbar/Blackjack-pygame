import pygame

from src.Animation import Animator
from src.util import TextComponent
from src.util import Header, Log, Button
from src.Deck import Deck
from src.CardSlot import CardSlot
from src.EventSystem import Event, EventSystem
#from src.Game import BlackJack

class App:
    pygame.init()

    WIDTH = 600
    HEIGHT = 400

    clock = pygame.time.Clock()
    FPS = 30
    frame_count = 0
    BKG_COLOR = (5,38,20)
    #BKG_COLOR = (230,230,230) #-- DEBUG
    win = pygame.display.set_mode((WIDTH, HEIGHT))

    def __init__(self):
        pygame.display.set_caption("Blackjack")
        
        self.animator = Animator(framerate=self.FPS)

        self.deck = Deck( (self.WIDTH - 120, 20) )
        self.deck.shuffleDeck()
        self.wallet = 1000
        self.bet_amount = 100
        self.playerHand = 0
        self.dealerHand = 0

        self.state = ""

        #---- UI ELEMENTS
        self.playerSlot = CardSlot((self.WIDTH/2,self.HEIGHT/2+40),70,100,(3,28,15))
        self.playerTitle = Header((self.WIDTH/2+35,self.HEIGHT/2+30),80,20,(230,230,230),"Your Hand","centered",font_name="Times New Roman",font_size=15)
        self.playerScore = Header((self.WIDTH/2+40,self.HEIGHT/2+160),80,20,(230,230,230),0,"centered",font_name="Times New Roman",font_size=15)
        self.playerWallet = Header((10,5),80,20,(230,230,230),"",font_name="Times New Roman",font_size=30)
        
        self.playerBet = Header((15,40),80,20,(230,230,230),"",font_name="Times New Roman",font_size=30)
        self.increaseBet = Button((15,75),25,25,(10,10,10),"+",self.increaseBetAmount)
        self.decreaseBet = Button((45,75),25,25,(10,10,10),"-",self.decreaseBetAmount)

        self.beginRound = Button((75,75),100,25,(10,10,10),"begin round",font_name="Times New Roman",font_size=15, action=self.setStateStart)

        self.dealerSlot = CardSlot((self.WIDTH/2,self.HEIGHT/2-150),70,100,(3,28,15))
        self.dealerTitle = Header((self.WIDTH/2+35,self.HEIGHT/2-160),80,20,(230,230,230),"Dealer's Hand","centered",font_name="Times New Roman",font_size=15)
        self.dealerScore = Header((self.WIDTH/2+40,self.HEIGHT/2-30),80,20,(230,230,230),0,"centered",font_name="Times New Roman",font_size=15)

        self.actionLog = Log((10,self.HEIGHT-50),100,200,5)
        #self.actionLog.pushText(TextComponent("you started a round"))
        #self.actionLog.pushText(TextComponent("bet: $500"))
        #self.actionLog.pushText(TextComponent("you lost the bet"))

        self.playerHit = Button((self.WIDTH-120,self.HEIGHT/2+40),75,35,(10,10,10),"Hit",self.dealCardPlayer,font_name="Times New Roman",font_size=20)
        self.playerStand = Button((self.WIDTH-120,self.HEIGHT/2+80),75,35,(10,10,10),"Stand",self.setStateDealer,font_name="Times New Roman",font_size=20)
        # - - - -

        #self.animator.lerp(self.deck.pop(), (self.dealerSlot.coordinates[0]+5,self.dealerSlot.coordinates[1]+5), 0.5)
        #self.GameController = BlackJack(deck=self.deck, animator=self.animator,playerSlot=self.playerSlot.coordinates,dealerSlot=self.dealerSlot.coordinates)

    def increaseBetAmount(self):
        self.bet_amount+=10
        if self.bet_amount >= self.wallet:
            self.bet_amount = self.wallet

    def decreaseBetAmount(self):
        self.bet_amount-=10
        if self.bet_amount < 0:
            self.bet_amount = 0

    def dealCardPlayer(self):
        card = self.deck.pop()
        self.playerHand+= card.getValue(self.playerHand)
        self.animator.lerp(card, (self.playerSlot.coordinates[0],self.playerSlot.coordinates[1]), 0.5)
        self.playerSlot.coordinates = (self.playerSlot.coordinates[0]-30,self.playerSlot.coordinates[1])

    def dealCardDealer(self):
        card = self.deck.pop()
        self.dealerHand+= card.getValue(self.dealerHand)
        self.animator.lerp(card, (self.dealerSlot.coordinates[0],self.dealerSlot.coordinates[1]), 0.5)
        self.dealerSlot.coordinates = (self.dealerSlot.coordinates[0]-30,self.dealerSlot.coordinates[1])

    def setStateStart(self):
        self.state = "start"
    def setStatePlayer(self):
        self.state = "player"
    def setStateDealer(self):
        self.state = "dealer"
    def setStateEnd(self):
        self.state = "end"

    def stateUpdate(self):
        if self.state == "":
           self.deck = Deck( (self.WIDTH - 120, 20) )
           self.deck.shuffleDeck()
           self.playerHand = 0
           self.dealerHand = 0
           self.dealerSlot.coordinates = (self.WIDTH/2,self.HEIGHT/2-150)
           self.playerSlot.coordinates = (self.WIDTH/2,self.HEIGHT/2+40)

        elif self.state == "start":
            self.wallet -= self.bet_amount
            self.dealCardPlayer()
            self.dealCardDealer()
            self.dealCardPlayer()
            self.state = "player"
        elif self.state == "player":
            if self.playerHand >= 21:
                self.state = "end"
        elif self.state == "dealer":
            if self.dealerHand < 17:
                self.dealCardDealer()
            else:
                self.state = "end"
        elif self.state == "end":
            if self.dealerHand == 21:
                self.actionLog.pushText("dealer blackjack. dealer wins")
            elif self.dealerHand > 21:
                self.actionLog.pushText("dealer bust. you win")
                self.wallet += self.bet_amount*2
            else:
                if self.playerHand > 21:
                    self.actionLog.pushText("player bust. dealer wins")
                elif self.playerHand == 21:
                    self.actionLog.pushText("player blackjack. you win")
                    self.wallet += self.bet_amount*2
                elif self.dealerHand <= self.playerHand:
                    self.actionLog.pushText(f"you win {self.playerHand}:{self.dealerHand}")
                    self.wallet += self.bet_amount*2
                else:
                    self.actionLog.pushText(f"dealer wins {self.dealerHand}:{self.playerHand}")
            self.state = ""

    def update(self):
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False

            # - - - - Update on event / continuously
            
            self.playerHit.update()
            self.playerStand.update()

            self.increaseBet.update()
            self.decreaseBet.update()
            self.beginRound.update()
            self.playerWallet.setText(f"Wallet: ${self.wallet}")
            self.playerBet.setText(f"Bet: ${self.bet_amount}")
            self.playerScore.setText(f"{self.playerHand}")
            self.dealerScore.setText(f"{self.dealerHand}")
            
            self.stateUpdate()

        self.animator.update()
            # - - - - 

            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     for button in self.buttons:
            #         button.update()

        #self.card.render(self.win)

        self.clock.tick(self.FPS)

    def render(self):
        self.win.fill(self.BKG_COLOR)
        # - - - - Render Actors

        self.playerSlot.render(self.win)
        self.dealerSlot.render(self.win)
        self.playerTitle.render(self.win)
        self.dealerTitle.render(self.win)
        self.playerScore.render(self.win)
        self.dealerScore.render(self.win)
        
        self.playerWallet.render(self.win)
        self.playerBet.render(self.win)
        self.increaseBet.render(self.win)
        self.decreaseBet.render(self.win)

        self.beginRound.render(self.win)

        self.actionLog.render(self.win)

        self.playerHit.render(self.win)
        self.playerStand.render(self.win)

        self.deck.render(self.win)
        # - - - -
        pygame.display.flip()


    def start(self):
        while True:
            self.update()
            self.render()


if __name__ == "__main__":
    app = App()
    app.start()