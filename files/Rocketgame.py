import pygame
from pygame import *
import sys
import time
from files.rocket import Rocket
from files.asteroid import Asteroid
from files.game import Game

ROCKET_IMAGE = pygame.image.load("player.png")
BG = pygame.image.load("background.png")
BIG_ASTEROID  = pygame.image.load("BigAsteroid.png")
num_of_asteroids = 100#the number of asteroids that the rocket will have to dodge on the way to mars
ATMOSPHERE_COLOUR = (252,116,53)
asteroid_list = []
BLACK = (0,0,0)
w_width = 600#window width
w_height = 400
WINDOW_SIZE = (w_width,w_height)
screen = pygame.display.set_mode((WINDOW_SIZE))#initate the screeb
clock = pygame.time.Clock()#starts the pygame clock, helps with keeping the framerate at 60
game = Game()
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
    
    
      
    self.rocket_hitbox = pygame.Rect(self.rocket.rect.x, self.rocket.rect.y, ROCKET_IMAGE.get_width(), ROCKET_IMAGE.get_height())
    
    self.steps = 4 

  def asteroid_collison(self):
      
      
    for j in asteroid.asteroids_list:
      if self.rocket_hitbox.colliderect(asteroid.rect):
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
    
    for i in range(num_of_asteroids):
      asteroid = Asteroid()
      asteroid_list.append(asteroid)
    
    
    while True:#loops the game 
      
      end_time = time.time()
      #print(end_time - start_time)

      if end_time - start_time > 45:#when all the baby asteroids are gone

        screen.blit(BIG_ASTEROID,(0,big_asteroid_posy))
        big_asteroid_posy -= 5
        
        if big_asteroid_posy <= 0:
          game.game()

      self.rocket_hitbox = pygame.Rect(self.rocket.rect.x, self.rocket.rect.y, ROCKET_IMAGE.get_width(), ROCKET_IMAGE.get_height())#this is used as the hitbox for the rocket collisons with asteroids
      
      pygame.display.update()
      screen.fill(ATMOSPHERE_COLOUR)#fills the screen with the atsmophere colour
      screen.blit(BG, (0, self.minigame_bgY))#this function is what makes the backround image move down in the rocket videogame
      self.rocket.update()#makes the rocket image move by x or y 
      self.rocket_list.draw(screen)#draws the rocket in the new x or y depending on if the player has pressed a new input
      
      self.minigame_bgY -= 5#makes the image move down by 5 pixes every time this loops over
      
      
      
      
      
      
      
      #for asteroid in asteroid.asteroid_list:
      #  asteroid.draw()
      
      for asteroid in asteroid_list:
        asteroid.rotate += asteroid.speed
        asteroid.y -= abs(asteroid.speed)#gets the absolute speed
        asteroid.draw()
      
      if pygame.Rect.colliderect(rocket.rect,asteroid.rect):
        self.damage += 1
      
      
      
      self.button_input()
      
      length = self.damage *10
      pygame.draw.rect(screen, BLACK,pygame.Rect(30,368,500,32))#this is healthbar code
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
        return#function of the menu