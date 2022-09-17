import pygame

from src.Animation import Animator
from src.util import TextComponent
from src.util import Header, Log, Button
from src.Deck import Deck
from src.CardSlot import CardSlot
from src.Game import BlackJack

class App:
    pygame.init()

    WIDTH = 600
    HEIGHT = 400

    clock = pygame.time.Clock()
    FPS = 15
    frame_count = 0
    BKG_COLOR = (5,38,20)
    #BKG_COLOR = (230,230,230) #-- DEBUG
    win = pygame.display.set_mode((WIDTH, HEIGHT))

    def __init__(self):
        pygame.display.set_caption("Blackjack")

        self.animator = Animator()

        self.deck = Deck( (self.WIDTH - 120, 20) )
        self.card = self.deck.getRandomCard()

        self.GameController = BlackJack(deck=self.deck)

        #----
        self.playerSlot = CardSlot((self.WIDTH/2,self.HEIGHT/2+40),80,110,(3,28,15))
        self.playerTitle = Header((self.WIDTH/2+40,self.HEIGHT/2+30),80,20,(10,10,10),"Your Hand","centered",font_name="Times New Roman",font_size=15)
        self.playerScore = Header((self.WIDTH/2+40,self.HEIGHT/2+160),80,20,(230,230,230),0,"centered",font_name="Times New Roman",font_size=15)
        self.playerWallet = Header((10,5),80,20,(230,230,230),"",font_name="Times New Roman",font_size=30)
        
        self.playerBet = Header((15,40),80,20,(230,230,230),"",font_name="Times New Roman",font_size=30)
        self.increaseBet = Button((140,45),25,25,(10,10,10),"+",None)
        self.decreaseBet = Button((170,45),25,25,(10,10,10),"-",None)

        self.dealerSlot = CardSlot((self.WIDTH/2,self.HEIGHT/2-150),80,110,(3,28,15))
        self.dealerTitle = Header((self.WIDTH/2+40,self.HEIGHT/2-160),80,20,(10,10,10),"Dealer's Hand","centered",font_name="Times New Roman",font_size=15)
        self.dealerScore = Header((self.WIDTH/2+40,self.HEIGHT/2-30),80,20,(230,230,230),0,"centered",font_name="Times New Roman",font_size=15)

        self.actionLog = Log((10,self.HEIGHT-50),100,200,5)
        self.actionLog.pushText(TextComponent("you started a round"))
        self.actionLog.pushText(TextComponent("bet: $500"))
        self.actionLog.pushText(TextComponent("you lost the bet"))

        self.playerHit = Button((self.WIDTH-120,self.HEIGHT/2+40),75,35,(10,10,10),"Hit",None,font_name="Times New Roman",font_size=20)
        self.playerStand = Button((self.WIDTH-120,self.HEIGHT/2+80),75,35,(10,10,10),"Stand",None,font_name="Times New Roman",font_size=20)

        self.animator.lerp(self.card, (self.playerSlot.coordinates[0]+5,self.playerSlot.coordinates[1]+5), 2, self.FPS)


    def update(self):
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False

            # - - - - Update Actors

            self.playerWallet.setText(f"Wallet: ${self.GameController.wallet}")
            self.playerBet.setText(f"Bet: ${self.GameController.bet_amount}")


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