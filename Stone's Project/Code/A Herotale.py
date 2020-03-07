import pygame
import os

#Colours

BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)
RED = (255,0,0)
GREEN = (51,204,51)
ORANGE = (255,153,0)
PURPLE = (102,0,51)
PINK = (255,0,255)
CYAN = (204,255,255)
DBLUE = (51,51,204)
DGREEN = (0,51,0)
LY = (255,255,204)
NICE = (204,204,255)

#Create Level
#Menu Creation
def CreateMenu(menu_list, button_list):

    herotale = Title() #Creates title
    menu_list.add(herotale) #Make it visible

    startButton = Button(1, 309, 93, 0, 595.5, 420) #Start
    button_list.add(startButton)
    menu_list.add(startButton)

    settingsButton = Button(2, 615, 93, 0, 442.5, 560) #Settings
    button_list.add(settingsButton)
    menu_list.add(settingsButton)

    tutorialButton = Button(3, 639, 93, 0, 430.5, 700) #Tutorial
    button_list.add(tutorialButton)
    menu_list.add(tutorialButton)

#endprocedure

#Save Files Creation
def CreateFile(file_list, button_list, item_list):

    #File 1
    fileBox1 = BlockClass(2, 333, 639, 163.5, 130.5) #File box 1
    file_list.add(fileBox1)

    select1 = Button(4, 161, 31, 1, 249.5, 680.5) #Select Button 1
    button_list.add(select1)
    file_list.add(select1)

    coin1 = ItemClass(1, 50, 50, 213.5, 200.5) #Coin etc 1
    file_list.add(coin1)
    item_list.add(coin1)

    heart1 = ItemClass(2, 50, 46, 213.5, 300.5)
    file_list.add(heart1)

    flag1 = ItemClass(3, 50, 50, 213.5, 400.5)
    file_list.add(flag1)

    #Open File 1
    f = open("Game_Files/File1.txt","r+") #Open file 1
    lines = f.readlines() #All data
    f.close() #Close

    WriteWords(0, lines[0], 293.5, 210, file_list, 3) #Coin1 number
    WriteWords(0, lines[1], 293.5, 310, file_list, 3) #Live1 number
    WriteWords(0, lines[2], 293.5, 410, file_list, 3) #Level1 number
    
    #File 2
    fileBox2 = BlockClass(2, 333, 639, 583.5, 130.5) #File box 2
    file_list.add(fileBox2)

    select2 = Button(4, 161, 31, 2, 669.5, 680.5) #Select Button 2
    button_list.add(select2)
    file_list.add(select2)

    coin2 = ItemClass(1, 50, 50, 633.5, 200.5) #Coin etc 2
    file_list.add(coin2)
    item_list.add(coin2)

    heart2 = ItemClass(2, 50, 46, 633.5, 300.5)
    file_list.add(heart2)

    flag2 = ItemClass(3, 50, 50, 633.5, 400.5)
    file_list.add(flag2)

    #Open File 2
    f = open("Game_Files/File2.txt","r+") #Open file 1
    lines = f.readlines() #All data
    f.close() #Close

    WriteWords(0, lines[0], 713.5, 210, file_list, 3) #Coin2 number
    WriteWords(0, lines[1], 713.5, 310, file_list, 3) #Live2 number
    WriteWords(0, lines[2], 713.5, 410, file_list, 3) #Level2 number
    
    #File 3
    fileBox3 = BlockClass(2, 333, 639, 1003.5, 130.5) #File box 3
    file_list.add(fileBox3)

    select3 = Button(4, 161, 31 ,3, 1089.5, 680.5) #Select Button 3
    button_list.add(select3)
    file_list.add(select3)

    coin3 = ItemClass(1, 50, 50, 1053.5, 200.5) #Coin etc 3
    file_list.add(coin3)
    item_list.add(coin3)

    heart3 = ItemClass(2, 50, 46, 1053.5, 300.5)
    file_list.add(heart3)

    flag3 = ItemClass(3, 50, 50, 1053.5, 400.5)
    file_list.add(flag3)

    #Open File 3
    f = open("Game_Files/File3.txt","r+") #Open file 1
    lines = f.readlines() #All data
    f.close() #Close

    WriteWords(0, lines[0], 1133.5, 210, file_list, 3) #Coin3 number
    WriteWords(0, lines[1], 1133.5, 310, file_list, 3) #Live3 number
    WriteWords(0, lines[2], 1133.5, 410, file_list, 3) #Level3 number

    #Back
    back = Button(5, 106, 31 ,0, 50, 820) #Back Button
    button_list.add(back)
    file_list.add(back)    

