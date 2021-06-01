
import pygame, sys, random

import sys
import random
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
big_asteroid = pygame.image.load("BigAsteroid.png")
rocket_image = pygame.image.load("player.png")
dababy = pygame.image.load("dababy.jpg")
front = pygame.image.load("mars front.png")
pygame.display.set_icon(icon)
atmosphere_colour = (252,116,53)
#variables
asteroids = []
num_of_asteroids = 100

vec = pygame.math.Vector2
mars_floor = pygame.image.load("mars_floor.png")
bg = pygame.image.load("background.png")

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


def draw_text(text,color,surface,x,y):
  textobj = myFont.render(text,1,color)
  textrect = textobj.get_rect()
  textrect.topleft = (x,y)
  surface.blit(textobj,textrect)   

class Main_menu:#this is the main menu and the dying screen on pygame # 
  
  def __init__(self):
    pass #sets self.click to false for the mouse clicking input
  
  
  def menu(self):
    click = False
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
      if button_1.collidepoint((mx,my)):#if the mouse is collding with the boxes x and y
        pygame.draw.rect(screen,(100,100,100),button_1)#makes it grey
        draw_text("Lets Go!",myFont,(255,255,255), screen, 75,105)#drawiing the start text
        
        if click:
          r = Rocketgame()
          r.rocketGameRunning()
          

      if button_2.collidepoint((mx,my)):
        if click:
          pass

      click = False#sets self.click to false before the mouse button down event but after the 
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


#need to add sound


