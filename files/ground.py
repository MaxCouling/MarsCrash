import pygame
w_width = 600#window width
w_height = 400
WINDOW_SIZE = (w_width,w_height)
screen = pygame.display.set_mode((WINDOW_SIZE))#initate the screensize

class Ground(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.image = pygame.image.load("mars_floor.png")
    self.rect = self.image.get_rect(center = (300, 360))
    
  def render(self):
    screen.blit(self.image,(self.rect.x,self.rect.y))
