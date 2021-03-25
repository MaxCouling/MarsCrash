import pygame, sys, random
import time
from pygame.locals import *
from typing import Tuple
from threading import Timer#import timer for the delays in game

pygame.init()#initates pygame
clock = pygame.time.Clock()#imports the time
screen = pygame.display.set_mode((600,400))#initate the WINDOW_SIZE
ALPHA = (0, 255, 0)
asteroids = []#THIS WILL HOLD ALL THE OBJECTS
ani = 4
black = (0,0,0)#tuple
pygame.display.set_caption("Mars Rover")
icon = pygame.image.load("logo.png")
asteroid_image = pygame.image.load("asteroid.png")
rocket_image = pygame.image.load("player.png")
pygame.display.set_icon(icon)
atmosphere_colour = (252,116,53)

class Asteroid:#asteroid class
  def __init__(self, pos_x, pos_y):#THE TWO THINGYS INSIDE THE OBJCET
    self.pos = [pos_x, pos_y]
  def update(num):
    for i in range(num):#making all the 
      asteroid_location = Asteroid(random.randint(0,568), random.randint(400,16000))#change this
      asteroids.append(asteroid_location)


class Rocket(pygame.sprite.Sprite):#using pygames sprite function for future aninmations
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.movex = 0
    self.movey = 0
    self.frame = 0
    self.images = []
    img = rocket_image.convert()
    img.convert_alpha()  # optimise alpha
    img.set_colorkey(ALPHA)  # set alpha
    self.images.append(img)
    self.image = self.images[0]
    self.rect = self.image.get_rect()
  
  def control(self,x,y):
    #control rocket movement
    self.movex += x
    self.movey += y
  
  def update(self):
    self.rect.x += self.movex
    self.rect.y += self.movey
    


rocket = Rocket()  # spawn player
rocket.rect.x = 0  # go to x
rocket.rect.y = 0  # go to y
rocket_list = pygame.sprite.Group()
rocket_list.add(rocket)
steps = 4
message ="GAME OVER"

#variables
running = True 
damage = 0
num_of_asteroids = 80

bg = pygame.image.load('background.png').convert()# get the background
bgy = 0 #background y


#playerhitbox

myFont = pygame.font.SysFont("Times New Roman", 18)
Asteroid.update(num_of_asteroids)
def asteroid_collison():
  global damage
  for asteroid_location in asteroids:
    asteroid_rect = pygame.Rect(asteroid_location.pos[0], asteroid_location.pos[1], asteroid_image.get_width(), asteroid_image.get_height())
    screen.blit(asteroid_image, asteroid_location.pos)#astriod location
    asteroid_location.pos[1] -= 6#IMPORTANT!!!!!!!! HOW TO GET THE X AND Y VARIABLES FROM OBJECT TYPE BEAT
    asteroid_rect.x = asteroid_location.pos[0]
    asteroid_rect.y = asteroid_location.pos[1]
    
    if rocket_rect.colliderect(asteroid_rect):
      damage += 1
      
def button_input():
  for event in pygame.event.get():#getting all the keyboard inputs from user
      if event.type == QUIT:#if one of those inputs is the user pressing the quit button
        print("Exited")#prints ecited into the console
        pygame.quit()#it will terminate ptgame
        sys.exit()
      
      if event.type == KEYDOWN:#movemtnt code
        if event.key == K_RIGHT:
          rocket.control(steps, 0)
        if event.key == K_LEFT:
          rocket.control(-steps, 0)
        if event.key == K_DOWN:
          rocket.control(0,steps)
        if event.key == K_UP:
          rocket.control(0,-steps)

      if event.type == KEYUP:
        if event.key == K_RIGHT:
          rocket.control(-steps, 0)
        if event.key == K_LEFT:
          rocket.control(steps, 0)
        if event.key == K_DOWN:
          rocket.control(0, -steps)
        if event.key == K_UP:
          rocket.control(0, steps)

def healthbar(x):
  length = x *10
  pygame.draw.rect(screen, (0,0,0),pygame.Rect(30,368,500,32))
  pygame.draw.rect(screen, (255,0,0), pygame.Rect(30, 368, 500 - length,32)) 
def gameover():
  screen.fill((0,0,0))
  gameovermessage = myFont.render(str(message), 1, (254,254,254))
  screen.blit(gameovermessage, (200,100))
#moving around minigame
def redrawWindow():
    screen.blit(bg, (0, bgy))  # draws our first bg image
      # draws the seconf bg image
      # updates the screen



def platformer():
    print ("hello, world")

t = Timer(45.0, platformer)
t.start() # after 30 seconds, "hello, world" will be printed
while running:
  
  rocket_rect = pygame.Rect(rocket.rect.x, rocket.rect.y, rocket_image.get_width(), rocket_image.get_height())
  pygame.display.update()
  screen.fill(atmosphere_colour)
  redrawWindow()
  rocket.update()
  rocket_list.draw(screen)
  #print(rocket.rect.x, rocket.rect.y)
  bgy -= 5
  
  
  asteroid_collison()
  if damage >50:
    gameover()
  button_input()
  
  damage_display = myFont.render(str(damage), 1, black)#shows score
  screen.blit(damage_display, (520, 30))
  healthbar(damage)
  
  if rocket.rect.x <= 0:#boundries in the game for x axis
    rocket.rect.x = 0
  elif rocket.rect.x >= 568:
    rocket.rect.x = 568
  if rocket.rect.y <= 0:
    rocket.rect.y = 0
  elif rocket.rect.y >= 368:
    rocket.rect.y = 368
    
  
  
  clock.tick(60)#making the game run at 60fps by limiting the amount of.0