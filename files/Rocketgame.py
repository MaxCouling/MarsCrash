import pygame
from pygame import *
import sys
import time
from files.rocket import Rocket
from files.asteroid import Asteroid
from files.game import Game


BG = pygame.image.load("Space.png")
BIG_ASTEROID  = pygame.image.load("BigAsteroid.png")
HEALTHBAR_HEIGHT = 30
num_of_asteroids = 100#the number of asteroids that the rocket will have to dodge on the way to mars
ATMOSPHERE_COLOUR = (252,116,53)
RED = (255,0,0)
BLACK = (0,0,0)
WINDOW_WIDTH = 600#window width
WINDOW_HEIGHT = 400
WINDOW_SIZE = (WINDOW_WIDTH,WINDOW_HEIGHT)
screen = pygame.display.set_mode((WINDOW_SIZE))#initate the screeb
clock = pygame.time.Clock()#starts the pygame clock, helps with keeping the uprate at 60

rocket = Rocket()

class Rocketgame:
  def __init__(self):
    self.rocket = Rocket()
    self.rocket.rect.x = 250#this is where the rocket starts off in the screen
    self.rocket.rect.y = 100
    
    self.rocket_list = pygame.sprite.Group()
    self.rocket_list.add(self.rocket)
    
    self.minigame_bgY = 0#sets the backround images y value to 0
    self.damage = 0#sets the damge to 0
    
    
      
    self.rocket_hitbox = pygame.Rect(self.rocket.rect.x, self.rocket.rect.y, self.rocket.image.get_width(), self.rocket.image.get_height())
    
    self.steps = 4 

  


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
    asteroid_list = []
    start_time = time.time()
    big_asteroid_posy = 1000
    
    for i in range(num_of_asteroids):
      asteroid = Asteroid()
      asteroid_list.append(asteroid)
    counter = 0
    
    while True:#loops the game 
      
      end_time = time.time()
      print(end_time - start_time)

      if end_time - start_time > 25:#when all the baby asteroids are gone

        screen.blit(BIG_ASTEROID,(0,big_asteroid_posy))
        big_asteroid_posy -= 5
        
        if big_asteroid_posy <= 0:
          game = Game()
          game.game()

      
      
      pygame.display.update()
      screen.fill(BLACK)#fills the screen with black
      screen.blit(BG, (0, self.minigame_bgY))#this function is what makes the backround image move down in the rocket videogame

      
      
      
      self.rocket.update()#makes the rocket image move by x or y and animates it
      
      #self.rocket_list.draw(screen)#draws the rocket in the new x or y depending on if the player has pressed a new input
      screen.blit(self.rocket.image,(self.rocket.rect.x,self.rocket.rect.y))#blitting the rocket on the 
      print(self.minigame_bgY)
      if self.minigame_bgY <= -BG.get_height():
        self.minigame_bgY = 0
        print("yeah")
      else:
        self.minigame_bgY -= 5#makes the image move down by 5 pixes every time this loops over
      
      
      
      for asteroid in asteroid_list:
        if pygame.Rect.colliderect(asteroid.rect, self.rocket_hitbox):
          self.damage += 1
          
      
      
      #for asteroid in asteroid.asteroid_list:
      #  asteroid.draw()
      
      for asteroid in asteroid_list:
        asteroid.rotate += asteroid.speed
        asteroid.y -= abs(asteroid.speed * 10)#gets the absolute speed, doesn't care for negatives
        asteroid.draw()
      
      
      
      
      
      self.button_input()
      
      length = self.damage *5
      pygame.draw.rect(screen, BLACK,pygame.Rect(0,WINDOW_HEIGHT-HEALTHBAR_HEIGHT,WINDOW_WIDTH,HEALTHBAR_HEIGHT))#this is healthbar code (X , Y , WIDTH, HRIGHT)
      pygame.draw.rect(screen, RED, pygame.Rect(0, WINDOW_HEIGHT - HEALTHBAR_HEIGHT, WINDOW_WIDTH - length,HEALTHBAR_HEIGHT))
      
      
      if self.rocket.rect.x <= 0:#boundries in the game for x axis
        self.rocket.rect.x = 0
      elif self.rocket.rect.x >= WINDOW_WIDTH - self.rocket.image.get_width():
        self.rocket.rect.x = WINDOW_WIDTH - self.rocket.image.get_width()
      if self.rocket.rect.y <= 0:#boundries in the game for y axis
        self.rocket.rect.y = 0
      elif self.rocket.rect.y >= WINDOW_HEIGHT - self.rocket.image.get_height() - HEALTHBAR_HEIGHT:
        self.rocket.rect.y = WINDOW_HEIGHT - self.rocket.image.get_height() - HEALTHBAR_HEIGHT#makes the player cannot go past 368. Player image is 32px and width is 400, 400 - 32 = 368.
      
      
      clock.tick(60)#making the game run at 60fps by limiting the amount of.0
      if self.damage >=120:#if the damge = 50, makes the player die and makes the player also go back to the starting menu
        return#function of the menu