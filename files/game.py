
import pygame
from pygame import *
import time
from files.player import Player
from files.ground import Ground
from files.background import Background
from files.mine import Mine
from files.water import Water
from files.textbox import Textbox
from files.crash import Crash
from files.camera import *
import sys
from pygame import mixer
pygame.init()
mixer.init()
Font = pygame.font.Font("fonts/visitor1.ttf",30)
WHITE = (255,255,255)
BLACK = (0,0,0)
YELLOW = (255,255,0)
RED = (255,0,0)
ROCKET_PRICE = 1
X_POWER,Y_POWER = 0,120
WINDOW_W, WINDOW_H = 600, 400
WINDOW_SIZE = WINDOW_W, WINDOW_H

class Game:
  def __init__(self):
    
    
    self.canvas = pygame.Surface((WINDOW_W*10,WINDOW_H))#setting the canvas
    self.window = pygame.display.set_mode(((WINDOW_SIZE)))#setting the window
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
   
    self.border = Border(self.camera, self.player)
    self.animationspeed = 0

    #setting up mine and other scene
    self.mine = Mine()
    self.water = Water()
    self.crash = Crash()#self.mine
    self.click_list = [self.mine,self.water,self.crash]#all the things in my game that can be clicked
    
    #terminal varibales
    #exit button
    self.exitbutton = pygame.Rect(30,30,50,50)

    #grey box on the inside
    self.whitebox = pygame.Rect(80,30,490,50)

    #different upgrade boxes
    self.rocket_upgrade_box = pygame.Rect(50,300,240,60)
    self.rocket_colour = (255,0,255)

    self.walking_upgrade_box = pygame.Rect(50,220,240,60)
    self.walking_colour = (0,255,0)

    self.mining_upgrade_box = pygame.Rect(50,140,240,60)
    self.mining_colour = (0,255,0)
    
    self.smelting_box = pygame.Rect(300,140,250,150)
    self.smelt_colour = (0,0,255)

    self.walking_price = 1
    self.mining_price = 1
    #items
    
    self.iron = 0
    self.iron_icon = pygame.image.load("assets\Iron.png")
    self.clicked = False
    self.smelting_price_ore = 10
    self.smelting_price_water = 10

    #power
    self.power_amount = 150
    self.power_outline = pygame.Rect(X_POWER,Y_POWER,200,50)
    self.power_icon = pygame.image.load("assets/power_symbol.png")
    self.power_level = pygame.Rect(X_POWER + 40 ,Y_POWER+12,self.power_amount,25)

    #upgrades
    self.mine_eff = 10 #drill efficenty, goes down as you upgrade it
    self.walking_eff = 0.08 #walking eff when you walk it takes power, so use it wisely!


    #winning condition

    self.rocket_rebuilt = False
    self.out_of_power = False

    #rocket
    self.rocket_image_rebuilt = pygame.transform.scale(pygame.image.load('assets/final_rocket.png'),(100,320))
    self.rebuilt_rocket_x,self.rebuilt_rocket_y = 300,0
    
    self.mouse_over_mine = False
    self.mouse_over_walk = False
    self.mouse_over_rocket = False
    self.mouse_over_smelt = False
    
  
  def game(self):
    #starting sequence with the basic instructions
    """Intro is the basic tutorial for the player, gives instructions and briefs them on power usage and the wearabouts of
    the ore and the water and tells them to come back to the crashsite if they want to fill back up with power"""
    intro = 0
    while intro < 6:
      self.canvas.fill(BLACK)
      if intro == 0:
        self.textbox.render("COMPUTER",(120,25),(255,255,255),"You have crash landed on MARS!",(120,65),(255,255,255),self.crash.avatar,1)
      if intro == 1:
        self.textbox.render("COMPUTER",(120,25),(255,255,255),"Lucky enough the ship has more than\nenough power to last until we can\nget out of here. \n\nBut how would we get out of this \ndesert planet?",(120,65),(255,255,255),self.crash.avatar,1)
      if intro == 2:
        self.textbox.render("COMPUTER",(120,25),(255,255,255),"You have a limited amount of power in \nyour suit, explore the surface of\nMars and find out what is out there.",(120,65),(255,255,255),self.crash.avatar,1)
      if intro == 3:
        self.textbox.render("COMPUTER",(120,25),(255,255,255),"My sources say that there is martian \nore and an ice deposit east of the \ncrash site.",(120,65),(255,255,255),self.crash.avatar,1)
      if intro == 4:
        self.textbox.render("COMPUTER",(120,25),(255,255,255),"Walking drains your battery, so does\nmining ore or extracting water\nfrom the ice.",(120,65),(255,255,255),self.crash.avatar,1)
      if intro == 5:
        self.textbox.render("COMPUTER",(120,25),(255,255,255),"Good luck astronaut!\n\nCome back to the crashed ship to fill \nyour battery up.",(120,65),(255,255,255),self.crash.avatar,1)
      
      
      
      for event in pygame.event.get():#exits the intro and moves onto the game
        if event.type == pygame.QUIT:
          sys.exit()
        if event.type == KEYDOWN or event.type == MOUSEBUTTONDOWN:#if the player clicks or presses any button on the keyboard it skips to the next slide
          intro +=1#goes onto the next textbox
    
    self.camera.setmethod(self.border)
    """Main loop where everything is drawn/blitted onto the screen, also holds the win and lose conditions."""
    mixer.music.load('assets/MainGameSongLoop.mp3')#music
    mixer.music.play(-1)
    while True:#main loop
      #setting framerate
      pygame.display.update()
      self.clock.tick(60)
      if self.out_of_power:#if you run out of power
        
        return#return to the 'Mars Crash'
      
      


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
      
      
      self.gravity_check()
      
      
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
      self.window.blit( pygame.font.Font.render(Font, str(self.mine.ore),1,(150,150,150)),(70,25))#the number blitting the screen
      self.window.blit(self.mine.icon,(25,25))#the icnon next to it
      
      #water icon
      self.window.blit( pygame.font.Font.render(Font, str(self.water.water),1,(150,150,150)),(70,75))#the number blitting onto the screen
      self.window.blit(self.water.icon,(25,75))

      #power bar
      pygame.draw.rect(self.window,BLACK,self.power_outline)
      pygame.draw.rect(self.window,YELLOW,self.power_level)
      self.window.blit(self.power_icon,(X_POWER,Y_POWER+5))#adding 5 to make th power symbol to go downa little on the screen as it was a bit too high before on the screen
      
      #losing power when walking
      self.power_level = pygame.Rect(X_POWER + 40 ,Y_POWER+12,self.power_amount,25)
      if self.player.running:
        self.power_amount -= self.walking_eff
        
      if self.crash.clicked:#takes the player to the terminal
        self.terminal()
      
      if self.rocket_rebuilt:#winning condition
        self.crash.image = pygame.image.load('assets/nothing.png')
        self.player.image = pygame.image.load('assets/nothing.png')
        self.window.blit(self.rocket_image_rebuilt,(self.rebuilt_rocket_x,self.rebuilt_rocket_y))
        self.rebuilt_rocket_y -= 1
        self.window.blit( pygame.font.Font.render(Font, ("YOU WIN!"),1,WHITE),(200,200))#the number blitting onto the screen
        if self.rebuilt_rocket_y == -320:#when the rocket has left the screen
          fade = pygame.Surface(WINDOW_SIZE)#sets the window size for the fade
          fade.fill(BLACK)#what colour the fade is going to be
          for alpha in range(0,100):#for loop that fades the screen
            fade.set_alpha(alpha)
            self.window.blit(fade, (0,0))
            pygame.display.update()
            pygame.time.delay(30)#delay per frame 
          sys.exit()
          
          
      else:#if the rocket is not gone, make the player go through its animation cycle and i dont want the camera to be able to move either
        #animation
        self.animationspeed += 1
        if self.animationspeed == 10:#this is so every 10 frames that the game is run, one frame of animation will play. If not the animation will play at 60fps and be very fast
          self.player.update()#playeranimation
          self.animationspeed = 0
        #camera scrolling function
        self.camera.scroll()
      
        

      if self.power_level.width <= 0:#if the power is 0 the player is out of power
        fade = pygame.Surface(WINDOW_SIZE)#sets the window size for the fade
        fade.fill(RED)#what colour the fade is going to be
        for alpha in range(0,100):#for loop that fades the screen
          fade.set_alpha(alpha)
          self.window.blit(fade, (0,0))
          pygame.display.update()
          pygame.time.delay(10)#delay per frame 
        
        
        
        self.out_of_power = True
      
      
        
      
      
    
      
  
  def gravity_check(self):
    """If the player y velocity is more than 0, it """
    hits = pygame.sprite.spritecollide(self.player ,self.groundgroup, False)
    if self.player.vel.y > 0:
      if hits:
        lowest = hits[0]#the first one in the list is the lowest
        if self.player.pos.y < lowest.rect.bottom:#if the player is touching the ground
          self.player.pos.y = lowest.rect.top +1#add one so it is above the ground
          self.player.vel.y = 0#set the verticle velocity to 0, it is on the ground now
          self.player.jumping = False#if player is touching the ground, it cannot be in the state of jump (duh)

  def jump(self):
    """First this function checks if the player is in contact with the cround, if hits = True and the player is
    not already jumping it sets self.player.jumping = True and moves the player vel up to the self.player.jump_height"""
    self.player.rect.x += 1
 
    # Check to see if payer is in contact with the ground
    hits = pygame.sprite.spritecollide(self.player, self.groundgroup, False)
     
    self.player.rect.x -= 1
 
    # If touching the ground, and not currently jumping, cause the player to jump.
    if hits and not self.player.jumping:
       self.player.jumping = True
       self.player.vel.y = -self.player.jump_height

  def mouse_is_over(self,obj):
    """This function was created as the inbuilt pygame .collidepoint was not working for some objects
    what it does is sees if the mouse is after the left most of the object, mouse before the right most part
    of the object, checks if the mouse is above the bottom of the image but below the top, this function works
    as I also have the camera offset in the function."""
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


  
  def click(self):
    """method that will keep track of what to do when the player clicks somewhere on the screen"""
    #getting the mouse position
    for obj in self.click_list:
      if self.mouse_is_over(obj):
        #if the object isn't the crashsite take power away 
        if obj != self.click_list[2]:
          self.power_amount -= self.mine_eff
        obj.on_click()
  
  def terminal(self):
    """This method is used when the player clicks the crashsite, 
    this will be able to regenerate his power and he will be able 
    to make upgrades to his suit, drilling and eventually fix his ship"""
    self.power_amount = 145
    running =  True
    click = False
    while running:
        
        pygame.display.update()
        
        self.clock.tick(60)
        self.window.fill(BLACK)#background colour
        mx, my = pygame.mouse.get_pos()#gets the mouse postion. mx is mouse x and mouse y is mouse y postion on the screen
        self.mouse_over_mine = False
        self.mouse_over_walk = False
        self.mouse_over_rocket = False
        self.mouse_over_smelt = False    
        #EXIT BUTTON
        pygame.draw.rect(self.window,(70,70,70),pygame.Rect(30,30,540,340))
        pygame.draw.rect(self.window,(255,0,0),self.exitbutton)
        self.window.blit(pygame.font.Font.render(Font, "X",1,WHITE),(47,40))
        #inventory display
        pygame.draw.rect(self.window,WHITE,self.whitebox)
        """Pricing system, logic to checck if the player has the right materials fot the upgrade, then gives the upgrade and takes away the materials after"""
        if self.exitbutton.collidepoint((mx,my)):#if the player's mouse is over the exit button
          if click:#and then they click
            self.crash.clicked = False#exit the terminal
            running = False
        
        if self.rocket_upgrade_box.collidepoint((mx,my)):
          self.mouse_over_rocket = True
          if click and self.iron >= ROCKET_PRICE:
          
            self.rocket_rebuilt = True
            self.iron -= ROCKET_PRICE
        
        if self.mining_upgrade_box.collidepoint((mx,my)):
          self.mouse_over_mine = True
          if click and self.water.water >= self.mining_price: 
            self.water.water -= self.mining_price
            self.mining_price *= 2#increasese the price by two
            self.mine_eff /=2#increases the efficency by two
          
          
          
        if self.walking_upgrade_box.collidepoint((mx,my)):
          self.mouse_over_walk = True
          if click and self.mine.ore >= self.walking_price:
            self.mine.ore -= self.walking_price
            self.walking_price *= 3 #times the price by three
            self.walking_eff /= 1.5 #increase the effeicency by 1.5


        if self.smelting_box.collidepoint((mx,my)):
          self.mouse_over_smelt = True
          if click and self.mine.ore >= self.smelting_price_ore and self.water.water >= self.smelting_price_water:
            self.mine.ore -= self.smelting_price_ore
            self.water.water -= self.smelting_price_ore
            self.iron +=1
        
        """Change colour of the upgrades depending if the mouse is on them or not"""
        if self.mouse_over_mine:
          self.mining_colour = (0,255,150)
        else:
          self.mining_colour = (0,255,0)
        
        if self.mouse_over_walk:
          self.walking_colour = (0,255,150)
        else:
          self.walking_colour = (0,255,0)
        
        if self.mouse_over_rocket:
          self.rocket_colour = (255,100,255)
        else:
          self.rocket_colour = (255,0,255)
        
        if self.mouse_over_smelt:
          self.smelt_colour = (100,0,255)
        else:
          self.smelt_colour = (0,0,255)


        
        
        
        
        """Icons at the top of the screen"""
        #ore
        self.window.blit( pygame.font.Font.render(Font, str(self.mine.ore),1,BLACK),(120,40))#ore number
        self.window.blit(self.mine.icon,(83,40))
        #water
        self.window.blit(pygame.font.Font.render(Font, str(self.water.water),1,BLACK),(193,40))
        self.window.blit(self.water.icon,(160,40))
        #Iron
        self.window.blit(pygame.font.Font.render(Font, str(self.iron),1,BLACK),(266,40))
        self.window.blit(self.iron_icon,(225,37))

        """Below are the boxes for the upgrades, you will not be able to purchase them if you do not have the right materials"""
        #Rcoket upgrade
        pygame.draw.rect(self.window,self.rocket_colour,self.rocket_upgrade_box)
        self.window.blit(pygame.font.Font.render(Font,"BUILD ROCKET",2,BLACK),(self.rocket_upgrade_box.x+15,self.rocket_upgrade_box.y))
        self.window.blit(pygame.font.Font.render(Font, str(ROCKET_PRICE),1 ,BLACK),(self.rocket_upgrade_box.x + 55,self.rocket_upgrade_box.y + 25))
        self.window.blit(self.iron_icon,(self.rocket_upgrade_box.x + 15,self.rocket_upgrade_box.y + 25))
        #walking upgrade
        pygame.draw.rect(self.window,self.mining_colour,self.mining_upgrade_box)
        self.window.blit(pygame.font.Font.render(Font,"MINE SKILL",2,BLACK),(self.mining_upgrade_box.x+15,self.mining_upgrade_box.y))#name of upgrade
        self.window.blit(pygame.font.Font.render(Font, str(self.mining_price),1 ,BLACK),(self.mining_upgrade_box.x + 55,self.mining_upgrade_box.y + 25))#price of upgrade
        self.window.blit(self.water.icon,(self.mining_upgrade_box.x + 15,self.mining_upgrade_box.y + 25))#icon next to price
        #mining upgrade
        pygame.draw.rect(self.window,self.walking_colour,self.walking_upgrade_box)
        self.window.blit(pygame.font.Font.render(Font,"WALK SKILL",2,BLACK),(self.walking_upgrade_box.x+15,self.walking_upgrade_box.y))
        self.window.blit(pygame.font.Font.render(Font, str(self.walking_price),1 ,BLACK),(self.walking_upgrade_box.x + 55,self.walking_upgrade_box.y + 25))
        self.window.blit(self.mine.icon,(self.walking_upgrade_box.x + 15,self.walking_upgrade_box.y + 25))

        """Smelting, turning rock and water into iron which you use for the upgrades and building the rocket"""
        pygame.draw.rect(self.window,self.smelt_colour,self.smelting_box)
        #the title
        self.window.blit(pygame.font.Font.render(Font,"SMELTING ORE",2,WHITE),(self.smelting_box.x+15,self.smelting_box.y))
        #rock price to smelt
        self.window.blit(self.mine.icon,(self.smelting_box.x + 15,self.smelting_box.y + 25))
        self.window.blit(pygame.font.Font.render(Font, str(self.smelting_price_ore),1 ,WHITE),(self.smelting_box.x + 55,self.smelting_box.y + 25))
        #water price to smelt
        self.window.blit(self.water.icon,(self.smelting_box.x + 15,self.smelting_box.y + 65))
        self.window.blit(pygame.font.Font.render(Font, str(self.smelting_price_water),1 ,WHITE),(self.smelting_box.x + 55,self.smelting_box.y + 65))
        #equals sign
        self.window.blit(pygame.font.Font.render(Font, "=",1 ,WHITE),(self.smelting_box.x + 95,self.smelting_box.y + 40))
        #how much iron you will get per smelt
        self.window.blit(self.iron_icon,(self.smelting_box.x + 120,self.smelting_box.y + 35))
        self.window.blit(pygame.font.Font.render(Font, "1",1,WHITE),(self.smelting_box.x + 160,self.smelting_box.y + 40))



        
        
        
        
        

          


        #setting click back to false
        click = False
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
      
      


    
    
    
  