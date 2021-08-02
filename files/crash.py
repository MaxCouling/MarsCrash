import pygame
from pygame import *
import sys
from files.textbox import Textbox

class Crash:
    def __init__(self,x,y):
        #terminal screen setup
        w_width = 600#window width
        w_height = 400
        WINDOW_SIZE = (w_width,w_height)
        self.screen = pygame.display.set_mode((WINDOW_SIZE))#initate the screensize
        
        
        
        
        
        
        self.image = pygame.transform.rotate(pygame.transform.scale(pygame.image.load('rocket1.png'),(100,100)),110)
        
        self.avatar = pygame.transform.scale(pygame.image.load('computer.png'), (125,125))
       
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.x = x
        self.y = y
        self.rect = self.image.get_rect(topleft = (self.x, self.y))
        self.clock = pygame.time.Clock()
        self.tutorial = True
        self.textbox = Textbox()
        #exit 
        self.exitbutton = pygame.Rect(30,30,50,50)
        


    def on_click(self):
        #gives the textbox to show the player what is going to happen next, go into the computer terminal to be able to smelt items and stuff
        if self.tutorial:
            self.textbox.render("COMPUTER",(120,25),(255,255,255),"HI, I am the ships computer! This is the terminal where you can smelt and use electroysis to use electricity to split water into hydrogen and oxygen",(120,50),(255,255,255),self.avatar,200)
            self.tutorial = False
        self.terminal()#opens the terminal
    
    def terminal(self):
        running =  True
        while running:
            pygame.display.update()
            self.clock.tick(60)
            self.screen.fill((0,0,0))#background colour
            mx, my = pygame.mouse.get_pos()#gets the mouse postion. mx is mouse x and mouse y is mouse y postion on the screen
            
            pygame.draw.rect(self.screen,(70,70,70),pygame.Rect(30,30,540,340))
            pygame.draw.rect(self.screen,(255,0,0),self.exitbutton)
            if self.exitbutton.collidepoint((mx,my)):
                if click:
                    running = False


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




        