import pygame



class Rocket(pygame.sprite.Sprite):#using pygames sprite function for future aninmations
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.movex = 0
    self.movey = 0
    self.frame = 0
    self.images = [pygame.image.load("rocket1.png"),pygame.image.load("rocket2.png")]#list is for animation
    self.framenum = 1
    
    
    self.image = self.images[self.frame]
    self.rect = self.image.get_rect()
  
  def control(self,x,y):
    #control rocket movement
    self.movex += x
    self.movey += y
  
  def update(self):
    
    self.image = self.images[self.frame]#animating the rocket falling to mars
    print("frame",self.frame)
    print("framenum",self.framenum)
    if self.frame == self.framenum:#resetting the amount of frames
      self.frame = 0
    else:
      self.frame += 1

    self.rect.x += self.movex
    self.rect.y += self.movey
    
    
    
    
    
    
      
