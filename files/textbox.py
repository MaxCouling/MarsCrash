import pygame
from pygame import *
pygame.init()


title_font = pygame.font.Font("fonts/visitor1.ttf",30)
text_font = pygame.font.Font("fonts/visitor2.ttf",20)

class Textbox:
  def __init__(self):
    w_width = 600#window width
    w_height = 400
    WINDOW_SIZE = (w_width,w_height)
    self.screen = pygame.display.set_mode((WINDOW_SIZE))#initate the screensize
    self.clock = pygame.time.Clock()
    
    self.tb = pygame.image.load("tb little.png")#loads in the background picture
    self.tb_rect = (self.tb.get_rect(topleft = (100,15)))#makes the backgroud a rect

    
    
   
    
    
  
  def render(self,title,title_pos,title_colour,text,text_pos,text_colour,avatar,time):
    counter = 0
    while counter != time:
      counter += 1
      pygame.display.update()
      self.clock.tick(60)
      self.screen.blit(self.tb,self.tb_rect)#drawing the background, the textbox which is then going to be used for the text to be put on
      
      self.screen.blit( pygame.font.Font.render(title_font, str(title),1,title_colour),title_pos)#The title of the text going onto the screen
      self.screen.blit(pygame.font.Font.render(text_font, str(text),1,text_colour),text_pos)#the text under it
      self.screen.blit(avatar,(450,12))
    
    


      
  def bigtextbox_render(self):#future proofing
    pass



  