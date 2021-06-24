import pygame
from pygame import *
vec = pygame.math.Vector2
from files.ground import Ground
from files.textbox import Textbox

textbox = Textbox()





Playergroup = pygame.sprite.Group()
w_width = 600#window width
w_height = 400
WINDOW_SIZE = (w_width,w_height)
screen = pygame.display.set_mode((WINDOW_SIZE))#initate the screensize

class Player(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.image_right = pygame.image.load("Astronaut.png")#loading the player in
    self.image_left = pygame.image.load("Astronaut_L.png")
    self.image = self.image_right
    self.rect = self.image.get_rect()#getting the hitbox for the player
    
    self.ACC = 0.3
    self.FRIC = -0.10

    self.ground_y = 280
    #postion and direction
    self.vx = 0
    self.pos = vec((200, 200))
    self.vel = vec(0,0)
    self.acc = vec(0,0)
    self.direction = "RIGHT"
    self.jumping = False
    self.level = 1
    self.jump_height = 12
  def move(self):#method to do the running
    
    self.acc = vec(0,0.5)#gravity, Force that constantly pulls the player down
    
    if abs(self.vel.x) > 0.3:
      self.running = True
    else:
      self.running = False
  


      
    # Formulas to calculate velocity while accounting for friction
    
    self.acc.x += self.vel.x * self.FRIC #slows the player down
    self.vel += self.acc #adds the acceleration to the veloctiy
    self.pos += self.vel + 0.5 * self.acc  # Updates Position with new values
    
    
    
    
    self.rect.midbottom = self.pos  # Update rect with new pos
  
  def update(self):#animation
    if self.vel.x > 0:
      self.image = self.image_right
    else:
      self.image = self.image_left
  
  
  
  def jump(self):
    self.rect.x += 1
 
    # Check to see if payer is in contact with the ground
    hits = pygame.sprite.spritecollide(self, ground_group, False)
     
    self.rect.x -= 1
 
    # If touching the ground, and not currently jumping, cause the player to jump.
    if hits and not self.jumping:
       self.jumping = True
       self.vel.y = -self.jump_height