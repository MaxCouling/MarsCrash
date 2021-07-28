import pygame
from files.textbox import Textbox
class Mine:
    def __init__(self,x,y):
        self.image = pygame.image.load('mine.png')
        self.icon =pygame.transform.scale(pygame.image.load("mineicon.png"), (32, 32))
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.x = x
        self.y = y
        self.rect = self.image.get_rect(topleft = (self.x, self.y))
        self.ore = 0#the amount of ore that the mine has produced
        
        self.textbox = Textbox()

    def on_click(self):
        self.ore += 1
        self.textbox.render("MINE",(60,25),(255,255,255),"This is the mine, click on it to get martian ore!",(60,125),(155,0,155),self.icon)
    
    
        
    