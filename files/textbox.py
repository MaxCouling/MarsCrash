import pygame


w_width = 600#window width
w_height = 400
WINDOW_SIZE = (w_width,w_height)
screen = pygame.display.set_mode((WINDOW_SIZE))#initate the screensize
title_font = pygame.font.Font("fonts/visitor1.ttf",30)
text_font = pygame.font.Font("fonts/visitor2.ttf",20)
clock = pygame.time.Clock()
class Textbox:
  def __init__(self):
    
    
    
    self.tb = pygame.image.load("tb little.png")#loads in the background picture
    self.tb_rect = (self.tb.get_rect(topleft = (100,15)))#makes the backgroud a rect

    
    
   
    
    
  
  def render(self,title,title_pos,title_colour,text,text_pos,text_colour,avatar):
    
    screen.blit(self.tb,self.tb_rect)#drawing the background, the textbox which is then going to be used for the text to be put on
    print("hey")
    screen.blit( pygame.font.Font.render(title_font, str(title),1,title_colour),title_pos)#The title of the text going onto the screen
    screen.blit(pygame.font.Font.render(text_font, str(text),1,text_colour),text_pos)#the text under it
    screen.blit(avatar,(450,50))
    
    


      
  def bigtextbox_render(self):#future proofing
    pass



  