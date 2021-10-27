import pygame
from pygame import *
import sys
import time
from files.rocket import Rocket
from files.asteroid import Asteroid
from files.game import Game
from files.game import Font
from files.game import WHITE


BG = pygame.image.load("Space.png")
BIG_ASTEROID  = pygame.image.load("BigAsteroid.png")
MARS = pygame.transform.scale(pygame.image.load("Mars_picture.png"), (600, 600))
HEALTHBAR_HEIGHT = 30
num_of_asteroids = 50#the number of asteroids that the rocket will have to dodge on the way to mars
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
    self.title = pygame.image.load("mars_crash_title.png")
  


  def button_input(self):
    """This method gets the inputs of the player and translates it to the movement of the sprite"""
    for event in pygame.event.get():#getting all the keyboard inputs from user
        if event.type == QUIT:#if one of those inputs is the user pressing the quit button
          
          pygame.quit()#it will terminate ptgame
          sys.exit()
        
        if event.type == KEYDOWN:#movemtnt code
          if event.key == K_RIGHT or event.key == K_d:
            self.rocket.control(self.steps, 0)
          if event.key == K_LEFT or event.key == K_a:
            self.rocket.control(-self.steps, 0)
          if event.key == K_DOWN or event.key == K_s:
            self.rocket.control(0,self.steps)
            
          if event.key == K_UP or event.key == K_w:
            self.rocket.control(0,-self.steps)

        if event.type == KEYUP:
          if event.key == K_RIGHT or event.key == K_d:
            self.rocket.control(-self.steps, 0)
          if event.key == K_LEFT or event.key == K_a:
            self.rocket.control(self.steps, 0)
          if event.key == K_DOWN or event.key == K_s:
            self.rocket.control(0, -self.steps)
          if event.key == K_UP or event.key == K_w:
            self.rocket.control(0, self.steps)


  def rocketGameRunning(self):
    asteroid_list = []
    start_time = time.time()
    mars_y = 1000
    #spawning the asteroids in a list
    for asteroid in range(num_of_asteroids):
      asteroid = Asteroid()
      asteroid_list.append(asteroid)
    pygame.mixer.music.load('assets/asteroid_music.mp3')#music
    pygame.mixer.music.play()
    """Main loop where the asteroid minigame plays in"""
    while True:#loops the game 
      
      end_time = time.time()
      
      
          

      
      
      pygame.display.update()
      screen.fill(BLACK)#fills the screen with black
      screen.blit(BG, (0, self.minigame_bgY))#this function is what makes the backround image move down in the rocket videogame
      if end_time - start_time > 25:#when all the baby asteroids are gone

        screen.blit(MARS,(0,mars_y))
        mars_y -= 5
        
        if mars_y <= 100:
          
          self.mini_title_screen()
      
      
      
      self.rocket.update()#makes the rocket image move by x or y and animates it
      
      #self.rocket_list.draw(screen)#draws the rocket in the new x or y depending on if the player has pressed a new input
      screen.blit(self.rocket.image,(self.rocket.rect.x,self.rocket.rect.y))#blitting the rocket on the 
      
      if self.minigame_bgY <= -BG.get_height():
        self.minigame_bgY = 0 
      else:
        self.minigame_bgY -= 5#makes the image move down by 5 pixels every time this loops over
      
      
      #asteroid collison code, if any of the asteroids in the astroid lists hitbox hits the rockets hit box damage += 1 
      for asteroid in asteroid_list:
        if pygame.Rect.colliderect(asteroid.rect, self.rocket_hitbox):
          self.damage += 1
          
      
      
      #this draws the asteroid onto the screen
      for asteroid in asteroid_list:
        asteroid.rotate += asteroid.speed
        asteroid.y -= abs(asteroid.speed * 10)#gets the absolute speed, doesn't care for negatives
        asteroid.draw()
      
      
      
      
      
      self.button_input()#calls the method for the player movement of the rocket
      
      length = self.damage *5#button length is properinatial to the damage 
      pygame.draw.rect(screen, BLACK,pygame.Rect(0,WINDOW_HEIGHT-HEALTHBAR_HEIGHT,WINDOW_WIDTH,HEALTHBAR_HEIGHT))#the black behind the healthbar to show the player how much damage he has lost
      pygame.draw.rect(screen, RED, pygame.Rect(0, WINDOW_HEIGHT - HEALTHBAR_HEIGHT, WINDOW_WIDTH - length,HEALTHBAR_HEIGHT))#this is healthbar code (X , Y , WIDTH, HEIGHT),
      
      
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
        pygame.mixer.music.stop()#stops the music
        return#function of the menu

  def mini_title_screen(self):
    """This Code fades from the rocket level and makes the player go into the real level"""
    fade = pygame.Surface(WINDOW_SIZE)#sets the window size for the fade
    fade.fill(BLACK)#what colour the fade is going to be
    for alpha in range(0,300):#for loop that fades the screen
      fade.set_alpha(alpha)
      screen.blit(fade, (0,0))
      pygame.display.update()
      pygame.time.delay(23)#delay per frame 
      for event in pygame.event.get():#this code will exucute once the user has pressed any key
        if event.type == QUIT:#if one of those inputs is the user pressing the quit button
          sys.exit()
    
    while True:
      screen.fill(BLACK)
      screen.blit(self.title,(0,0))#title will be a png saying press any key to continue
      screen.blit( pygame.font.Font.render(Font, "PRESS ANY KEY TO CONTINUE",1,WHITE),(70,250))
      pygame.display.update()
      
      for event in pygame.event.get():#this code will exucute once the user has pressed any key
        if event.type == KEYDOWN or event.type == MOUSEBUTTONDOWN:

          pygame.mixer.music.stop()#stops the music
          game = Game()
          game.game()
        if event.type == QUIT:#if one of those inputs is the user pressing the quit button
          
          pygame.quit()#it will terminate ptgame
          sys.exit()
        
