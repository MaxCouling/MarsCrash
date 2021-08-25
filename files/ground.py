import pygame
w_width = 600#window width
w_height = 400
WINDOW_SIZE = (w_width,w_height)
canvas = pygame.Surface((WINDOW_SIZE))#initate the screensize

class Ground(pygame.sprite.Sprite):
  """Setting the groudn tiles x and y and the imaage used for it"""
  def __init__(self,x,y):
    super().__init__()
    self.x = x
    self.y = y
    self.image = pygame.image.load("mars_floor.png")
    self.rect = self.image.get_rect(center = (self.x,self.y))
    
