import pygame
from pygame import *
import sys
from textbox import Textbox
from mine import Mine
from water import Water
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
            self.textbox.render("COMPUTER",(120,25),(255,255,255),"HI, This is where you craft!",(120,70),(255,255,255),self.avatar,200)
            self.tutorial = False
        #self.terminal()#opens the terminal
        self.clicked = True

        
    
    """def terminal(self):
        running =  True
        self.ore_amount = self.mine.ore
        self.water_amount = self.water.water
        while running:
            pygame.display.update()
            self.clock.tick(60)
            self.screen.fill((0,0,0))#background colour
            mx, my = pygame.mouse.get_pos()#gets the mouse postion. mx is mouse x and mouse y is mouse y postion on the screen
            
            #EXIT BUTTON
            pygame.draw.rect(self.screen,(70,70,70),pygame.Rect(30,30,540,340))
            pygame.draw.rect(self.screen,(255,0,0),self.exitbutton)
            if self.exitbutton.collidepoint((mx,my)):
                if click:
                    running = False
            #inventory display
            pygame.draw.rect(self.screen,WHITE,self.whitebox)
            
            #ore
            self.screen.blit( pygame.font.Font.render(Font, str(self.ore_amount),1,BLACK),(120,40))#ore number
            self.screen.blit(self.ore_icon,(83,40))
            #water
            self.screen.blit(pygame.font.Font.render(Font, str(self.water_amount),1,BLACK),(193,40))
            self.screen.blit(self.water_icon,(160,40))
            

            click = False
            for event in pygame.event.get():#getting all the keyboard inputs from user
                if event.type == QUIT:#if one of those inputs is the user pressing the quit button
                    pygame.quit()#it will terminate ptgame
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()#it will terminate ptgame
                        sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
"""



        