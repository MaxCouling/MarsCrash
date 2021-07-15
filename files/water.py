import pygame

class Water:
    def __init__(self,x,y):
        self.image = pygame.image.load('water.png')
        self.icon = pygame.transform.scale(pygame.image.load("watericon.png"), (32, 32))
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.x = x
        self.y = y
        self.rect = self.image.get_rect(topleft = (self.x, self.y))
        self.water = 0#the amount of ore that the mine has produced
        


    def on_click(self):
        self.water += 1

        
    
    