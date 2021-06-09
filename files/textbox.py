import pygame
from files.main_menu import Main_menu

w_width = 600#window width
w_height = 400
WINDOW_SIZE = (w_width,w_height)
screen = pygame.display.set_mode((WINDOW_SIZE))#initate the screensize

class Textbox:
  def __init__(self):
    
    
    
    self.tb = pygame.image.load("tb little.png")#loads in the background picture
    self.tb_rect = (self.tb.get_rect(topleft = (50,20)))#makes the background hitbox so we know when you click out of it

    self.buy = pygame.image.load("BUY.png")
    self.buy_rect = (self.buy.get_rect(topleft = (300,60)))
    
    self.sold = pygame.image.load("SOLD.png")
    self.sold_rect = (self.sold.get_rect(topleft = (300,60)))
    self.is_sold = False
    self.rendertb = False
  
  def render(self):
    screen.blit(self.tb,self.tb_rect)#this is were the text is going to go
    draw_text("Jumpboost",(255,255,255),screen,150,60)
    
    if self.is_sold:
      screen.blit(self.sold,self.sold_rect)
      
    else:
      screen.blit(self.buy,self.buy_rect)
    
    


      
  def bigtextbox_render(self):#future proofing
    pass



  