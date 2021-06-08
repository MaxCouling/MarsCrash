
import pygame
from files.asteroid import Asteroid
from files.rocket import Rocket
from files.main_menu import Main_menu
from files.game import Game
from files.background import Background
from files.ground import Ground
from files.player import Player
from files.textbox import Textbox


from pygame import *
import sys
import random





pygame.init()#initates pygame

w_width = 600#window width
w_height = 400
WINDOW_SIZE = (w_width,w_height)
screen = pygame.display.set_mode((WINDOW_SIZE))#initate the 

#THIS WILL HOLD ALL THE OBJECTS


pygame.display.set_caption("Mars Rover")
ICON = pygame.image.load("logo.png")
ASTEROID_IMAGE = pygame.image.load("greyAsteroid.png")
ROCKET_IMAGE = pygame.image.load("player.png")

pygame.display.set_icon(ICON)
ATMOSPHERE_COLOUR = (252,116,53)
#variables

num_of_asteroids = 100#the number of asteroids that the rocket will have to dodge on the way to mars


mars_floor = pygame.image.load("mars_floor.png")


#playerhitbox

myFont = pygame.font.SysFont("Comic Sans MS", 24)

"""
class Asteroid:#asteroid class
  def __init__(self, pos_x, pos_y):#THE TWO THINGYS INSIDE THE OBJCET
    self.pos = [pos_x, pos_y]
    self.asteroids_list = []
    self.asteroid_location = 0
  def update(self):
    
    self.asteroid_location = Asteroid(random.randint(0,568), random.randint(400,16000))#change this
    self.asteroids_list.append(self.asteroid_location)
    self.rect = ASTEROID_IMAGE.get_rect()
    screen.blit(ASTEROID_IMAGE, self.rect)#astriod location
"""






#need to add sound



    
asteroid = Asteroid()
textbox = Textbox()



Playergroup = pygame.sprite.Group()

game = Game()

menu = Main_menu()#starts the code
menu.menu()





