from cgitb import text
import pygame
from typing import Tuple
from math import floor

def getRectCenter( pos,width,height=None ):
    if not height: height = width
    return (pos[0]+width/2,pos[1]+height/2)

class UIComponent():

    def __init__(self, coordinates:Tuple[int,int], width:int, height:int, color:Tuple[int,int,int]):
        pygame.init()

        self.coordinates = coordinates
        self.width, self.height = width, height
        self.rect = pygame.Rect(coordinates[0], coordinates[1], width, height)
        self.color = color

    def isClicked(self):
        mouse = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            return True

class TextComponent():

    def __init__(self, text_string, font_name="Arial", font_size=30, text_color=(255,255,255)):
        pygame.font.init()
        self.text_string = text_string
        self.font_name = font_name
        self.font_size = font_size
        self.text_color = text_color
        self.font = pygame.font.SysFont(font_name, font_size)
        self.text = self.font.render(text_string,1,text_color)

    def getTextCenter(self, container_coords:Tuple[int,int], container_size:Tuple[int,int])-> Tuple[int,int]:
        '''find the centered position for text in a rect '''

        rectCenter = getRectCenter(container_coords, container_size[0], container_size[1])
        textDim = self.font.size(self.text_string)
        textDim = getRectCenter((0,0),textDim[0], textDim[1])
        return (rectCenter[0]-textDim[0], rectCenter[1]-textDim[1])

    def getTextAlignment(self, container_coords:Tuple[int,int], container_size:Tuple[int,int], alignment, padding=5) -> Tuple[int,int]:
        ''' 
            returns coordinates for text to be aligned to container in a relative position 

            alignment options: "center", "TL", "TR", "BL", "BR" 
        
        '''
        
        textDim = self.font.size(self.text_string)

        if alignment == "center":
            return self.getTextCenter(container_coords, container_size)

        if alignment == "TL":
            return (container_coords[0]+padding,container_coords[1]+padding)

        if alignment == "BL":
            return (container_coords[0]+padding,container_coords[1]+container_size[1]- padding -textDim[1])

        if alignment == "TR":
            return (container_coords[0]+container_size[0]-textDim[0]-padding,container_coords[1]+padding )

        if alignment == "BR":
            return (container_coords[0]+container_size[0]-textDim[0]-padding, container_coords[1]+container_size[1] -padding -textDim[1])
