import pygame
import sys
from pygame import *
from files.textbox import Textbox
from files.player import Player
from files.background import Background
from files.ground import Ground
from files.ObjectLoader import Object_load
from files.textbox import Textbox

textbox = Textbox()
objectload = Object_load()
player = Player()
ground = Ground()
background = Background()
w_width = 600#window width
w_height = 400
WINDOW_SIZE = (w_width,w_height)
screen = pygame.display.set_mode((WINDOW_SIZE))#initate the screensize
clock = pygame.time.Clock()

class Game:#actual game
  def __init__(self):
    #variables and constants that need to be decleared
    self.level = 1
  def game(self):
    
    while True:#main game loop
      
      player.gravity_check()
      for event in pygame.event.get():

        # Will run when the close window button is clicked    
        if event.type == QUIT:
          pygame.quit()
          sys.exit() 
             
        # For events that occur upon clicking the mouse (left click) 
        
        if event.type == pygame.MOUSEBUTTONDOWN:
          if event.button == 1:
            
            
            self.handle_click()
  

            
            
 
        # Event handling for a range of different key presses    
        if event.type == pygame.KEYDOWN:
          
          if event.key == pygame.K_SPACE:
            player.jump()
        
          



      
      
      
      
      player.move()
      player.update()
      background.render()
      ground.render()
      if textbox.rendertb:#just checks if it wants to render the texbox then it renders it in the main loop
        textbox.render()
      objectload.render()#renders the crashsite, water and mine
      screen.blit(player.image, player.rect)
      #need to draw mars floor/ make a tile system for that
      #need to make "nodes", which you can get reasources
      #ice can be converted to water or hydrogen and oxegen, hydrogen to power rovers and oxegen to breathe
      
      pygame.display.update()
      clock.tick(60)
      #use https://pygame-gui.readthedocs.io/en/latest/theme_reference/theme_horizontal_scroll_bar.html
  
  
  def handle_click(self):
    mx, my = pygame.mouse.get_pos()#gets the mouse coords
    
    if player.level == 1:
      
      if objectload.crash_rect.collidepoint(mx,my): #seeing if it over the nouse when clicked, if it is over the crashsite or the
        textbox.rendertb = True#render the textbox
        return#need this otherwise it will run the rest of the code and because this isnt in the textbox it will not bring it up
      
      
        
      if textbox.rendertb:#if the mouse isnt over the crashsite it might be over the textbox and 
        #we don't want it to leave if it is over the textbox, seees if the textbox is allready up also because we 
        # don't want it making it so that when you click the area that the textbox is supposed to be but isnt htere you open the textbox
          
        if textbox.tb_rect.collidepoint(mx,my):#if it clicks inside the box, it will keep the box up
          textbox.rendertb = True
          
        
          if not textbox.is_sold:#if the upgrade hasnt been purchased, this code will play
            if textbox.buy_rect.collidepoint(mx,my):#User has bought an jump upgrade, will call jump upgrade method
              player.jump_height += 20#adds the upgrade
              textbox.is_sold = True #setting is_sold to true

          
          

        else:
          self.rendertb = False#in all other cases but there two it will return false