import pygame
from pygame import *
vec = pygame.math.Vector2









Playergroup = pygame.sprite.Group()
w_width = 600#window width
w_height = 400
WINDOW_SIZE = (w_width,w_height)
screen = pygame.display.set_mode((WINDOW_SIZE))#initate the screensize

class Player(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.image_right = [pygame.image.load("right1.png"), pygame.image.load("right2.png"), pygame.image.load("right1.png"), pygame.image.load("right3.png")]#loading the player in
    self.image_left = [pygame.image.load("left1.png"), pygame.image.load("left2.png"), pygame.image.load("left1.png"), pygame.image.load("left3.png")]
    self.image = self.image_right[1]
    self.rect = self.image.get_rect()#getting the hitbox for the player
    
    self.ACC = 0.3
    self.FRIC = -0.10

    #these are for the border that the player cannot get past
    self.left_border = -200
    self.right_border = 3900

    self.ground_y = 280
    #postion and direction
    self.vx = 0
    self.pos = vec((200, 200))
    self.vel = vec(0,0)
    self.acc = vec(0,0)
    self.direction = "RIGHT"
    self.jumping = False
    self.jump_height = 12
    self.move_frame = 0 #tracking the current frame of the character
    
  def move(self):#method to do the running
    self.acc = vec(0,0.5)#gravity, Force that constantly pulls the player down
    #if at the border
    if self.rect.x >= self.right_border -50:
      self.acc.x -= 10
    if self.rect.x <= self.left_border:
      print("ay")
      self.acc.x +=10# the reason why im changing the acceleration of the player rather than just making it stop is because it makes a funny bounce

    if abs(self.vel.x) > 0.3:
      self.running = True
    else:
      self.running = False
    # Formulas to calculate velocity while accounting for friction
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[K_LEFT] or pressed_keys[K_a]:
      self.acc.x += -self.ACC#making it so when you press the left arrow key the acc goes down
    
    if pressed_keys[K_RIGHT] or pressed_keys[K_d]:
      self.acc.x += self.ACC

    self.acc.x += self.vel.x * self.FRIC #slows the player down
    self.vel += self.acc #adds the acceleration to the veloctiy
    self.pos += self.vel + 0.5 * self.acc  # Updates Position with new values

    self.rect.midbottom = self.pos  # Update rect with new pos

    
    
  
  def update(self):#animation
    
    self.move_frame +=1
    if self.move_frame > 3:#if it is the 4th frame, go and make it go back to the first one
      self.move_frame = 0#makes it go back to the standing frame
    print(self.move_frame)
    
    #if player is not jumping and they ARE running do this code below
    if not self.jumping and self.running:
      if self.vel.x > 0:#if the player is going right
        self.image = self.image_right[self.move_frame]
      else:
        self.image = self.image_left[self.move_frame]
      #makes it so it moves the frame by one everytime this goes over
      self.move_frame
    #This final section fixes the bug that makes it so when you try to stop, the sprite for moving shows
    if abs(self.vel.x) < 0.5 and self.move_frame != 0: #if the speed is below a certian point and the frame is not standing
      self.move_frame = 0#sets it to standing
      if self.vel.x > 0:#still a little bit of velocity, will use this to detrimine either left or right
        self.image = self.image_right[self.move_frame]
      else:
        self.image = self.image_left[self.move_frame]

  
  
  
  