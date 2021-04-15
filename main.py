import pygame
import sys
import random
import pygame_gui
import time
from pygame.locals import *
from typing import Tuple


pygame.init()#initates pygame
clock = pygame.time.Clock()#imports the time
WINDOW_SIZE = (600,400)
screen = pygame.display.set_mode((WINDOW_SIZE))#initate the 
ALPHA = (0,255,0)
#THIS WILL HOLD ALL THE OBJECTS
ani = 4
black = (0,0,0)#tuple
pygame.display.set_caption("Mars Rover")
icon = pygame.image.load("logo.png")
asteroid_image = pygame.image.load("asteroid.png")
rocket_image = pygame.image.load("player.png")
dababy = pygame.image.load("dababy.jpg")
front = pygame.image.load("mars front.png")
pygame.display.set_icon(icon)
atmosphere_colour = (252,116,53)
#variables

num_of_asteroids = 100
asteroids = []
bg = pygame.image.load('background.png').convert()# get the background



#playerhitbox

myFont = pygame.font.SysFont("Comic Sans MS", 24)


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

class Main_menu:#this is the main menu and the dying screen on pygame # 
  
  def __init__(self):
    self.click = False #sets self.click to false for the mouse clicking input
  
  
  def menu(self):
    self.click = False
    while True:
      pygame.display.update()#updates the screen
      clock.tick(60)#make sthe menu run at 60fps
      screen.fill ((0,0,0))#makes the screen black
      draw_text("main menu",myFont,(255,255,255), screen,20,20)#this draw text function makes the text main menu appear on the top left corner

      mx, my = pygame.mouse.get_pos()#gets the mouse postion. mx is mouse x and mouse y is mouse y postion on the screen
      

      button_1 = pygame.Rect(50,100,200,50)#postion of the mouse 1
    
      button_2 = pygame.Rect(50,200,200,50)
      pygame.draw.rect(screen,(255,0,0),button_1)
      draw_text("Start",myFont,(255,255,255), screen, 75,105)#drawiing the start text
      pygame.draw.rect(screen,(255,0,0),button_2)
      if button_1.collidepoint((mx,my)):
        pygame.draw.rect(screen,(100,100,100),button_1)
        draw_text("Lets Go!",myFont,(255,255,255), screen, 75,105)#drawiing the start text
        
        if self.click:
          r = Rocketgame()
          r.rocketGameRunning()
          

      if button_2.collidepoint((mx,my)):
        if self.click:
          pass

      self.click = False#sets self.click to false before the mouse button down event but after the 
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
            self.click = True






      


      





