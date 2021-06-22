import pygame
w_width = 600#window width
w_height = 400
WINDOW_SIZE = (w_width,w_height)
canvas = pygame.Surface((WINDOW_SIZE))#initate the screensize

class Ground(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.image = pygame.image.load("mars_floor.png")
    self.rect = self.image.get_rect(center = (300, 360))
    
  def render(self):
    canvas.blit(self.image,(self.rect.x,self.rect.y))
