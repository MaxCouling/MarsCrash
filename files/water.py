import pygame
from files.textbox import Textbox


class Water:
    def __init__(self):
        self.image = pygame.image.load('assets/water.png')
        self.icon = pygame.transform.scale(pygame.image.load("assets/watericon.png"), (32, 32))
        self.water_for_tutorial = pygame.transform.scale(pygame.image.load('assets/watericon.png'),(125,125))
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.x,self.y = 2400,235
        self.rect = self.image.get_rect(topleft = (self.x, self.y))
        self.water = 0#the amount of ore that the mine has produced
        self.textbox = Textbox()
        self.tutorial = True

    def on_click(self):
        """When the water is clicked this function happens. It adds one to the water counter and if it is the players first time clicking on the water they get a tutorial"""
        self.water +=1 
        
        if self.tutorial:
            self.textbox.render("WATER",(120,25),(255,255,255),"This is ice, click on it to get water!\nwater can be used for upgrades\nand smelting ore!",(120,65),(255,255,255),self.water_for_tutorial,150)
            self.tutorial = False
        
    
    