class Rocketgame:
  def __init__(self):
    self.rocket = Rocket()
    self.rocket.rect.x = 250#this is where the rocket starts off in the screen
    self.rocket.rect.y = 100
    
    self.rocket_list = pygame.sprite.Group()
    self.rocket_list.add(self.rocket)
    self.num_of_asteroids = 100#the number of asteroids that the rocket will have to dodge on the way to mars
    self.bgy = 0#sets the backround images y value to 0
    self.damage = 0#sets the damge to 0
    Asteroid.update(num_of_asteroids)#this updates the class and makes asteroid objects
    self.rocket_hitbox = pygame.Rect(self.rocket.rect.x, self.rocket.rect.y, rocket_image.get_width(), rocket_image.get_height())
    self.steps = 4 


  def asteroid_collison(self):
    for asteroid_location in asteroids:
      asteroid_rect = pygame.Rect(asteroid_location.pos[0], asteroid_location.pos[1], asteroid_image.get_width(), asteroid_image.get_height())
      screen.blit(asteroid_image, asteroid_location.pos)#astriod location
      asteroid_location.pos[1] -= 6#IMPORTANT!!!!!!!! HOW TO GET THE X AND Y VARIABLES FROM OBJECT TYPE BEAT
      asteroid_rect.x = asteroid_location.pos[0]
      asteroid_rect.y = asteroid_location.pos[1]
      
        
      if self.rocket_hitbox.colliderect(asteroid_rect):
        self.damage += 1


  def button_input(self):
    
    for event in pygame.event.get():#getting all the keyboard inputs from user
        if event.type == QUIT:#if one of those inputs is the user pressing the quit button
          print("Exited")#prints ecited into the console
          pygame.quit()#it will terminate ptgame
          sys.exit()
        
        if event.type == KEYDOWN:#movemtnt code
          if event.key == K_RIGHT:
            self.rocket.control(self.steps, 0)
          if event.key == K_LEFT:
            self.rocket.control(-self.steps, 0)
          if event.key == K_DOWN:
            self.rocket.control(0,self.steps)
          if event.key == K_UP:
            self.rocket.control(0,-self.steps)

        if event.type == KEYUP:
          if event.key == K_RIGHT:
            self.rocket.control(-self.steps, 0)
          if event.key == K_LEFT:
            self.rocket.control(self.steps, 0)
          if event.key == K_DOWN:
            self.rocket.control(0, -self.steps)
          if event.key == K_UP:
            self.rocket.control(0, self.steps)


  def rocketGameRunning(self):
    start_time = time.time()
    while True:#loops the game 
      end_time = time.time()
      print(end_time - start_time)
      if end_time - start_time > 25:
        Game.game(1)
      self.rocket_hitbox = pygame.Rect(self.rocket.rect.x, self.rocket.rect.y, rocket_image.get_width(), rocket_image.get_height())#this is used as the hitbox for the rocket collisons with asteroids
      
      pygame.display.update()
      screen.fill(atmosphere_colour)#fills the screen with the atsmophere colour
      screen.blit(bg, (0, self.bgy))#this function is what makes the backround image move down in the rocket videogame
      self.rocket.update()#makes the rocket image move by x or y 
      self.rocket_list.draw(screen)#draws the rocket in the new x or y depending on if the player has pressed a new input
      #print(rocket.rect.x, self.rocket.rect.y)
      self.bgy -= 5#makes the image move down by 5 pixes every time this loops over
      self.asteroid_collison()
      self.button_input()
      
      length = self.damage *10
      pygame.draw.rect(screen, (0,0,0),pygame.Rect(30,368,500,32))
      pygame.draw.rect(screen, (255,0,0), pygame.Rect(30, 368, 500 - length,32))
      
      if self.rocket.rect.x <= 0:#boundries in the game for x axis
        self.rocket.rect.x = 0
      elif self.rocket.rect.x >= 568:
        self.rocket.rect.x = 568
      if self.rocket.rect.y <= 0:#boundries in the game for y axis
        self.rocket.rect.y = 0
      elif self.rocket.rect.y >= 368:
        self.rocket.rect.y = 368#makes the player cannot go past 368. Player image is 32px and width is 400, 400 - 32 = 368.
      
      
      clock.tick(60)#making the game run at 60fps by limiting the amount of.0
      if self.damage >=50:#if the damge = 50, makes the player die and makes the player also go back to the starting menu
        menu.menu()#function of the menu
  

class Game:#actual game
  def __init__(self):
    self.click = False
    
  def game(self):
    manager = pygame_gui.UIManager(WINDOW_SIZE)
    slowAnimation = 500
    while True:#this will be the little animation of it going into mars
      screen.fill ((0,0,0))#makes the screen black
      
      
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
          print("Exited")#prints ecited into the console
          pygame.quit()#it will terminate ptgame
          sys.exit()
      
      screen.fill(atmosphere_colour)
      
      if slowAnimation >= 0:
        slowAnimation -= 1
      screen.blit(front,(0,slowAnimation))
      
      
   
      pygame.display.update()
      #use https://pygame-gui.readthedocs.io/en/latest/theme_reference/theme_horizontal_scroll_bar.html
menu = Main_menu()#starts the code
menu.menu()