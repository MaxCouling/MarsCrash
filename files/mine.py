import pygame

class Mine:
    def __init__(self,x,y):
        self.image = pygame.image.load('mine.png')
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.x = x
        self.y = y
        self.rect = self.image.get_rect(topleft = (self.x, self.y))

    def on_click(self):
        print("WOHOO IM CLICKED")
    