#endprocedure

#LevelOneCreation
def CreateLevelOne(player_list, block_list, levelOne_list, startEnd_list, playerAnimation_list):

    #Files
    f = open("Game_Files/Blocks.txt","r+") #Open platforms file
    nodes = f.readlines() #All platforms
    nodesNum = len(nodes) #Number of platforms
    f.close() #Close

    #Nodes
    for i in range(nodesNum): 
        
        line = nodes[i-2] #Skip the last line because it is empty

        #Type of Block
        typeOfBlock = int(line[0])
        #x position
        if line[1] == "0" and line[2] == "0": #If first two numbers are 0, than the number is the last two numbers (0030)
            xpos = int(str(line[3])+str(line[4]))
        elif line[1] == "0" and line[2] != "0": #If first number is 0, the number is the following three numbers (0300)
            xpos = int(str(line[2])+str(line[3])+str(line[4]))
        elif line[4] == str(0) and line[3] == str(0) and line[2] == str(0) and line[1] == str(0) : #If all numbers are 0, the number is (0)
            xpos = 0
        else: #If else, the number is just a four digit number (4300)
            xpos = int(str(line[1])+str(line[2])+str(line[3])+str(line[4]))
        #endif

        #y position
        if line[5] == str(0): #If first number is 0, the number is the last two numbers
            ypos = int(str(line[6])+str(line[7]))
        else:
            ypos = int(str(line[5])+str(line[6])+str(line[7]))
        #endif

        #width
        if line[8] == str(0): #If first number is 0, the number is the last two numbers
            width = int(str(line[9])+str(line[10]))
        else:
            width = int(str(line[8])+str(line[9])+str(line[10]))
        #endif

        #hieght
        if line[11] == str(0): #If first number is 0, the number is the last two numbers
            height = int(str(line[12])+str(line[13]))
        else:
            height = int(str(line[11])+str(line[12])+str(line[13]))
        #endif
                
        if line[0] == str(1): #If it is a normal block, create a normal platform

            block = BlockClass(typeOfBlock, width, height, xpos, ypos) #Creates a block with given width & height
            block_list.add(block) #Used for later collision
            levelOne_list.add(block) #Make it visible

        #endif

    #endfor

    ground = GroundClass(0, 800) #Creates ground
    levelOne_list.add(ground) #Make it visible

    startBlock = BlockClass(0, 10, 800, -10, 0)
    block_list.add(block)

    player = PlayerClass(50, 705)
    player_list.add(player)

    area = BlockClass(0, 717.5, 800, 0, 0)
    startEnd_list.add(area)

    animationPlayer = PlayerAnimation(player.rect.x, player.rect.y)
    playerAnimation_list.add(animationPlayer)
    levelOne_list.add(animationPlayer)
            
#endprocedure

#Menu Class ----------------------------------------------------------------------------------------

