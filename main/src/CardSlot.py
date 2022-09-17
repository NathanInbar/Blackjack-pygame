from typing import Tuple
from src.util import UIComponent
import pygame

class CardSlot(UIComponent):

    def __init__(self, coordinates: Tuple[int, int], width: int, height: int, color: Tuple[int, int, int]):
        UIComponent.__init__(self,coordinates, width, height, color)

    def render(self,win):
        pygame.draw.rect(win, self.color, self.rect)