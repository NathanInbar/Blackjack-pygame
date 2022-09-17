import pygame
from src.Deck import Deck

class App:
    pygame.init()

    WIDTH = 600
    HEIGHT = 400

    clock = pygame.time.Clock()
    FPS = 27
    frame_count = 0
    BKG_COLOR = (5,38,20)
    #BKG_COLOR = (230,230,230) #-- DEBUG
    win = pygame.display.set_mode((WIDTH, HEIGHT))

    def __init__(self):
        pygame.display.set_caption("Blackjack")
        self.deck = Deck( (self.WIDTH - 120, 20) )

    def update(self):
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False

            # - - - - Update Actors


            # - - - - 

            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     for button in self.buttons:
            #         button.update()

        #self.card.render(self.win)

        self.clock.tick(self.FPS)

    def render(self):
        self.win.fill(self.BKG_COLOR)
        # - - - - Render Actors

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