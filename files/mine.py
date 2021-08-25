import pygame
from textbox import Textbox

class Mine:
    def __init__(self):
        self.image = pygame.image.load('mine.png')
        self.icon =pygame.transform.scale(pygame.image.load("mineicon.png"), (32, 32))
        self.rock_for_tutorial = pygame.transform.scale(pygame.image.load('mineicon.png'),(125,125))
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.x,self.y = 1400,155

        self.rect = self.image.get_rect(topleft = (self.x, self.y))
        self.ore = 0#the amount of ore that the mine has produced
        
        self.textbox = Textbox()
        self.tutorial = True

    def on_click(self):
        """When clicked it adds one to the score o"""
        self.ore += 1
        
        if self.tutorial:
            self.textbox.render("MINE",(120,25),(255,255,255),"This is the mine, click on it to get \nthe martian ore!\n\n\nUse the ore to increase the distance your battery\ncan take you! ",(120,65),(255,255,255),self.rock_for_tutorial,250)
            self.tutorial = False
    
    
        
    