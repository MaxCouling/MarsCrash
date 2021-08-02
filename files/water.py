import pygame
from textbox import Textbox

class Water:
    def __init__(self,x,y):
        self.image = pygame.image.load('water.png')
        self.icon = pygame.transform.scale(pygame.image.load("watericon.png"), (32, 32))
        self.water_for_tutorial = pygame.transform.scale(pygame.image.load('watericon.png'),(125,125))
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.x = x
        self.y = y
        self.rect = self.image.get_rect(topleft = (self.x, self.y))
        self.water = 0#the amount of ore that the mine has produced
        self.textbox = Textbox()


    def on_click(self):
        self.water += 1
        
        if self.water == 1:
            self.textbox.render("WATER",(120,25),(255,255,255),"This is ice, click on it to get water!",(120,125),(155,0,155),self.water_for_tutorial,150)
        
    
    