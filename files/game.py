import pygame
from pygame import *
from files.player import Player
from files.ground import Ground
from files.background import Background
from files.camera import *
import sys

#initating window and clocPlayergroup = pygame.sprite.Group()



class Game:
  def __init__(self):
    pygame.init()
    WINDOW_W, WINDOW_H = 6000, 400
    self.canvas = pygame.Surface((WINDOW_W*10,WINDOW_H))#setting the canvas
    self.window = pygame.display.set_mode(((WINDOW_W,WINDOW_H)))#setting the window
    self.clock = pygame.time.Clock()#pygame clock
    self.dababy = pygame.image.load("dababy.jpg")
    
    
    #loading player, scenes and self.
    self.player = Player()
    self.groundgroup = pygame.sprite.Group()

    for i in range(0,4000, 600):
      g = Ground(i, 280)
      self.groundgroup.add(g)

    self.background = Background()
    
    self.camera = Camera(self.player)
   # auto = Auto(self.camera,self.player)#its called borderself.
    self.follow = Follow(self.camera, self.player)
    
    
    
  
  def game(self):
    self.camera.setmethod(self.follow)
    while True:#main loop
      self.clock.tick(60)
      pygame.display.update()
      #key inputs
      for event in pygame.event.get():#exits the game 
        if event.type == pygame.QUIT:
          sys.exit()
        if event.type == KEYDOWN:
          if event.key == K_SPACE:
            self.player.jump()
          if event.key == K_DOWN:
            self.player.acc.x += -self.player.ACC#making it so when you press the left arrow key the acc goes down
        

      self.canvas.fill((155,154,0))
      self.canvas.blit(self.dababy,(50,100))
      #updating and animating sprites
      self.player.move()#uses the player move funciton
      self.player.update()
      self.gravity_check()
      self.camera.scroll()
      
      #updating window and display
      self.canvas.blit(self.background.image,(self.background.bgX - (self.camera.offset.x/5), self.background.bgY - (self.camera.offset.y/5)))
      self.canvas.blit(self.player.image,(self.player.rect.x- self.camera.offset.x, self.player.rect.y - self.camera.offset.y))
      
      for ground in self.groundgroup:
        self.canvas.blit(ground.image,(ground.rect.x - self.camera.offset.x, ground.rect.y - self.camera.offset.y))
      
      self.window.blit(self.canvas, (0,0))
      
      pressed_keys = pygame.key.get_pressed()
    
      if pressed_keys[K_LEFT] or pressed_keys[K_a]:
        self.player.acc.x += -self.player.ACC#making it so when you press the left arrow key the acc goes down
    
      if pressed_keys[K_RIGHT] or pressed_keys[K_d]:
        self.player.acc.x += self.player.ACC
  
  def gravity_check(self):
    
    hits = pygame.sprite.spritecollide(self.player ,self.groundgroup, False)
    if self.player.vel.y > 0:
      if hits:
        lowest = hits[0]#the first one in the list is the lowest
        if self.player.pos.y < lowest.rect.bottom:#if the player is touching the ground
          self.player.pos.y = lowest.rect.top +1#add one so it is above the ground
          self.player.vel.y = 0#set the verticle velocity to 0, it is on the ground now
          self.player.jumping = False#if player is touching the ground, it cannot be in the state of jump (duh)
      
