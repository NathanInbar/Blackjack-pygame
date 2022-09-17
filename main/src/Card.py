from src.util import UIComponent, TextComponent
import pygame

class Card(UIComponent):

    def __init__(self, suit, suit_color, value, coordinates):
        UIComponent.__init__(self,coordinates,width=70,height=100,color=(232,232,232))
        self.valueText = TextComponent(text_string=str(value),font_size=15,text_color=(4,4,4))
        self.suitText = TextComponent(text_string=suit,font_name="segoeuisymbol",font_size=17,text_color=suit_color)

        self.suit = suit
        self.value = value

    def getValue(self, hand_value):
        value = self.value
        if value == "J" or value == "Q" or value == "K":
            return 10
        if value == "A":
            if hand_value + 11 > 21:
                return 1
            else:
                return 11

        return value


    def renderBack(self, win):
        back_color = (40,12,23)
        pygame.draw.rect(win, back_color, self.rect)
        pygame.draw.rect(win, self.color, self.rect.inflate(-4,-4))
        pygame.draw.rect(win, back_color, self.rect.inflate(-12,-12))

        insignia = TextComponent("♔","segoeuisymbol",text_color=(235,177,52))

        win.blit(insignia.text, insignia.getTextAlignment(self.coordinates,(self.width,self.height),"center",padding=0))



    def renderFace(self, win):
        valuePadding=5
        win.blit(self.valueText.text, self.valueText.getTextAlignment(self.coordinates,(self.width,self.height),"TL",padding=valuePadding))
        win.blit(self.valueText.text, self.valueText.getTextAlignment(self.coordinates,(self.width,self.height),"TR",padding=valuePadding))
        win.blit(self.valueText.text, self.valueText.getTextAlignment(self.coordinates,(self.width,self.height),"BL",padding=valuePadding))
        win.blit(self.valueText.text, self.valueText.getTextAlignment(self.coordinates,(self.width,self.height),"BR",padding=valuePadding))

        suitPadding = self.suitText.font.size(self.valueText.text_string)
        suitPadding = max(suitPadding[0],suitPadding[1]) - valuePadding

        win.blit(self.suitText.text, self.suitText.getTextAlignment(self.coordinates,(self.width,self.height),"TL",padding=suitPadding))
        win.blit(self.suitText.text, self.suitText.getTextAlignment(self.coordinates,(self.width,self.height),"TR",padding=suitPadding))
        win.blit(self.suitText.text, self.suitText.getTextAlignment(self.coordinates,(self.width,self.height),"BL",padding=suitPadding))
        win.blit(self.suitText.text, self.suitText.getTextAlignment(self.coordinates,(self.width,self.height),"BR",padding=suitPadding))

        win.blit(self.suitText.text, self.suitText.getTextAlignment(self.coordinates,(self.width,self.height),"center",padding=suitPadding))


    def render(self, win, isInDeck):
        border_size = 2
        pygame.draw.rect(win, (0,0,0), self.rect.inflate(border_size,border_size))    #border
        pygame.draw.rect(win, self.color, self.rect)

        if isInDeck:
            self.renderBack(win)
        else:
            self.renderFace(win)



    def __str__(self):
        value = self.value
        suit = self.suit

        middle_spaces = "    " if value == 10 else "      "

        card =  "*----------*"+"\n"+ \
                f"| {value}"+ middle_spaces + f"{value} |"+"\n"+ \
                f"| {suit}      {suit} |"+"\n"+ \
                "|          |"+"\n"+ \
                "|          |"+"\n"+ \
                f"| {suit}      {suit} |"+"\n"+ \
                f"| {value}"+ middle_spaces + f"{value} |"+"\n"+ \
                "*----------*"+"\n"

        return card