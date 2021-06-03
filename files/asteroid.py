import random
import pygame
ASTEROID_IMAGE = pygame.image.load("greyAsteroid.png")
w_width = 600#window width
w_height = 400
WINDOW_SIZE = (w_width,w_height)
screen = pygame.display.set_mode((WINDOW_SIZE))#initate the 

class Asteroid:

  def __init__(self):
    self.x = random.randint(0,568)#400,16000
    self.y = random.randint(0,300)#0,568
    

  def recycle(self):
    pass
    
    

  
  
  def draw(self):
    self.rect = ASTEROID_IMAGE.get_rect(topleft = (self.x,self.y))
    screen.blit(ASTEROID_IMAGE, self.rect)
  
    