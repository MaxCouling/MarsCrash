import pygame
import sys
from game import Game
from pygame import *
from Rocketgame import Rocketgame

pygame.init()#inititlising pygame
w_width = 600#window width
w_height = 400#window height
WINDOW_SIZE = (w_width,w_height)
screen = pygame.display.set_mode((WINDOW_SIZE))#initate the screeb size
clock = pygame.time.Clock()#imports the time
BLACK = (0,0,0)#tuple
WHITE = (255,255,255)
myFont = pygame.font.Font("fonts/visitor1.ttf",30)

pygame.display.set_caption("Mars Crash")
ICON = pygame.image.load("logo.png")
ASTEROID_IMAGE = pygame.image.load("greyAsteroid.png")
ROCKET_IMAGE = pygame.image.load("player.png")
TITLE_IMAGE = pygame.image.load("mars_crash_title.png")
pygame.display.set_icon(ICON)





#little function used to make drawing text easier
def draw_text(text,color,surface,x,y):
  textobj = myFont.render(text,1,color)
  textrect = textobj.get_rect()
  textrect.topleft = (x,y)
  surface.blit(textobj,textrect)   

class Main_menu:#this is the main menu and the dying screen on pygame # 
  
  def __init__(self):
    self.straight_to_mars = True#debugger that skips the first sequence and intro to the game
  
  def menu(self):
    click = False
    while True:
      pygame.display.update()#updates the screen
      clock.tick(60)#make sthe menu run at 60fps
      screen.fill (BLACK)#makes the screen black
      screen.blit(TITLE_IMAGE,(0,0))

      mx, my = pygame.mouse.get_pos()#gets the mouse postion. mx is mouse x and mouse y is mouse y postion on the screen
      

      button_1 = pygame.Rect(200,270,200,50)#postion of the mouse 1
    
      button_2 = pygame.Rect(200,330,200,50)
      pygame.draw.rect(screen,(255,0,0),button_1)
      draw_text("Start",(255,255,255), screen, button_1.x +25,button_1.y + 5)#drawiing the start text
     
      if self.straight_to_mars:
        pygame.draw.rect(screen,(255,0,0),button_2)
      if button_1.collidepoint((mx,my)):#if the mouse is collding with the boxes x and y
        pygame.draw.rect(screen,(100,100,100),button_1)#makes it grey
        draw_text("Lets Go!",(255,255,255), screen, button_1.x +25,button_1.y + 5)#drawiing the start text
        
        if click:#when clicked sends you to rocket minigame
          self.straight_to_mars = True
          r = Rocketgame()
          r.rocketGameRunning()
          

      if button_2.collidepoint((mx,my)):
        if click:
          game = Game()
          game.game()

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



#runs the main menu
main = Main_menu()
main.menu()
