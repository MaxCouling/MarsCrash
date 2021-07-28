
import pygame
from files.asteroid import Asteroid
from files.rocket import Rocket
from files.main_menu import Main_menu
from files.game import Game
from files.background import Background
from files.ground import Ground
from files.player import Player



from pygame import *






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

s_floor = pygame.image.load("mars_floor.png")


#playerhitbox

myFont = pygame.font.SysFont("Vistor", 24)


menu = Main_menu()#starts the code

menu.menu()






