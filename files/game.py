import pygame
from files.player import Player
from files.camera import *
import sys

#initating window and clock



#loading self.player, scenes and self.


class Game:
  def __init__(self):
    pygame.init()
    WINDOW_W, WINDOW_H = 600, 400
    self.canvas = pygame.Surface((WINDOW_W,WINDOW_H))#setting the canvas
    self.window = pygame.display.set_mode(((WINDOW_W,WINDOW_H)))#setting the window
    self.clock = pygame.time.Clock()#pygame clock
    self.dababy = pygame.image.load("dababy.jpg")
    self.player = Player()
    self.camera = Camera(self.player)
    self.border = Border(self.camera,self.player)#its called border
  
  def game(self):
    while True:#main loop

      #key inputs
      for event in pygame.event.get():#exits the game 
        if event.type == pygame.QUIT:
          sys.exit()
      self.canvas.fill((155,154,0))
      self.canvas.blit(self.dababy,(50,100))
      #updating and animating sprites
      self.player.move()#uses the self.player move funciton
      print("deeznae")
      #updating window and display
      self.canvas.blit(self.player.image,(self.player.rect.x- self.camera.offset.x, self.player.rect.y - self.camera.offset.y))
      self.window.blit(self.canvas, (0,0))
