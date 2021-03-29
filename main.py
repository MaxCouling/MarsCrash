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
steps = 4
message ="GAME OVER"

#variables
damage = 0
num_of_asteroids = 80

bg = pygame.image.load('background.png').convert()# get the background
bgy =0


#playerhitbox

myFont = pygame.font.SysFont("Times New Roman", 18)


class Asteroid:#asteroid class
  def __init__(self, pos_x, pos_y):#THE TWO THINGYS INSIDE THE OBJCET
    self.pos = [pos_x, pos_y]
  def update(self):
    for i in range(self):#making all the 
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


def draw_text(text,font,color,surface,x,y):
  textobj = myFont.render(text,1,color)
  textrect = textobj.get_rect()
  textrect.topleft = (x,y)
  surface.blit(textobj,textrect)   

def main_menu():
  click = False
  
  while True:
    pygame.display.update()#updates the screen
    clock.tick(60)#make sthe menu run at 60fps
    screen.fill ((0,0,0))
    draw_text("main menu",myFont,(255,255,255), screen,20,20)

    mx, my = pygame.mouse.get_pos()#gets the mouse postion. mx is mouse x and mouse y is mouse y postion on the screen
    

    button_1 = pygame.Rect(50,100,200,50)
    button_2 = pygame.Rect(50,200,200,50)
    pygame.draw.rect(screen,(255,0,0),button_1)
    pygame.draw.rect(screen,(255,0,0),button_2)
    if button_1.collidepoint((mx,my)):
      if click:
        rocketgame()
    if button_2.collidepoint((mx,my)):
      if click:
        pass




    for event in pygame.event.get():#getting all the keyboard inputs from user
      if event.type == QUIT:#if one of those inputs is the user pressing the quit button
        pygame.quit()#it will terminate ptgame
        sys.exit()
      if event.type == KEYDOWN:
        if event.key == K_ESCAPE:
          pygame.quit()#it will terminate ptgame
          sys.exit()
      if event.type == MOUSEBUTTONDOWN:
        if event.button == 1:
          click = True





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



def platformer():#carry on platformer from here
    print ("move on")
    




def rocketgame():
  global rocket_rect, rocket, bgy
  t = Timer(45.0,platformer)
  t.start
  rocket = Rocket()
  rocket.rect.x = 250
  rocket.rect.y = 100
  rocket.rect.x = 0  # go to x
  rocket.rect.y = 0  # go to y
  rocket_list = pygame.sprite.Group()
  rocket_list.add(rocket)
  Asteroid.update(num_of_asteroids)
  while True:
    
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
      main_menu()
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








main_menu()#starts the code