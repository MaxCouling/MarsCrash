import pygame
from files.player import Player
player = Player()

w_width = 600#window width
w_height = 400
WINDOW_SIZE = (w_width,w_height)
screen = pygame.display.set_mode((WINDOW_SIZE))#initate the screensize

class Object_load(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    
    
    #init crashsite stuff
    self.crash_image = pygame.image.load("crash.png")
    self.crash_coords = (300,220)
    
    self.water_image = pygame.image.load("water.png")
    self.mine_image = pygame.image.load("mine.png")
    
    self.crash_rect = (self.crash_image.get_rect(topleft = (300,220)))
    
    

  def render(self):
    
    
    
    if player.level == 1:#the crashsite is on level 1K_a
      
      screen.blit(self.crash_image,self.crash_rect)#loads the crashsite in
    elif player.level == 0:#the water is on level 0
      
      screen.blit(self.water_image,(200,220))#loads the thing in
    elif player.level == -1:#the mine is on level -1
      
      screen.blit(self.mine_image,(400,220))#loads the thing in