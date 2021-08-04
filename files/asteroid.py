import random
import pygame
ASTEROID_IMAGE = pygame.image.load("greyAsteroid.png")
w_width = 600#window width
w_height = 400
WINDOW_SIZE = (w_width,w_height)
screen = pygame.display.set_mode((WINDOW_SIZE))#initate the 

class Asteroid:

  def __init__(self):
    
    self.x = random.randint(0,568)#0,568
    self.y = random.randint(400,16000)#400,16000
    self.rotate = random.randint(0,359)
    self.speed = random.randint(-1,1)
    self.rect = ASTEROID_IMAGE.get_rect(topleft = (self.x,self.y))
    

  def recycle(self):
    pass
    
    

  
  
  def draw(self):
    self.rotated_asteroid_image = pygame.transform.rotate(ASTEROID_IMAGE, self.rotate)
    self.rect = self.rotated_asteroid_image.get_rect(topleft = (self.x,self.y))
    
    screen.blit(self.rotated_asteroid_image, self.rect)
  
    