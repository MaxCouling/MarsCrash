import pygame


class Rocket(
        pygame.sprite.Sprite):  # using pygames sprite function for future aninmations
    def __init__(self):
        """At the moment the rocket DOES have a slight animation of heat in the heat sheild, its just going too fast
        for anyone to notice. I might make more animation for the rocket if i want to. Also what this fucntion does is
        that it sets the movement of the player's rect the 'hitbox' as the players x and y,"""
        pygame.sprite.Sprite.__init__(self)
        self.movex = 0
        self.movey = 0
        self.frame = 0
        self.images = [pygame.image.load("assets/rocket1.png"), pygame.image.load("assets/rocket2.png")]  # list is for animation
        self.framenum = 1

        self.image = self.images[self.frame]
        self.rect = self.image.get_rect()

    def control(self, x, y):
        """the self.movex/y moves the hitbox so it is important that it is equal to x and y"""
        # control rocket movement
        self.movex += x
        self.movey += y

    def update(self):
        """This method plays the animations and moves the hitbox"""
        self.image = self.images[self.frame]  # animating the rocket falling to mars

        if self.frame == self.framenum:  # resetting the amount of frames
            self.frame = 0
        else:
            self.frame += 1

        self.rect.x += self.movex
        self.rect.y += self.movey
