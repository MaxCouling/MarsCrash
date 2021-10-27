import pygame
from pygame import *
pygame.init()


title_font = pygame.font.Font("fonts/visitor1.ttf",40)
text_font = pygame.font.Font("fonts/visitor2.ttf",20)
WHITE = (0,0,0)
class Textbox:
  def __init__(self):
    w_width = 600#window width
    w_height = 400
    WINDOW_SIZE = (w_width,w_height)
    self.screen = pygame.display.set_mode((WINDOW_SIZE))#initate the screensize
    self.clock = pygame.time.Clock()
    
    self.tb = pygame.image.load("assets/tb little.png")#loads in the background picture
    self.tb_rect = (self.tb.get_rect(topleft = (100,15)))#makes the backgroud a rect

    
    
   
    
    
  
  def render(self,title,title_pos,title_colour,text,text_pos,text_colour,avatar,time):
    """This pops up the textbox and i can choose what to put in there, what avatar i want, text, title and how long it plays for.
    This has been very helpful with streamlining the dialog"""
    counter = 0
    while counter != time:
      counter += 1
      pygame.display.update()
      self.clock.tick(60)
      self.screen.blit(self.tb,self.tb_rect)#drawing the background, the textbox which is then going to be used for the text to be put on
      
      self.screen.blit( pygame.font.Font.render(title_font, str(title),1,title_colour),title_pos)#The title of the text going onto the screen
      self.blit_text(self.screen,text,text_pos,text_font,text_colour)
      self.screen.blit(avatar,(450,12))
    
    


      
  
  def blit_text(self, surface, text, pos, font,colour):
    """This method helps with multiple lines of text in pygame"""
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, colour)
            word_width, word_height = word_surface.get_size()
            
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.



  