#Title
class Title(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        
        self.image = pygame.Surface([1250, 184])
        self.rect = self.image.get_rect() #Get the shape
        self.rect.x = 125 #Set pos
        self.rect.y = 100
        self.titleImage = [pygame.transform.scale(pygame.image.load('Game_Images/Text/GameTitle.png'), (1250, 184))]
        self.image = self.titleImage[0]
        
    #endprocedure

#endclass

#Button
class Button(pygame.sprite.Sprite):

    def __init__(self, imageNumber, width, height, number, x, y):
        super().__init__()
        
        self.image = pygame.Surface([width, height])
        self.rect = self.image.get_rect() #Get the shape
        self.imageNum = imageNumber
        self.num = number
        self.rect.x = x
        self.rect.y = y

        self.play = [pygame.transform.scale(pygame.image.load('Game_Images/Text/Play1.png'), (309, 93)), pygame.transform.scale(pygame.image.load('Game_Images/Text/Play2.png'), (309, 93))]
        self.set = [pygame.transform.scale(pygame.image.load('Game_Images/Text/Settings1.png'), (615, 93)), pygame.transform.scale(pygame.image.load('Game_Images/Text/Settings2.png'), (615, 93))]
        self.tutorial = [pygame.transform.scale(pygame.image.load('Game_Images/Text/Tutorial1.png'), (639, 93)), pygame.transform.scale(pygame.image.load('Game_Images/Text/Tutorial2.png'), (639, 93))]
        self.select = [pygame.transform.scale(pygame.image.load('Game_Images/Text/Select1.png'), (161, 31)), pygame.transform.scale(pygame.image.load('Game_Images/Text/Select2.png'), (161, 31))]
        self.back = [pygame.transform.scale(pygame.image.load('Game_Images/Text/Back1.png'), (106, 31)), pygame.transform.scale(pygame.image.load('Game_Images/Text/Back2.png'), (106, 31))]

        if self.imageNum == 1:

            self.image = self.play[0]

        elif self.imageNum == 2:

            self.image = self.set[0]

        elif self.imageNum == 3:

            self.image = self.tutorial[0]

        elif self.imageNum == 4:

            self.image = self.select[0]

        elif self.imageNum == 5:

            self.image = self.back[0]

        #endif
        
    #endprocedure

    def Change(self, pos, level):

        if level == 0 and pos[0] >= 595.5 and pos[1] >= 420 and pos[0] <= 904.5 and pos[1] <= 513 and self.imageNum == 1:
            
            self.image = self.play[1] #Hover on start button
            
        elif level == 0 and pos[0] >= 442.5 and pos[1] >= 560 and pos[0] <= 1057.5 and pos[1] <= 653 and self.imageNum == 2:
            
            self.image = self.set[1] #Hover on Settings
            
        elif level == 0 and pos[0] >= 430.5 and pos[1] >= 700 and pos[0] <= 1069.5 and pos[1] <= 793 and self.imageNum == 3:
            
            self.image = self.tutorial[1] #Hover on Tutorial

        elif level == 3 and pos[0] >= 249.5 and pos[1] >= 680.5 and pos[0] <= 410.5 and pos[1] <= 711.5 and self.imageNum == 4 and self.num == 1:
            
            self.image = self.select[1] #Hover on select file 1
            
        elif level == 3 and pos[0] >= 669.5 and pos[1] >= 680.5 and pos[0] <= 830.5 and pos[1] <= 711.5 and self.imageNum == 4 and self.num == 2:
            
            self.image = self.select[1] #Hover on select file 2

        elif level == 3 and pos[0] >= 1089.5 and pos[1] >= 680.5 and pos[0] <= 1250.5 and pos[1] <= 711.5 and self.imageNum == 4 and self.num == 3:
            
            self.image = self.select[1] #Hover on select file 3
            
        elif level == 3 and pos[0] >= 50 and pos[1] >= 820 and pos[0] <= 156 and pos[1] <= 851 and self.imageNum == 5:
            
            self.image = self.back[1] #Hover on back
            
        else:

            if self.imageNum == 1:

                self.image = self.play[0]

            elif self.imageNum == 2:

                self.image = self.set[0]

            elif self.imageNum == 3:

                self.image = self.tutorial[0]

            elif self.imageNum == 4:

                self.image = self.select[0]

            elif self.imageNum == 5:

                self.image = self.back[0]

            #endif

        #endif

    #endprocedure

#endclass

#Save Files Class
#Item Class
class ItemClass(pygame.sprite.Sprite):

    def __init__(self, typeOfItem, width, height, x, y):
        super().__init__()

        self.image = pygame.Surface([width,height])
        self.rect = self.image.get_rect() #Get the shape

        self.rect.x = x #Set position
        self.rect.y = y

        self.item = typeOfItem

        #Counters
        self.coinCounter = 0

        #Timers
        self.startAnimation = 0
        self.endAnimation = 0

        self.coins = [] #Numbers
        for x in range(5):
            add_str = str(x+1)
            if x < 10:
                self.coins.append(pygame.transform.scale(pygame.image.load("Game_Images/Object/Coins/Coin" + add_str + ".png"), (50, 50)))
            #endif
        #endfor

        self.hearts = [pygame.transform.scale(pygame.image.load("Game_Images/Object/Hearts/Heart.png"), (50, 46))] #Hearts
        self.flags = [pygame.transform.scale(pygame.image.load("Game_Images/Object/Flags/Flag.png"), (50, 50))] #Hearts

        if self.item == 1: #Set image

            self.image = self.coins[0]

        elif self.item == 2:

            self.image = self.hearts[0]

        elif self.item == 3:

            self.image = self.flags[0]

        #endif

    def Change(self):

        if self.startAnimation == 0: #If start timer has not started yet

            self.startAnimation = pygame.time.get_ticks() #Record current time

        #endif

        self.endAnimation = pygame.time.get_ticks() #Get current time for end time
        if self.endAnimation - self.startAnimation >= 120:

            self.startAnimation = self.endAnimation #Reset timer
            
            if self.item == 1:

                self.image = self.coins[self.coinCounter]
                if self.coinCounter == 4:
                    self.coinCounter = 0
                else:
                    self.coinCounter += 1
                #endif

            #endif

        #endif

    #endprocedure

#endclass

#Word
class WordClass(pygame.sprite.Sprite):

    def __init__(self, typeOfWord, wordNum, width, height, x, y):
        super().__init__()

        self.image = pygame.Surface([width,height])
        self.rect = self.image.get_rect() #Get the shape

        self.rect.x = x #Set position
        self.rect.y = y

        self.wordType = typeOfWord
        self.num = wordNum

        #Counters

        #Timers
        self.startAnimation = 0
        self.endAnimation = 0

        self.numbers = [] #Numbers
        for x in range(10):
            add_str = str(x)
            if x < 10:
                self.numbers.append(pygame.transform.scale(pygame.image.load("Game_Images/Object/Numbers/" + add_str + ".png"), (24, 31)))
            #endif
        #endfor

        if self.wordType == 0:
            
            self.image = self.numbers[int(self.num)]

        #endif

    #endprocedure

#endclass

#Write Words
def WriteWords(typeOfWord, line, x, y, file_list, level):

    line = line.rstrip("\n") #Get rid of next line (\n)
    length = len(str(line))
    for i in range(length): #Loop

        if typeOfWord == 0: #If type is number
            width = 24
            height = 31
            xIncrement = 29
            word = WordClass(0, line[i], width, height, x, y) #Create word
            x += xIncrement #Move Further
            
            if level == 3:
                file_list.add(word) #Add to list
            #endif
        #endif     

    #endfor

#endprocedure

#Gameplay Class ------------------------------------------------------------------------------------

#Block
class BlockClass(pygame.sprite.Sprite): #Block is a sprite, because I need to create multiple blocks
    
    def __init__(self, typeOfBlock, width, height, x, y):
        super().__init__()
        
        self.image = pygame.Surface([width,height])
        self.rect = self.image.get_rect() #Get the shape

        self.rect.x = x
        self.rect.y = y

        self.grassBlock = [pygame.transform.scale(pygame.image.load('Game_Images/Background/GroundBlock.png'), (240, 40))]
        self.saveFileBlock = [pygame.transform.scale(pygame.image.load('Game_Images/Text/SaveFileBox.png'), (333, 639))]

        if typeOfBlock == 1:

            self.image = self.grassBlock[0]

        elif typeOfBlock == 2:

            self.image = self.saveFileBlock[0]

        #endif
        
    #endprocedure

#endclass

#Ground
class GroundClass(pygame.sprite.Sprite): #Block is a sprite, because I need to create multiple blocks
    
    def __init__(self, x, y):
        super().__init__()
        
        self.image = pygame.Surface([1500,100])
        self.image.fill(DGREEN)
        self.rect = self.image.get_rect() #Get the shape

        self.rect.x = x
        self.rect.y = y
        
    #endprocedure

    def ChangeSkin(self):

        self.image = self.image #Changes the texture of itself

    #endprocedure

#endclass

#Player Class
class PlayerClass(pygame.sprite.Sprite): #Class of the player
 
    def __init__(self, x, y):
        
        super().__init__()
 
        self.image = pygame.Surface([65, 97])
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

        #Attributes
        self.horiSpeed = 0
        self.lastHoriSpeed = 0
        self.doubleJump = False
        self.vertSpeed = -0.4
        self.jumped = False
        self.doubleJumped = False
        self.attacked = False
        self.freeze = False

        #Timers
        self.endAnimation = 0
        self.startAnimation = 0

        #Counter
        self.idleCounter = 0
        self.runCounter = 0
        self.jumpCounter = 0
        self.fallCounter = 0
        
    #endprocedure

    def Animation(self, playerAnimation_list):

        if self.startAnimation == 0: #If start timer has not started yet

            self.startAnimation = pygame.time.get_ticks() #Record current time

        #endif

        for animationPlayer in playerAnimation_list:

            self.endAnimation = pygame.time.get_ticks() #Get current time for end time
            
            if self.attacked == False and self.horiSpeed == 0 and self.jumped == False:

                if self.idleCounter == 1 or self.idleCounter == 2 or self.idleCounter == 3:
                    animationPlayer.rect.y = self.rect.y - 3
                else:
                    animationPlayer.rect.y = self.rect.y
                #endif
                    
                if self.lastHoriSpeed > 0: #X position
                    animationPlayer.rect.x = self.rect.x - 47
                else:
                    animationPlayer.rect.x = self.rect.x
                #endif

                if self.endAnimation - self.startAnimation >= 160: #If next image
                    
                    self.startAnimation = self.endAnimation #If player is idle
                    animationPlayer.PlayerIdle(self.lastHoriSpeed, self.idleCounter)

                    if self.idleCounter != 7: #If reached the end
                        self.idleCounter += 1
                    else:
                        self.idleCounter = 0
                    #endif

                #endif

            elif self.attacked == False and self.horiSpeed != 0 and self.jumped == False:

                if self.lastHoriSpeed > 0: #X position
                    animationPlayer.rect.x = self.rect.x - 42
                else:
                    animationPlayer.rect.x = self.rect.x
                #endif
                    
                if self.runCounter == 1 or self.runCounter == 2 or self.runCounter == 6 or self.runCounter == 7 or self.runCounter == 9 or self.runCounter == 4:
                    animationPlayer.rect.y = self.rect.y - 5
                elif self.runCounter == 3 or self.runCounter == 8:
                    animationPlayer.rect.y = self.rect.y - 3
                elif self.runCounter == 0 or self.runCounter == 5:
                    animationPlayer.rect.y = self.rect.y
                #endif

                if self.endAnimation - self.startAnimation >= 80:
                    
                    self.startAnimation = self.endAnimation #If player running
                    animationPlayer.PlayerRun(self.lastHoriSpeed, self.runCounter)

                    if self.runCounter != 9: #If reached the end
                        self.runCounter += 1
                    else:
                        self.runCounter = 0
                    #endif

                #endif

            elif self.jumped == True and self.vertSpeed >= 0:

                if self.lastHoriSpeed > 0: #X position
                    animationPlayer.rect.x = self.rect.x - 40
                else:
                    animationPlayer.rect.x = self.rect.x
                #endif
                    
                animationPlayer.rect.y = self.rect.y

                if self.endAnimation - self.startAnimation >= 200:

                    self.startAnimation = self.endAnimation #If player jumping
                    animationPlayer.PlayerJump(self.lastHoriSpeed, self.jumpCounter)

                    if self.jumpCounter != 2: #If reached the end
                        self.jumpCounter += 1
                    else:
                        self.jumpCounter = 2 #Stay at the last frame
                    #endif

                #endif

            elif self.jumped == True and self.vertSpeed < 0:

                if self.lastHoriSpeed > 0: #X position
                    animationPlayer.rect.x = self.rect.x - 49
                else:
                    animationPlayer.rect.x = self.rect.x
                #endif
                    
                animationPlayer.rect.y = self.rect.y

                if self.endAnimation - self.startAnimation >= 200:

                    self.startAnimation = self.endAnimation #If player falling
                    animationPlayer.PlayerFall(self.lastHoriSpeed, self.fallCounter)

                    if self.fallCounter != 3: #If reached the end
                        self.fallCounter += 1
                    else:
                        self.fallCounter = 3 #Stay at the last frame
                    #endif

                #endif
                
            #endif

        #endfor

    #endprocedure

    def Jump(self):

        if self.freeze == False:

            if self.jumped == False: #If player has not jumped yet

                self.vertSpeed = 15
                self.jumped = True
                self.doubleJumped = False
                self.jumpCounter = 0
                self.fallCounter = 0

            elif self.jumped == True and self.doubleJumped == False: #If double jump

                self.vertSpeed = 12
                self.doubleJumped = True
                self.jumpCounter = 0
                self.fallCounter = 0

            #endif

        #endif

    #endprocedure

    def MoveVert(self, block_list):

        if self.freeze == False:

            if self.vertSpeed == 0: #Keep testing if player hits something
                self.vertSpeed = -0.4
            else: #Gravity
                self.vertSpeed -= 0.6
            #endif

            if self.rect.y >= 703 and self.vertSpeed <= 0: #If sinks into the ground

                self.rect.y = 703 #Stands on the ground
                self.vertSpeed = 0
                self.jumped = False

            elif self.rect.y <= 0 and self.vertSpeed > 0:

                self.rect.y = 0
                self.vertSpeed = 0

            #endif

            self.rect.y -= self.vertSpeed #Player move

            playerVertBlock_list = pygame.sprite.spritecollide(self, block_list, False)#If collide
            for block in playerVertBlock_list:
                
                if self.vertSpeed <= 0: #If player is falling

                    self.rect.bottom = block.rect.top
                    self.jumped = False

                elif self.vertSpeed >= 0: #If player is jumping

                    self.rect.top = block.rect.bottom

                #endif

                self.vertSpeed = 0 #Stop player

            #endfor

        #endif

    #endprocedure

    def ChangeSpeed(self,num):

        if self.freeze == False:

            if num == 0:

                self.horiSpeed = -8
                self.lastHoriSpeed = self.horiSpeed

            elif num == 1:

                self.horiSpeed = 8
                self.lastHoriSpeed = self.horiSpeed

            elif num == 2:

                self.horiSpeed = 0

            #endif

        #endif

    #endprocedure

    def MoveHori(self, centered, block_list, startEnd_list, player_list):

        if self.freeze == False:
            
            if centered == False: #If player is not required to be in the center, itself 
    #will move instead of the blocks
                self.rect.x += self.horiSpeed

                for block in block_list:
                            
                    if self.rect.colliderect(block.rect): #If player hit block
                        if self.horiSpeed > 0:
                            self.rect.right = block.rect.left
                        else:
                            self.rect.left = block.rect.right
                        #endif
                    #endif

                #endfor

                if self.rect.x <= 0: #If player reach the end of screen

                    self.rect.x = 0

                elif self.rect.x >= 1435:

                    self.rect.x = 1435

                #endif

            else: #If player placed in the center, the blocks move instead of the player

                for block in block_list:

                    block.rect.x -= self.horiSpeed
                    for area in startEnd_list:

                        area.rect.x -= self.horiSpeed

                    #endfor
                    
                    playerBlock_list = pygame.sprite.spritecollide(block, player_list, False)
                    for player in playerBlock_list:

                        for block in block_list:
                            
                            block.rect.x += self.horiSpeed

                            for area in startEnd_list:

                                area.rect.x += self.horiSpeed

                            #endfor

                        #endfor

                    #endif

                #endfor

            #endif

        #endif

    #endprocedure

#endclass

#Player Animation Class
class PlayerAnimation(pygame.sprite.Sprite): #Class of player's animation
 
    def __init__(self, x, y):
        
        super().__init__()
 
        self.image = pygame.Surface([65, 97])
        self.rect = self.image.get_rect()

        self.rect.x = x #Set pos
        self.rect.y = y

        #Animation
        self.playerIdle = [pygame.transform.scale(pygame.image.load('Game_Images/Player/IdlePlayer1.png'), (112, 100)), pygame.transform.scale(pygame.image.load('Game_Images/Player/IdlePlayer2.png'), (112, 100)), pygame.transform.scale(pygame.image.load('Game_Images/Player/IdlePlayer3.png'), (107, 100)), pygame.transform.scale(pygame.image.load('Game_Images/Player/IdlePlayer4.png'), (107, 100)), pygame.transform.scale(pygame.image.load('Game_Images/Player/IdlePlayer5.png'), (110, 97)), pygame.transform.scale(pygame.image.load('Game_Images/Player/IdlePlayer6.png'), (110, 97)), pygame.transform.scale(pygame.image.load('Game_Images/Player/IdlePlayer7.png'), (107, 97)), pygame.transform.scale(pygame.image.load('Game_Images/Player/IdlePlayer8.png'), (107, 97))]
        self.playerRun = [pygame.transform.scale(pygame.image.load('Game_Images/Player/PlayerRun1.png'), (105, 97)), pygame.transform.scale(pygame.image.load('Game_Images/Player/PlayerRun2.png'), (110, 100)), pygame.transform.scale(pygame.image.load('Game_Images/Player/PlayerRun3.png'), (112, 100)), pygame.transform.scale(pygame.image.load('Game_Images/Player/PlayerRun4.png'), (117, 102)), pygame.transform.scale(pygame.image.load('Game_Images/Player/PlayerRun5.png'), (112, 100)), pygame.transform.scale(pygame.image.load('Game_Images/Player/PlayerRun6.png'), (110, 97)), pygame.transform.scale(pygame.image.load('Game_Images/Player/PlayerRun7.png'), (112, 100)), pygame.transform.scale(pygame.image.load('Game_Images/Player/PlayerRun8.png'), (112, 100)), pygame.transform.scale(pygame.image.load('Game_Images/Player/PlayerRun9.png'), (117, 102)), pygame.transform.scale(pygame.image.load('Game_Images/Player/PlayerRun10.png'), (107, 100))]
        self.playerJump = [pygame.transform.scale(pygame.image.load('Game_Images/Player/PlayerJump1.png'), (105, 95)), pygame.transform.scale(pygame.image.load('Game_Images/Player/PlayerJump2.png'), (107, 92)), pygame.transform.scale(pygame.image.load('Game_Images/Player/PlayerJump3.png'), (107, 87))]
        self.playerFall = [pygame.transform.scale(pygame.image.load('Game_Images/Player/PlayerFall1.png'), (112, 97)), pygame.transform.scale(pygame.image.load('Game_Images/Player/PlayerFall2.png'), (112, 97)), pygame.transform.scale(pygame.image.load('Game_Images/Player/PlayerFall3.png'), (115, 97)), pygame.transform.scale(pygame.image.load('Game_Images/Player/PlayerFall4.png'), (112, 97))]
        
    #endprocedure

    def PlayerIdle(self, speed, i): #When player not moving

        if speed > 0:
            self.image = self.playerIdle[i] #Right
        else:
            self.image = pygame.transform.flip(self.playerIdle[i],1,0) #Left
        #endif

    #endprocedure

    def PlayerRun(self, speed, i):

        if speed > 0:
            self.image = self.playerRun[i]
        else:
            self.image = pygame.transform.flip(self.playerRun[i],1,0)
        #endif

    #endprocedure

    def PlayerJump(self, speed, i):

        if speed > 0:
            self.image = self.playerJump[i]
        else:
            self.image = pygame.transform.flip(self.playerJump[i],1,0)
        #endif

    #endprocedure

    def PlayerFall(self, speed, i):

        if speed > 0:
            self.image = self.playerFall[i]
        else:
            self.image = pygame.transform.flip(self.playerFall[i],1,0)
        #endif

    #endprocedure

#endclass
        
#Gameplay
def Game():

    game_over = False #Not finish
    
    clock = pygame.time.Clock()

    #Variables
    currentSpeed = 0
    centered = False
    level = 0

    block_list = pygame.sprite.Group() #Blocks list

    player_list = pygame.sprite.Group() #Player's list

    startEnd_list = pygame.sprite.Group() #The area determines the start and end of a level

    levelOne_list = pygame.sprite.Group() #All visible object lists in level one

    menu_list = pygame.sprite.Group() #All visible objects in menu

    file_list = pygame.sprite.Group() #All visible objects in file

    playerAnimation_list = pygame.sprite.Group() #Player's animation

    button_list = pygame.sprite.Group() #Buttons

    item_list = pygame.sprite.Group() #Group of items

    CreateFile(file_list, button_list, item_list)
    CreateLevelOne(player_list, block_list, levelOne_list, startEnd_list, playerAnimation_list) #Call create block function
    CreateMenu(menu_list, button_list)

    while not game_over:
        
    # -- User input and controls
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()#Track Mouse' Position
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.MOUSEBUTTONDOWN: #Mouse Click
                if level == 0 and pos[0] >= 595.5 and pos[1] >= 420 and pos[0] <= 904.5 and pos[1] <= 513: #Select save files
                    level = 3 #Start game
                elif level == 0 and pos[0] >= 442.5 and pos[1] >= 560 and pos[0] <= 1057.5 and pos[1] <= 653: #Select Settings
                    level = 1 #Settings
                elif level == 0 and pos[0] >= 430.5 and pos[1] >= 700 and pos[0] <= 1069.5 and pos[1] <= 793: #Select tutorial
                    level = 2 #Tutorial
                elif level == 3 and pos[0] >= 249.5 and pos[1] >= 700 and pos[0] <= 410.5 and pos[1] <= 731: #Select file 1
                    level = -1
                elif level == 3 and pos[0] >= 669.5 and pos[1] >= 700 and pos[0] <= 830.5 and pos[1] <= 731: #Select file 2
                    level = -1
                elif level == 3 and pos[0] >= 1089.5 and pos[1] >= 700 and pos[0] <= 1250.5 and pos[1] <= 731: #Select file 3
                    level = -1
                elif level == 3 and pos[0] >= 50 and pos[1] >= 820 and pos[0] <= 156 and pos[1] <= 851: #Go back to menu
                    level = 0
                #endif
            elif level >= 4 and event.type == pygame.KEYDOWN: #Press Key Down
                if event.key == pygame.K_w:
                    player.Jump()
                if event.key == pygame.K_a:
                    player.ChangeSpeed(0)
                    currentSpeed = -1
                if event.key == pygame.K_d:
                    player.ChangeSpeed(1)
                    currentSpeed = 1
                #endif
            elif level >= 4 and event.type == pygame.KEYUP: #Release Key
                if event.key == pygame.K_a and currentSpeed < 0:
                    player.ChangeSpeed(2)
                if event.key == pygame.K_d and currentSpeed > 0:
                    player.ChangeSpeed(2)
                #endif
            #endif
        #endfor

        if level == 0:

            screen.fill(BLACK)

            for button in button_list:
                
                button.Change(pos, level)

            #endfor

            menu_list.draw(screen) #Display all visible objects

        elif level == 3:

            screen.fill(BLACK)

            for button in button_list:

                button.Change(pos, level)

            #endfor

            for item in item_list:

                item.Change()

            #endfor

            file_list.draw(screen) #Display all visible objects

        elif level == 4:

            screen.fill(WHITE)

            #Player Movement
            for player in player_list:

                #Centered
                for area in startEnd_list:
                    playerStartEnd_list = pygame.sprite.spritecollide(area, player_list, False)
                    for player in playerStartEnd_list:

                        centered = False

                    #endfor
                #endfor

                #Horizontal Movement
                player.MoveHori(centered, block_list, startEnd_list, player_list) #Player move horizontally

                centered = True #Centered is true regardless of the situation, it will be verifies before next move

                #Vertical Movement
                player.MoveVert(block_list)

                #Animation
                player.Animation(playerAnimation_list)

            #endfor

            levelOne_list.draw(screen) #Display all visible objects

        #endif

        pygame.display.flip() #Flip the images

        clock.tick(60) #Tick

    #endwhile

#endprocedure

# -- Initialise PyGame
pygame.init()

# -- Blank Screen
size = (1500,900)
screen = pygame.display.set_mode(size)

# -- Title of new window/screen
pygame.display.set_caption("2D RPG Game")
    
### -- Game Loop

Game() #Calls game

pygame.quit()
