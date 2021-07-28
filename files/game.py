import pygame
from pygame import *
from files.player import Player
from files.ground import Ground
from files.background import Background
from files.mine import Mine
from files.water import Water
from files.textbox import Textbox
from files.crash import Crash
from files.camera import *
import sys

pygame.init()

myFont = pygame.font.Font("fonts/visitor1.ttf",30)






class Game:
  def __init__(self):
    
    WINDOW_W, WINDOW_H = 600, 400
    self.canvas = pygame.Surface((WINDOW_W*10,WINDOW_H))#setting the canvas
    self.window = pygame.display.set_mode(((WINDOW_W,WINDOW_H)))#setting the window
    self.clock = pygame.time.Clock()#pygame clock
    
    
    
    #loading player, scenes and self.
    self.player = Player()
    self.groundgroup = pygame.sprite.Group()

    for i in range(0,4000, 600):#this is making the ground tile
      g = Ground(i, 280)
      self.groundgroup.add(g)

    self.background = Background()
    self.textbox = Textbox()
    self.camera = Camera(self.player)
   # auto = Auto(self.camera,self.player)#its called borderself.
    self.follow = Follow(self.camera, self.player)
    self.animationspeed = 0

    #setting up mine and other scene
    self.mine = Mine(1400,155)
    self.water = Water(2400,235)
    self.crash = Crash(400,155)
    self.click_list = [self.mine,self.water,self.crash]#all the things in my game that can be clicked
    
    
    
    
  
  def game(self):
    self.camera.setmethod(self.follow)
    while True:#main loop
      #setting framerate
      pygame.display.update()
      self.clock.tick(60)
     
      #key inputs
      for event in pygame.event.get():#exits the game 
        if event.type == pygame.QUIT:
          sys.exit()
        if event.type == KEYDOWN:
          if event.key == K_SPACE:
            self.jump()
          
          

        if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
          self.click()
        

      self.canvas.fill((255,169,120))#background colour
      
      #updating and animating sprites
      self.player.move()#uses the player move funciton
      
      #animation 
      self.animationspeed += 1
      if self.animationspeed == 10:#this is so every 10 frames that the game is run, one frame of animation will play. If not the animation will play at 60fps and be very fast
        self.player.update()#playeranimation
        self.animationspeed = 0
      
      self.gravity_check()
      self.camera.scroll()
      
      #--updating window and display--
      
      #rendering the background
      
      self.canvas.blit(self.background.mountains0, (self.background.mountains0X - (self.camera.offset.x/5), self.background.mountains0Y - (self.camera.offset.y/5)))
      self.canvas.blit(self.background.mountains1, (self.background.mountains1X - (self.camera.offset.x/3), self.background.mountains1Y - (self.camera.offset.y/3)))
      self.canvas.blit(self.background.mountains2, (self.background.mountains2X - (self.camera.offset.x/2), self.background.mountains2Y - (self.camera.offset.y/2)))
      
      
      #blitiing the ground
      for ground in self.groundgroup:
        self.canvas.blit(ground.image,(ground.rect.x - self.camera.offset.x, ground.rect.y - self.camera.offset.y))

      #--blitting the setting--
      #The mine
      self.canvas.blit(self.mine.image,(self.mine.rect.x- self.camera.offset.x, self.mine.rect.y - self.camera.offset.y))
      #The ice
      self.canvas.blit(self.water.image,(self.water.rect.x - self.camera.offset.x, self.water.rect.y - self.camera.offset.y))
      #The crashsite
      self.canvas.blit(self.crash.image,(self.crash.rect.x - self.camera.offset.x, self.crash.rect.y - self.camera.offset.y))

      #--blitting the player--
      self.canvas.blit(self.player.image,(self.player.rect.x- self.camera.offset.x, self.player.rect.y - self.camera.offset.y))
      
      
      
      #blitting the game to window
      self.window.blit(self.canvas, (0,0))

      #textbox blitting/rendering
      
      
      #--blitting Icons, this is after the stuff in the game as the icons for health and stuff won't move inside the game--
      
      #mine icon
      self.window.blit( pygame.font.Font.render(myFont, str(self.mine.ore),1,(150,150,150)),(70,25))#the number blitting the screen
      self.window.blit(self.mine.icon,(25,25))#the icnon next to it
      
      #water icon
      self.window.blit( pygame.font.Font.render(myFont, str(self.water.water),1,(150,150,150)),(70,75))#the number blitting onto the screen
      self.window.blit(self.water.icon,(25,75))
      
        

      
      
      
    
      
  
  def gravity_check(self):
    
    hits = pygame.sprite.spritecollide(self.player ,self.groundgroup, False)
    if self.player.vel.y > 0:
      if hits:
        lowest = hits[0]#the first one in the list is the lowest
        if self.player.pos.y < lowest.rect.bottom:#if the player is touching the ground
          self.player.pos.y = lowest.rect.top +1#add one so it is above the ground
          self.player.vel.y = 0#set the verticle velocity to 0, it is on the ground now
          self.player.jumping = False#if player is touching the ground, it cannot be in the state of jump (duh)

  def jump(self):
    self.player.rect.x += 1
 
    # Check to see if payer is in contact with the ground
    hits = pygame.sprite.spritecollide(self.player, self.groundgroup, False)
     
    self.player.rect.x -= 1
 
    # If touching the ground, and not currently jumping, cause the player to jump.
    if hits and not self.player.jumping:
       self.player.jumping = True
       self.player.vel.y = -self.player.jump_height

  def mouse_is_over(self,obj):
    
    mouse_x,mouse_y = pygame.mouse.get_pos()
    #this is to deterimine if the mouse is over the object or not
    obj_left = obj.rect.x- self.camera.offset.x
    obj_right = obj.rect.x- self.camera.offset.x + obj.width
    obj_top = obj.rect.y - self.camera.offset.y
    obj_bottom = obj.rect.y - self.camera.offset.y + obj.height
    if obj_left <= mouse_x <= obj_right and obj_top <= mouse_y <= obj_bottom:#basically saying if the mouse is within the object, return true
      return True
    else:
      return False


  
  def click(self,):
    #method that will keep track of what to do when the player clicks somewhere on the screen
    #getting the mouse position
    for obj in self.click_list:
      if self.mouse_is_over(obj):
        obj.on_click()
  
  
    
    
    
    
        


      
    
       
      