class Rocketgame:
  def __init__(self):
    self.rocket = Rocket()
    self.rocket.rect.x = 250#this is where the rocket starts off in the screen
    self.rocket.rect.y = 100
    
    self.rocket_list = pygame.sprite.Group()
    self.rocket_list.add(self.rocket)
    self.num_of_asteroids = 100#the number of asteroids that the rocket will have to dodge on the way to mars
    self.minigame_bgY = 0#sets the backround images y value to 0
    self.damage = 0#sets the damge to 0
    asteroids.clear()#makes it so that the list of asteroids is clear before adding more. So that the code doesn't keep adding more and more asteroids
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
    big_asteroid_posy = 1000
    while True:#loops the game 
      
      end_time = time.time()
      print(end_time - start_time)


      if end_time - start_time > 45:#when all the baby asteroids are gone

        screen.blit(big_asteroid,(0,big_asteroid_posy))
        big_asteroid_posy -= 5
        if big_asteroid_posy <= 0:
          Game.game(2)
        

      self.rocket_hitbox = pygame.Rect(self.rocket.rect.x, self.rocket.rect.y, rocket_image.get_width(), rocket_image.get_height())#this is used as the hitbox for the rocket collisons with asteroids
      
      pygame.display.update()
      screen.fill(atmosphere_colour)#fills the screen with the atsmophere colour
      screen.blit(bg, (0, self.minigame_bgY))#this function is what makes the backround image move down in the rocket videogame
      self.rocket.update()#makes the rocket image move by x or y 
      self.rocket_list.draw(screen)#draws the rocket in the new x or y depending on if the player has pressed a new input
      
      self.minigame_bgY -= 5#makes the image move down by 5 pixes every time this loops over
      self.asteroid_collison()
      self.button_input()
      
      length = self.damage *10
      pygame.draw.rect(screen, (0,0,0),pygame.Rect(30,368,500,32))#this is healthbar code
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

  
class Background(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.bgimage = pygame.image.load("mars_bg.png")
    self.bgY = 0
    self.bgX = 0
  def render(self):
    screen.blit(self.bgimage,(self.bgY,self.bgX))

 
 
class Ground(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.image = pygame.image.load("mars_floor.png")
    self.rect = self.image.get_rect(center = (300, 360))
    
  def render(self):
    screen.blit(self.image,(self.rect.x,self.rect.y))



    
class Player(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.image_right = pygame.image.load("Astronaut.png")#loading the player in
    self.image_left = pygame.image.load("Astronaut_L.png")
    self.image = self.image_right
    self.rect = self.image.get_rect()#getting the hitbox for the player
    
    self.ACC = 0.3
    self.FRIC = -0.10
    
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
  

    pressed_keys = pygame.key.get_pressed()
    
    if pressed_keys[K_LEFT] or pressed_keys[K_a]:
      self.acc.x += -self.ACC#making it so when you press the left arrow key the acc goes down
    
    if pressed_keys[K_RIGHT] or pressed_keys[K_d]:
      self.acc.x += self.ACC
      
    # Formulas to calculate velocity while accounting for friction
    
    self.acc.x += self.vel.x * self.FRIC #slows the player down
    self.vel += self.acc #adds the acceleration to the veloctiy
    self.pos += self.vel + 0.5 * self.acc  # Updates Position with new values
    
    
    
    if self.pos.x > 600:#this is stopping the player getting out
      self.pos.x = 0
      game.rendertb = False
      self.level += 1#make sthe level plus one notifying the rest of the code that you are on a different level
    
    if self.pos.x < 0:#if the player goes all the way to the left of the screen
      self.pos.x = 600#the player is then teleported to the right, giving the illusion of going to a different level
      game.rendertb = False#if there is a textbox rendered it will now be unrendered as we don't want this going across different screens
      self.level -= 1#makes the rest of the code know we are on a different level now
    self.rect.midbottom = self.pos  # Update rect with new pos
  
  def update(self):#animation
    if self.vel.x > 0:
      self.image = self.image_right
    else:
      self.image = self.image_left
  
  def gravity_check(self):
    hits = pygame.sprite.spritecollide(player , ground_group, False)
    if self.vel.y > 0:
      if hits:
        lowest = hits[0]#the first one in the list is the lowest
        if self.pos.y < lowest.rect.bottom:#if the player is touching the ground
          self.pos.y = lowest.rect.top +1#add one so it is above the ground
          self.vel.y = 0#set the verticle velocity to 0, it is on the ground now
          self.jumping = False#if player is touching the ground, it cannot be in the state of jump (duh)
  
  def jump(self):
    self.rect.x += 1
 
    # Check to see if payer is in contact with the ground
    hits = pygame.sprite.spritecollide(self, ground_group, False)
     
    self.rect.x -= 1
 
    # If touching the ground, and not currently jumping, cause the player to jump.
    if hits and not self.jumping:
       self.jumping = True
       self.vel.y = -player.jump_height
  
class Object_load(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    
    
    #init crashsite stuff
    self.crash_image = pygame.image.load("crash.png")
    self.crash_coords = (300,220)
    
    self.water_image = pygame.image.load("water.png")
    self.mine_image = pygame.image.load("mine.png")
    self.game = Game()
    self.crash_rect = (self.crash_image.get_rect(topleft = (300,220)))
    
    

  def render(self):
    
    
    
    if player.level == 1:#the crashsite is on level 1K_a
      
      screen.blit(self.crash_image,self.crash_rect)#loads the crashsite in
    elif player.level == 0:#the water is on level 0
      
      screen.blit(self.water_image,(200,220))#loads the thing in
    elif player.level == -1:#the mine is on level -1
      
      screen.blit(self.mine_image,(400,220))#loads the thing in

class Textbox:
  def __init__(self):
    
    
    
    self.tb = pygame.image.load("tb little.png")#loads in the background picture
    self.tb_rect = (self.tb.get_rect(topleft = (50,20)))#makes the background hitbox so we know when you click out of it

    self.buy = pygame.image.load("BUY.png")
    self.buy_rect = (self.buy.get_rect(topleft = (300,60)))
    
    self.sold = pygame.image.load("SOLD.png")
    self.sold_rect = (self.sold.get_rect(topleft = (300,60)))
    self.is_sold = False
  def render(self):
    screen.blit(self.tb,self.tb_rect)#this is were the text is going to go
    draw_text("Jumpboost",(255,255,255),screen,150,60)
    
    if self.is_sold:
      screen.blit(self.sold,self.sold_rect)
      
    else:
      screen.blit(self.buy,self.buy_rect)
    
    


      
  def bigtextbox_render(self):
    pass



  

    


class Game:#actual game
  def __init__(self):
    #variables and constants that need to be decleared
    self.rendertb = False
  def game(self):
    
    while True:#main game loop
      
      player.gravity_check()
      for event in pygame.event.get():

        # Will run when the close window button is clicked    
        if event.type == QUIT:
          pygame.quit()
          sys.exit() 
             
        # For events that occur upon clicking the mouse (left click) 
        
        if event.type == pygame.MOUSEBUTTONDOWN:
          if event.button == 1:
            
            
            self.handle_click()
  

            
            
 
        # Event handling for a range of different key presses    
        if event.type == pygame.KEYDOWN:
          
          if event.key == pygame.K_SPACE:
            player.jump()
        
          



      
      
      
      
      player.move()
      player.update()
      background.render()
      ground.render()
      if self.rendertb:#just checks if it wants to render the texbox then it renders it in the main loop
        textbox.render()
      objectload.render()
      screen.blit(player.image, player.rect)
      #need to draw mars floor/ make a tile system for that
      #need to make "nodes", which you can get reasources
      #ice can be converted to water or hydrogen and oxegen, hydrogen to power rovers and oxegen to breathe
      
      pygame.display.update()
      clock.tick(60)
      #use https://pygame-gui.readthedocs.io/en/latest/theme_reference/theme_horizontal_scroll_bar.html
  
  
  def handle_click(self):
    mx, my = pygame.mouse.get_pos()#gets the mouse coords
    
    if player.level == 1:
      
      if objectload.crash_rect.collidepoint(mx,my): #seeing if it over the nouse when clicked, if it is over the crashsite or the
        self.rendertb = True#render the textbox
        return#need this otherwise it will run the rest of the code and because this isnt in the textbox it will not bring it up
      
      
        
      if self.rendertb:#if the mouse isnt over the crashsite it might be over the textbox and 
        #we don't want it to leave if it is over the textbox, seees if the textbox is allready up also because we 
        # don't want it making it so that when you click the area that the textbox is supposed to be but isnt htere you open the textbox
          
        if textbox.tb_rect.collidepoint(mx,my):#if it clicks inside the box, it will keep the box up
          self.rendertb = True
          
        
          if not textbox.is_sold:#if the upgrade hasnt been purchased, this code will play
            if textbox.buy_rect.collidepoint(mx,my):#User has bought an jump upgrade, will call jump upgrade method
              player.jump_height += 20#adds the upgrade
              textbox.is_sold = True #setting is_sold to true

          
          

        else:
          self.rendertb = False#in all other cases but there two it will return false

    
      
    


    
    
textbox = Textbox()
ground = Ground()
background = Background()
ground_group = pygame.sprite.Group()
ground_group.add(ground)
player = Player()
Playergroup = pygame.sprite.Group()
objectload = Object_load()
game = Game()

menu = Main_menu()#starts the code
#menu.menu()
game.game()




