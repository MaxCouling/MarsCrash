import pygame
from pygame import *
from files.textbox import Textbox

Font = pygame.font.Font("fonts/visitor1.ttf", 30)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class Crash:
    def __init__(self):
        # terminal screen setup
        w_width = 600  # window width
        w_height = 400
        WINDOW_SIZE = (w_width, w_height)
        self.screen = pygame.display.set_mode((WINDOW_SIZE))  # initate the screensize

        self.image = pygame.transform.rotate(pygame.transform.scale(pygame.image.load('assets/rocket1.png'), (100, 100)), 110)

        self.avatar = pygame.transform.scale(pygame.image.load('assets/computer.png'), (125, 125))

        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.x, self.y = 400, 155

        self.rect = self.image.get_rect(topleft=(self.x, self.y))

        self.tutorial = True
        self.textbox = Textbox()

        self.clicked = False

    def on_click(self):
        """If it s the first time clicking on the crash site it tells them its the palace to upgrade/ smelt and full up your battery, when clciked self.clicked = True"""
        # gives the textbox to show the player what is going to happen next, go
        # into the computer terminal to be able to smelt items and stuff
        if self.tutorial:
            self.textbox.render("COMPUTER", (120, 25), (255, 255, 255), "HI, This is where you upgrade and fill\nyour battery up to go on the trips to\nthe deposits", (120, 70), (255, 255, 255), self.avatar, 200)
            self.tutorial = False
        # self.terminal()#opens the terminal
        self.clicked = True
