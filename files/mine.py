import pygame

class Mine:
    def __init__(self,x,y):
        self.image = pygame.image.load('mine.png')
        self.x = x
        self.y = y
        self.rect = self.image.get_rect(center = (self.x, self.y))
    