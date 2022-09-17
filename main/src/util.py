from cgitb import text
import pygame
from typing import Tuple
from math import floor
from collections import deque

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

    def updatePosition(self, coordinates):
        self. coordinates = coordinates
        self.rect = pygame.Rect(coordinates[0], coordinates[1], self.width, self.height)

    def translatePosition(self, x_displacement, y_displacement):
        #print("im translating!")
        self.coordinates = (self.coordinates[0]+x_displacement,self.coordinates[1]+y_displacement)
        self.rect = pygame.Rect(self.coordinates[0], self.coordinates[1], self.width, self.height)


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

class Header(UIComponent, TextComponent):

    def __init__(self, coordinates, width, height, color, text_string="", alignment="", font_name="consolas", font_size=30):
        text_string = str(text_string)
        UIComponent.__init__(self, coordinates, width, height, (0,0,0))
        TextComponent.__init__(self, text_string, font_name=font_name, font_size=font_size, text_color=color)
        self.alignment = alignment

    def setText(self, text_string):
        self.text_string = text_string
        self.text = self.font.render(text_string,1,self.text_color)

    def render(self, win):
        if self.alignment == "centered":
            textDim = self.font.size(self.text_string)
            textDim = getRectCenter((0,0),textDim[0], textDim[1])
            win.blit(self.text,  (self.coordinates[0]-textDim[0], self.coordinates[1]-textDim[1]))
        else:
            win.blit(self.text, self.coordinates)

class Log(UIComponent):

    def __init__(self, coordinates, width, height, maxItems):
        UIComponent.__init__(self,coordinates,width,height,color=(0,0,0))

        self.maxItems = maxItems
        self.textLog = deque()

    def pushText(self, text):
        self.textLog.append(text)
        if len(self.textLog)>self.maxItems:
            self.textLog.pop()

    def render(self, win):
        heightDisplacement = 0
        for text in self.textLog:
            win.blit(text.text, (self.coordinates[0], self.coordinates[1]-heightDisplacement))
            heightDisplacement += text.font.size(text.text_string)[1]

class Button(UIComponent, TextComponent):

    def __init__(self, coordinates: Tuple[int,int], width, height, color, \
                         text_string, action, font_name="Arial", font_size=30, font_color=(255,255,255)):

        UIComponent.__init__(self,coordinates, width, height, color)
        TextComponent.__init__(self,text_string,font_name, font_size, font_color)

        self.action = action

    def update(self):

        if (self.isClicked()):
            self.action()

    def render(self,win):
        pygame.draw.rect(win,self.color,self.rect)
        centeredText = self.getTextCenter(self.coordinates, (self.width, self.height))
        win.blit(self.text, centeredText )