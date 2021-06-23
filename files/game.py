import pygame
from pygame import *
from files.player import Player
from files.ground import Ground
from files.background import Background
from files.camera import *
import sys

#initating window and clocPlayergroup = pygame.sprite.Group()
player = Player()

camera = Camera(player)
auto = Auto(camera,player)#its called border
follow = Follow(camera, player)
class Game:
  def __init__(self):
    pygame.init()
    WINDOW_W, WINDOW_H = 600, 400
    self.canvas = pygame.Surface((WINDOW_W,WINDOW_H))#setting the canvas
    self.window = pygame.display.set_mode(((WINDOW_W,WINDOW_H)))#setting the window
    self.clock = pygame.time.Clock()#pygame clock
    self.dababy = pygame.image.load("dababy.jpg")
    
    
    #loading player, scenes and self.
    
    self.ground = Ground()
    self.background = Background()
    
    
    
    
    
  
  def game(self):
    camera.setmethod(follow)
    while True:#main loop
      self.clock.tick(60)
      pygame.display.update()
      #key inputs
      for event in pygame.event.get():#exits the game 
        if event.type == pygame.QUIT:
          sys.exit()
        if event.type == KEYDOWN:
          if event.key == K_SPACE:
            player.jump()
        

      self.canvas.fill((155,154,0))
      self.canvas.blit(self.dababy,(50,100))
      #updating and animating sprites
      player.move()#uses the player move funciton
      player.update()
      player.gravity_check()
      camera.scroll()
      
      #updating window and display
      self.canvas.blit(self.background.image,(self.background.bgX - (camera.offset.x/5), self.background.bgY - (camera.offset.y/5)))
      self.canvas.blit(player.image,(player.rect.x- camera.offset.x, player.rect.y - camera.offset.y))
      self.canvas.blit(self.ground.image,(self.ground.rect.x - camera.offset.x, self.ground.rect.y - camera.offset.y))
      
      self.window.blit(self.canvas, (0,0))
      
