import pygame
from pygame import *
import sys
from textbox import Textbox

Font = pygame.font.Font("fonts/visitor1.ttf",30)
WHITE = (255,255,255)
BLACK = (0,0,0)
class Crash:
    def __init__(self,mine,water):
        #terminal screen setup
        w_width = 600#window width
        w_height = 400
        WINDOW_SIZE = (w_width,w_height)
        self.screen = pygame.display.set_mode((WINDOW_SIZE))#initate the screensize
        
        self.mine = mine
        self.water = water

        self.ore_amount = 0
        self.ore_icon = mine.icon

        self.water_amount = 0
        self.water_icon = water.icon
        
        
        
        
        self.image = pygame.transform.rotate(pygame.transform.scale(pygame.image.load('rocket1.png'),(100,100)),110)
        
        self.avatar = pygame.transform.scale(pygame.image.load('computer.png'), (125,125))
       
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.x,self.y = 400,155
        
        self.rect = self.image.get_rect(topleft = (self.x, self.y))
        self.clock = pygame.time.Clock()
        self.tutorial = True
        self.textbox = Textbox()
        #exit 
        self.exitbutton = pygame.Rect(30,30,50,50)

        #white box
        self.whitebox = pygame.Rect(80,30,490,50)
        #items
        self.hydrogen = 0
        self.oxygen = 0
        self.iron = 0
        self.clicked = False
        
        
        


    def on_click(self):
        #gives the textbox to show the player what is going to happen next, go into the computer terminal to be able to smelt items and stuff
        if self.tutorial:
            self.textbox.render("COMPUTER",(120,25),(255,255,255),"HI, This is where you craft and fill\nyour battery up to go on the trips to\nthe deposits",(120,70),(255,255,255),self.avatar,200)
            self.tutorial = False
        #self.terminal()#opens the terminal
        self.clicked = True

    



        