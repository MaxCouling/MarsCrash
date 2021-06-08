import pygame
w_width = 600#window width
w_height = 400
WINDOW_SIZE = (w_width,w_height)
screen = pygame.display.set_mode((WINDOW_SIZE))#initate the screensize


class Background(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.bgimage = pygame.image.load("mars_bg.png")
    self.bgY = 0
    self.bgX = 0
  def render(self):
    screen.blit(self.bgimage,(self.bgY,self.bgX))