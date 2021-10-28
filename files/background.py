import pygame
w_width = 600  # window width
w_height = 400
WINDOW_SIZE = (w_width, w_height)
screen = pygame.display.set_mode((WINDOW_SIZE))  # initate the screensize
BLACK = (0, 0, 0)


class Background(pygame.sprite.Sprite):
    def __init__(self):
        """I found that adding multiple mountains caused my game to lag. This is because the PNG's i was constantly loading was taking up
        alot of the machines power, what i did to fix it was convert it into a png, the transparent parts of the picture is now black,
        then i took the black away, this made it preform alot better."""
        super().__init__()
        # sky
        self.sky = pygame.image.load("assets/mars_bg.png").convert()
        self.skyY = 0
        self.skyX = 0
        # mountains 0
        self.mountains0 = pygame.image.load(
            "assets/mars_background_outer.png").convert()
        self.mountains0.set_colorkey(BLACK)
        self.mountains0Y = 0
        self.mountains0X = -100
        # mountains 1
        self.mountains1 = pygame.image.load(
            "assets/mars_mountains.png").convert()
        self.mountains1.set_colorkey(BLACK)
        self.mountains1Y = 0
        self.mountains1X = -200
        # mountains 2
        self.mountains2 = pygame.image.load(
            "assets/mars_background_inner.png").convert()
        self.mountains2.set_colorkey(BLACK)
        self.mountains2Y = 0
        self.mountains2X = -200
