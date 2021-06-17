import pygame
from files.player import Player
from files.camera import *
import sys

#initating window and clock
pygame.init()
WINDOW_W, WINDOW_H = 600, 400
canvas = pygame.Surface((WINDOW_W,WINDOW_H))#setting the canvas
window = pygame.display.set_mode(((WINDOW_W,WINDOW_H)))#setting the window
clock = pygame.time.Clock()#pygame clock

#loading player, scenes and camera
player = Player()
camera = Camera(player)
border = Border(camera,player)#its called border
crashsite = pygame.image.l

while True:#main loop

  #key inputs
  for event in pygame.event.get():#exits the game 
    if event.type == pygame.QUIT:
      sys.exit()
  
  
  #updating and animating sprites
  player.move()#uses the player move funciton

  #updating window and display
  canvas.blit(player.image,(player.rect.x- camera.offset.x, player.rect.y - camera.offset.y))
  window.blit(canvas, (0,0))
