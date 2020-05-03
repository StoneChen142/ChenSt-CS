import pygame
import os
#from pydub import *
from decimal import *
from random import randint

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
#Loading Creation
def CreateLoad(loading_list):

    #Loading
    loading = LoadingClass()
    loading_list.add(loading)

#endprocedure

#Pause Panel Creation
def CreatePause(button_list, optionBlock_list, pauseButton_list, panelButton_list, levelOne_list, levelTwo_list, levelThree_list):

    pauseButton = Button(8, 60, 60, 0, 1430, 10) #Pause
    pauseButton_list.add(pauseButton)
    button_list.add(pauseButton)
    levelOne_list.add(pauseButton)
    levelTwo_list.add(pauseButton)
    levelThree_list.add(pauseButton)

    closeButton = Button(10, 60, 60, 0, 1068, 234) #Pause
    button_list.add(closeButton)
    panelButton_list.add(closeButton)

    quitButton = Button(11, 100, 40, 0, 700, 530)
    button_list.add(quitButton)
    panelButton_list.add(quitButton)

    optionBox = BlockClass(6, 800, 475, 350, 212) #Option box
    optionBlock_list.add(optionBox)

    quitInstruction = InstructionClass(10, 698, 77, 401, 362) #Instruction
    optionBlock_list.add(quitInstruction)

#endprocedure

#Characters
def CreateCharacters1(player_list, playerAttack_list, tutorialEnemy_list, tutorial_list, levelOne_list, levelTwo_list, levelThree_list, enemyAttack_list, character1_list):

    player = PlayerClass(50, 700, playerAttack_list)
    player_list.add(player)
    character1_list.add(player)

    dummy = BanditClass(1, 295, 250, tutorial_list, enemyAttack_list)
    tutorialEnemy_list.add(dummy) #Specify Level
    character1_list.add(dummy)

#endprocedure

def CreateCharacters2(levelOne_list, enemy_list, warlock_list, wordBox_list, nextButton_list, rogue_list, enemyAttack_list, rogueAttack_list, banditGroup1_list, banditGroup2_list, character1_list):

    warlock = WarlockClass(150,730,levelOne_list)
    warlock_list.add(warlock)
    character1_list.add(warlock)

    wordbox = BlockClass(5, 1065, 150, 217.5, 750)
    wordBox_list.add(wordbox)

    nextButton = Button(9, 60, 20, 0, 1195, 850)
    nextButton_list.add(nextButton)

    rogue = RogueClass(2260, 710, levelOne_list, enemyAttack_list, rogueAttack_list)
    rogue_list.add(rogue)
    character1_list.add(rogue)

    for i in range(3):
        bandit = BanditClass(1, 2140+i*100, 700, levelOne_list, enemyAttack_list)
        banditGroup1_list.add(bandit) #Specify Level
        character1_list.add(bandit)
    #endfor

    bandit1 = BanditClass(1, 1670, 450, levelOne_list, enemyAttack_list)
    bandit2 = BanditClass(1, 1780, 450, levelOne_list, enemyAttack_list)
    bandit3 = BanditClass(1, 2670, 450, levelOne_list, enemyAttack_list)
    bandit4 = BanditClass(1, 2780, 450, levelOne_list, enemyAttack_list)
    bandit5 = BanditClass(1, 2170, 700, levelOne_list, enemyAttack_list)
    bandit6 = BanditClass(1, 2280, 700, levelOne_list, enemyAttack_list)
    banditGroup2_list.add(bandit1, bandit2, bandit3, bandit4, bandit5, bandit6)
    character1_list.add(bandit1, bandit2, bandit3, bandit4, bandit5, bandit6)

#endprocedure

#Currency Creation
def CreateMoney(tutorial_list, levelOne_list, levelTwo_list, levelThree_list, thousand_list, hundred_list, ten_list, one_list):

    coin = ItemClass(1, 50, 50, 15, 10, 2)
    tutorial_list.add(coin)
    levelOne_list.add(coin)
    levelTwo_list.add(coin)
    levelThree_list.add(coin)

    thousand = WordClass(0, 0, 24, 31, 85, 20)
    thousand_list.add(thousand)
    tutorial_list.add(thousand)
    levelOne_list.add(thousand)
    levelTwo_list.add(thousand)
    levelThree_list.add(thousand)

    hundred = WordClass(0, 0, 24, 31, 115, 20)
    hundred_list.add(hundred)
    tutorial_list.add(hundred)
    levelOne_list.add(hundred)
    levelTwo_list.add(hundred)
    levelThree_list.add(hundred)

    ten = WordClass(0, 0, 24, 31, 145, 20)
    ten_list.add(ten)
    tutorial_list.add(ten)
    levelOne_list.add(ten)
    levelTwo_list.add(ten)
    levelThree_list.add(ten)

    one = WordClass(0, 0, 24, 31, 175, 20)
    one_list.add(one)
    tutorial_list.add(one)
    levelOne_list.add(one)
    levelTwo_list.add(one)
    levelThree_list.add(one)

#endprocedure
    
#Menu Creation
def CreateMenu(menu_list, button_list):

    herotale = Title() #Creates title
    menu_list.add(herotale) #Make it visible

    #Start
    startButton = Button(1, 309, 93, 0, 595.5, 420)
    button_list.add(startButton)
    menu_list.add(startButton)

    settingsButton = Button(2, 615, 93, 0, 442.5, 560) #Settings
    button_list.add(settingsButton)
    menu_list.add(settingsButton)

    tutorialButton = Button(3, 639, 93, 0, 430.5, 700) #Tutorial
    button_list.add(tutorialButton)
    menu_list.add(tutorialButton)

#endprocedure

#Setting Creation
def CreateSettings(setting_list, button_list, easy_list, hard_list):

    easy = Button(6, 411, 120, 0, 544.5, 250) #Easy Button
    easy_list.add(easy)
    setting_list.add(easy)
    button_list.add(easy)

    hard = Button(7, 441, 120, 0, 529.5, 250) #Hard Button
    hard_list.add(hard)
    button_list.add(hard)

    #Back
    back = Button(5, 106, 31 ,0, 50, 820) #Back Button
    button_list.add(back)
    setting_list.add(back)

    #Text
    chooseDiff = BlockClass(4, 1220, 202, 140, 480)
    setting_list.add(chooseDiff)

#endprocedure

def RemoveFile(file_list):

    for item in file_list:

        file_list.remove(item)

    #endfor

#endprocedure

#Save Files Creation
def CreateFile(file_list, button_list, item_list, crown_list):

    #File 1
    fileBox1 = BlockClass(2, 333, 639, 163.5, 130.5) #File box 1
    file_list.add(fileBox1)

    select1 = Button(4, 161, 31, 1, 249.5, 680.5) #Select Button 1
    button_list.add(select1)
    file_list.add(select1)

    coin1 = ItemClass(1, 50, 50, 213.5, 200.5, 3) #Coin etc 1
    file_list.add(coin1)
    item_list.add(coin1)

    heart1 = ItemClass(2, 50, 50, 213.5, 300.5, 3)
    file_list.add(heart1)

    flag1 = ItemClass(3, 50, 50, 213.5, 400.5, 3)
    file_list.add(flag1)

    #Open File 1
    f = open("Game_Files/File1.txt","r+") #Open file 1
    lines = f.readlines() #All data
    f.close() #Close

    WriteWords(0, lines[0], 293.5, 210, file_list, crown_list, crown_list, crown_list, crown_list, 3, 0, 0) #Coin1 number
    WriteWords(0, lines[1], 293.5, 310, file_list, crown_list, crown_list, crown_list, crown_list, 3, 0, 0) #Live1 number
    WriteWords(0, lines[2], 293.5, 410, file_list, crown_list, crown_list, crown_list, crown_list, 3, 0, 0) #Level1 number
    
    #File 2
    fileBox2 = BlockClass(2, 333, 639, 583.5, 130.5) #File box 2
    file_list.add(fileBox2)

    select2 = Button(4, 161, 31, 2, 669.5, 680.5) #Select Button 2
    button_list.add(select2)
    file_list.add(select2)

    coin2 = ItemClass(1, 50, 50, 633.5, 200.5, 3) #Coin etc 2
    file_list.add(coin2)
    item_list.add(coin2)

    heart2 = ItemClass(2, 50, 50, 633.5, 300.5, 3)
    file_list.add(heart2)

    flag2 = ItemClass(3, 50, 50, 633.5, 400.5, 3)
    file_list.add(flag2)

    #Open File 2
    f = open("Game_Files/File2.txt","r+") #Open file 2
    lines = f.readlines() #All data
    f.close() #Close

    WriteWords(0, lines[0], 713.5, 210, file_list, crown_list, crown_list, crown_list, crown_list, 3, 0, 0) #Coin2 number
    WriteWords(0, lines[1], 713.5, 310, file_list, crown_list, crown_list, crown_list, crown_list, 3, 0, 0) #Live2 number
    WriteWords(0, lines[2], 713.5, 410, file_list, crown_list, crown_list, crown_list, crown_list, 3, 0, 0) #Level2 number
    
    #File 3
    fileBox3 = BlockClass(2, 333, 639, 1003.5, 130.5) #File box 3
    file_list.add(fileBox3)

    select3 = Button(4, 161, 31 ,3, 1089.5, 680.5) #Select Button 3
    button_list.add(select3)
    file_list.add(select3)

    coin3 = ItemClass(1, 50, 50, 1053.5, 200.5, 3) #Coin etc 3
    file_list.add(coin3)
    item_list.add(coin3)

    heart3 = ItemClass(2, 50, 50, 1053.5, 300.5, 3)
    file_list.add(heart3)

    flag3 = ItemClass(3, 50, 50, 1053.5, 400.5, 3)
    file_list.add(flag3)

    #Open File 3
    f = open("Game_Files/File3.txt","r+") #Open file 3
    lines = f.readlines() #All data
    f.close() #Close

    WriteWords(0, lines[0], 1133.5, 210, file_list, crown_list, crown_list, crown_list, crown_list, 3, 0, 0) #Coin3 number
    WriteWords(0, lines[1], 1133.5, 310, file_list, crown_list, crown_list, crown_list, crown_list, 3, 0, 0) #Live3 number
    WriteWords(0, lines[2], 1133.5, 410, file_list, crown_list, crown_list, crown_list, crown_list, 3, 0, 0) #Level3 number

    #Back
    back = Button(5, 106, 31 ,0, 50, 820) #Back Button
    button_list.add(back)
    file_list.add(back)

    #Crown
    crown = BlockClass(3, 333, 140.5, 163.5, 7.5) #Crown
    file_list.add(crown)
    crown_list.add(crown)

    SetCrown(crown_list)

#endprocedure

#LevelOneCreation
def CreateTutorialPlatform(tutorialBlock_list, tutorial_list, button_list):

    #Files
    f = open("Game_Files/Tutorial.txt","r+") #Open platforms file
    nodes = f.readlines() #All platforms
    nodesNum = len(nodes) #Number of platforms
    f.close() #Close

    mountain1 = BackgroundClass(1, 0, 2560, 800, 0, 0)
    mountain2 = BackgroundClass(1, 1, 2560, 800, 0, 0)
    cloud1 = BackgroundClass(1, 2, 2560, 800, 0, 0)
    cloud2 = BackgroundClass(1, 3, 2560, 800, 0, 0)

    tutorial_list.add(cloud2, cloud1, mountain2, mountain1)

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
            tutorialBlock_list.add(block) #Used for later collision
            tutorial_list.add(block) #Make it visible

        #endif

    #endfor

    ground = GroundClass(1, 0, 800) #Creates ground
    tutorial_list.add(ground) #Make it visible

    startBlock = BlockClass(0, 10, 800, -10, 0)
    tutorialBlock_list.add(block)

    moveInstruction = InstructionClass(1, 439, 27, 40, 670)
    jumpInstruction = InstructionClass(2, 210, 25, 810, 670)
    attackInstruction = InstructionClass(3, 289, 25, 175.5, 200)
    rollInstruction = InstructionClass(4, 230, 20, 1105, 330)
    dJumpInstruction = InstructionClass(5, 305, 25, 760, 580)
    blockInstruction = InstructionClass(6, 189, 20, 225.5, 120)
    coinInstruction = InstructionClass(8, 487, 27, 240, 26)
    fakeInstruction = InstructionClass(9, 354, 20, 18, 65)
    tutorial_list.add(moveInstruction, jumpInstruction, attackInstruction, rollInstruction, dJumpInstruction, blockInstruction, coinInstruction, fakeInstruction)

    closeButton1 = Button(10, 60, 60, 0, 1430, 10) #Pause
    button_list.add(closeButton1)
    tutorial_list.add(closeButton1)
            
#endprocedure

#LevelOneCreation
def CreateLevelOnePlatform(block1_list, levelOne_list, startEnd_list, background1_list, cloud_list, ground1_list):

    #Files
    f = open("Game_Files/Level1Platform.txt","r+") #Open platforms file
    nodes = f.readlines() #All platforms
    nodesNum = len(nodes) #Number of platforms
    f.close() #Close

    back1 = BackgroundClass(1, 0, 2560, 800, 0, 0)
    back2 = BackgroundClass(1, 1, 2560, 800, 0, 0)
    back3 = BackgroundClass(1, 2, 2560, 800, 0, 0)
    back4 = BackgroundClass(1, 3, 2560, 800, 0, 0)
    back5 = BackgroundClass(1, 2, 2560, 800, 2560, 0)
    back6 = BackgroundClass(1, 3, 2560, 800, 2560, 0)

    background1_list.add(back1,back2)
    cloud_list.add(back3, back4, back5, back6)
    levelOne_list.add(back4, back6, back3, back5, back2, back1)

    #Nodes
    for i in range(nodesNum): 
        
        line = nodes[i] #Skip the last line because it is empty

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
            block1_list.add(block) #Used for later collision
            levelOne_list.add(block) #Make it visible

        #endif

    #endfor

    ground = GroundClass(1, 0, 800) #Creates ground
    ground1_list.add(ground)
    levelOne_list.add(ground) #Make it visible

    startBlock = BlockClass(0, 10, 800, -10, 0)
    block1_list.add(block)

    area = BlockClass(0, 1500, 800, 0, 0)
    startEnd_list.add(area)
            
#endprocedure

def ReadScript(script1, script2, script3):

    f = open("Game_Files/Level1Script.txt","r+") #Open
    lines = f.readlines() #All lines
    num = len(lines) #Number of lines
    f.close() #Close
    for i in range(num):
        script1.append(lines[i])
    #endfor

    f = open("Game_Files/Level2Script.txt","r+") #Open
    lines = f.readlines() #All lines
    num = len(lines) #Number of lines
    f.close() #Close
    for i in range(num):
        script2.append(lines[i])
    #endfor

    f = open("Game_Files/Level3Script.txt","r+") #Open
    lines = f.readlines() #All lines
    num = len(lines) #Number of lines
    f.close() #Close
    for i in range(num):
        script3.append(lines[i])
    #endfor

#endfor

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

        self.play = [pygame.transform.scale(pygame.image.load('Game_Images/Object/Buttons/Play1.png'), (309, 93)), pygame.transform.scale(pygame.image.load('Game_Images/Object/Buttons/Play2.png'), (309, 93))]
        self.set = [pygame.transform.scale(pygame.image.load('Game_Images/Object/Buttons/Settings1.png'), (615, 93)), pygame.transform.scale(pygame.image.load('Game_Images/Object/Buttons/Settings2.png'), (615, 93))]
        self.tutorial = [pygame.transform.scale(pygame.image.load('Game_Images/Object/Buttons/Tutorial1.png'), (639, 93)), pygame.transform.scale(pygame.image.load('Game_Images/Object/Buttons/Tutorial2.png'), (639, 93))]
        self.select = [pygame.transform.scale(pygame.image.load('Game_Images/Object/Buttons/Select1.png'), (161, 31)), pygame.transform.scale(pygame.image.load('Game_Images/Object/Buttons/Select2.png'), (161, 31))]
        self.back = [pygame.transform.scale(pygame.image.load('Game_Images/Object/Buttons/Back1.png'), (106, 31)), pygame.transform.scale(pygame.image.load('Game_Images/Object/Buttons/Back2.png'), (106, 31))]
        self.easy = [pygame.transform.scale(pygame.image.load('Game_Images/Object/Buttons/Easy1.png'), (411, 120)), pygame.transform.scale(pygame.image.load('Game_Images/Object/Buttons/Easy2.png'), (411, 120))]
        self.hard = [pygame.transform.scale(pygame.image.load('Game_Images/Object/Buttons/Hard1.png'), (441, 120)), pygame.transform.scale(pygame.image.load('Game_Images/Object/Buttons/Hard2.png'), (441, 120))]
        self.pause = [pygame.transform.scale(pygame.image.load('Game_Images/Object/Buttons/Pause1.png'), (60, 60)), pygame.transform.scale(pygame.image.load('Game_Images/Object/Buttons/Pause2.png'), (60, 60))]
        self.close = [pygame.transform.scale(pygame.image.load('Game_Images/Object/Buttons/Close1.png'), (60, 60)), pygame.transform.scale(pygame.image.load('Game_Images/Object/Buttons/Close2.png'), (60, 60))]
        self.next = [pygame.transform.scale(pygame.image.load('Game_Images/Object/Buttons/Next1.png'), (60, 20)), pygame.transform.scale(pygame.image.load('Game_Images/Object/Buttons/Next2.png'), (60, 20))]
        self.quit = [pygame.transform.scale(pygame.image.load('Game_Images/Object/Buttons/Quit1.png'), (width, height)), pygame.transform.scale(pygame.image.load('Game_Images/Object/Buttons/Quit2.png'), (width, height))]

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

        elif self.imageNum == 6:

            self.image = self.easy[0]

        elif self.imageNum == 7:

            self.image = self.hard[0]

        elif self.imageNum == 8:

            self.image = self.pause[0]

        elif self.imageNum == 9:

            self.image = self.next[0]

        elif self.imageNum == 10:

            self.image = self.close[0]

        elif self.imageNum == 11:

            self.image = self.quit[0]

        #endif
        
    #endprocedure

    def Change(self, pos, level):

        if level == 0 and pos[0] >= 595.5 and pos[1] >= 420 and pos[0] <= 904.5 and pos[1] <= 513 and self.imageNum == 1: #Menu
            
            self.image = self.play[1] #Hover on start button
            
        elif level == 0 and pos[0] >= 442.5 and pos[1] >= 560 and pos[0] <= 1057.5 and pos[1] <= 653 and self.imageNum == 2: #Settings
            
            self.image = self.set[1] #Hover on Settings
            
        elif level == 0 and pos[0] >= 430.5 and pos[1] >= 700 and pos[0] <= 1069.5 and pos[1] <= 793 and self.imageNum == 3: #Tutorial
            
            self.image = self.tutorial[1] #Hover on Tutorial

        elif level == 1 and pos[0] >= 544.5 and pos[1] >= 300 and pos[0] <= 955.5 and pos[1] <= 420 and self.imageNum == 6: #Easy
            
            self.image = self.easy[1] #Hover on Easy

        elif level == 1 and pos[0] >= 529.5 and pos[1] >= 300 and pos[0] <= 970.5 and pos[1] <= 420 and self.imageNum == 7: #Hard
            
            self.image = self.hard[1] #Hover on Hard

        elif level == 1 and pos[0] >= 50 and pos[1] >= 820 and pos[0] <= 156 and pos[1] <= 851 and self.imageNum == 5: #Back Button on Settings
            
            self.image = self.back[1] #Hover on back

        elif level == 3 and pos[0] >= 249.5 and pos[1] >= 680.5 and pos[0] <= 410.5 and pos[1] <= 711.5 and self.imageNum == 4 and self.num == 1: #Save Files
            
            self.image = self.select[1] #Hover on select file 1
            
        elif level == 3 and pos[0] >= 669.5 and pos[1] >= 680.5 and pos[0] <= 830.5 and pos[1] <= 711.5 and self.imageNum == 4 and self.num == 2:
            
            self.image = self.select[1] #Hover on select file 2

        elif level == 3 and pos[0] >= 1089.5 and pos[1] >= 680.5 and pos[0] <= 1250.5 and pos[1] <= 711.5 and self.imageNum == 4 and self.num == 3:
            
            self.image = self.select[1] #Hover on select file 3
            
        elif level == 3 and pos[0] >= 50 and pos[1] >= 820 and pos[0] <= 156 and pos[1] <= 851 and self.imageNum == 5:
            
            self.image = self.back[1] #Hover on back

        elif level == 2 and pos[0] >= 1430 and pos[1] >= 10 and pos[0] <= 1490 and pos[1] <= 70 and self.imageNum == 10:
            
            self.image = self.close[1] #Hover on pause

        elif level == 4 and pos[0] >= 1430 and pos[1] >= 10 and pos[0] <= 1490 and pos[1] <= 70 and self.imageNum == 8:
            
            self.image = self.pause[1] #Hover on close

        elif level == 4 and pos[0] >= 1195 and pos[1] >= 850 and pos[0] <= 1255 and pos[1] <= 870 and self.imageNum == 9:

            self.image = self.next[1]

        elif level == 4 and pos[0] >= 1068 and pos[1] >= 234 and pos[0] <= 1128 and pos[1] <= 294 and self.imageNum == 10:

            self.image = self.close[1]

        elif level == 4 and pos[0] >= 700 and pos[1] >= 530 and pos[0] <= 800 and pos[1] <= 570 and self.imageNum == 11:

            self.image = self.quit[1]
            
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

            elif self.imageNum == 6:

                self.image = self.easy[0]

            elif self.imageNum == 7:

                self.image = self.hard[0]

            elif self.imageNum == 8:

                self.image = self.pause[0]

            elif self.imageNum == 9:

                self.image = self.next[0]

            elif self.imageNum == 10:

                self.image = self.close[0]

            elif self.imageNum == 11:

                self.image = self.quit[0]

            #endif

        #endif

    #endprocedure

#endclass

#Save Files Class------------------------------------------------------------------------------------------------------------------
#Item Class
class ItemClass(pygame.sprite.Sprite):

    def __init__(self, typeOfItem, width, height, x, y, level):
        super().__init__()

        self.image = pygame.Surface([width,height])
        self.rect = self.image.get_rect() #Get the shape

        self.rect.x = x #Set position
        self.rect.y = y

        self.item = typeOfItem

        #Attributes
        self.vertSpeed = 0
        self.horiSpeed = 0
        self.finalX = randint(-30,30)
        if self.finalX > 0:
            self.horiSpeed = 1
        elif self.finalX < 0:
            self.horiSpeed = -1
        #endif
        self.moveX = 0
        self.level = level

        #Coin
        self.dropped = False
        self.getCoin = False
        #self.coinSound = AudioSegment.from_wav('Game_Sounds/Object/coin.wav')

        #Counters
        self.coinCounter = 0

        #Timers
        self.startAnimation = 0
        self.endAnimation = 0
        self.startDisappear = 0
        self.endDisappear = 0

        self.coins = []
        for x in range(7):
            add_str = str(x+1)
            self.coins.append(pygame.transform.scale(pygame.image.load("Game_Images/Object/Coins/Coin" + add_str + ".png"), (width, height)))
        #endfor

        self.hearts = [pygame.transform.scale(pygame.image.load("Game_Images/Object/Hearts/Heart.png"), (50, 50))] #Hearts
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
        if self.endAnimation - self.startAnimation >= 120 and self.item == 1 and not self.getCoin:

            self.startAnimation = self.endAnimation #Reset timer

            self.image = self.coins[self.coinCounter]
            if self.coinCounter == 4:
                self.coinCounter = 0
            else:
                self.coinCounter += 1
            #endif

        elif self.endAnimation - self.startAnimation >= 100 and self.item == 1 and self.getCoin:

            if self.coinCounter < 5:
                self.coinCounter = 5
            #endif
            self.startAnimation = self.endAnimation #Reset timer

            self.image = self.coins[self.coinCounter]
            if self.coinCounter == 6:
                self.coinCounter = 6
            elif self.coinCounter == 5:
                self.coinCounter += 1
            #endif

        #endif

    #endprocedure

    def CoinUpdate(self, player_list, block1_list, tutorialBlock_list, tutorial_list, levelOne_list, coin_list, currency):

        if not self.dropped:

            self.dropped = True
            self.vertSpeed = randint(5,6)

        #endif

        if not self.getCoin:

            for player in player_list: #If player touch coin
                if self.rect.colliderect(player.rect):
                    self.getCoin = True
                #endif
            #endfor

            if abs(self.moveX) < abs(self.finalX) and self.horiSpeed != 0:
                self.rect.x += self.horiSpeed
                self.moveX += self.horiSpeed
            #endif

            if self.level == 2:
                for block in tutorialBlock_list:
                    if self.rect.colliderect(block.rect):
                        if self.horiSpeed > 0:
                            self.rect.right = block.rect.left
                        elif self.horiSpeed < 0:
                            self.rect.left = block.rect.right
                        #endif
                        self.horiSpeed = 0
                    #endif
                #endfor
            elif self.level == 4:
                for block in block1_list:
                    if self.rect.colliderect(block.rect):
                        if self.horiSpeed > 0:
                            self.rect.right = block.rect.left
                        elif self.horiSpeed < 0:
                            self.rect.left = block.rect.right
                        #endif
                        self.horiSpeed = 0
                    #endif
                #endfor
            #endif

            if self.vertSpeed == 0: #Keep testing if coin hits something
                self.vertSpeed = -0.4
            else: #Gravity
                self.vertSpeed -= 0.6
            #endif

            if self.rect.y >= 780 and self.vertSpeed <= 0: #If sinks into the ground

                self.rect.y = 780 #Stands on the ground
                self.vertSpeed = 0

            elif self.rect.y <= 0 and self.vertSpeed > 0:

                self.rect.y = 0
                self.vertSpeed = 0

            #endif

            self.rect.y -= self.vertSpeed #coin move vertically

            if self.level == 4:
                
                coinVertBlock_list = pygame.sprite.spritecollide(self, block1_list, False)#If collide
                for block in coinVertBlock_list:
                    
                    if self.vertSpeed <= 0: #If coin is falling

                        self.rect.bottom = block.rect.top

                    elif self.vertSpeed >= 0: #If coin is jumping

                        self.rect.top = block.rect.bottom

                    #endif

                    self.vertSpeed = 0 #Stop coin

                #endfor

            elif self.level == 2:

                coinVertBlock_list = pygame.sprite.spritecollide(self, tutorialBlock_list, False)#If collide
                for block in coinVertBlock_list:
                    
                    if self.vertSpeed <= 0: #If coin is falling

                        self.rect.bottom = block.rect.top

                    elif self.vertSpeed >= 0: #If coin is jumping

                        self.rect.top = block.rect.bottom

                    #endif

                    self.vertSpeed = 0 #Stop coin

                #endfor

            #endif

        elif self.getCoin:

            if self.startDisappear == 0: #If start timer has not started yet

                self.startDisappear = pygame.time.get_ticks() #Record current time
                #play(self.coinSound)

            #endif

            self.endDisappear = pygame.time.get_ticks() #Get current time for end time
            if self.endDisappear - self.startDisappear >= 200:

                if self.level == 2:
                    tutorial_list.remove(self)
                elif self.level == 4:
                    levelOne_list.remove(self)
                #endif
                coin_list.remove(self)
                currency[3] += 1
                if currency[3] == 10:
                    currency[2] += 1
                    currency[3] = 0
                #endif
                if currency[2] == 10:
                    currency[1] += 1
                    currency[2] = 0
                #endif
                if currency[1] == 10:
                    currency[0] += 1
                    currency[1] = 0
                #endif
                if currency[0] == 10:
                    currency[0] = 0
                    currency[1] = 0
                    currency[2] = 0
                    currency[3] = 0
                #endif
            #endif
                
        #endif

    #endprocedure

#endclass

#Timer Class
class TimerClass():

    def __init__(self):

        #Timers
        self.start = 0
        self.end = 0

    #endprocedure

    def Counter(self, loTime, timeUp):

        if self.start == 0:
            self.start = pygame.time.get_ticks() #Record current time
            timeUp[0] = 0
        #endif
        self.end = pygame.time.get_ticks() #Record current time
        if self.end - self.start >= loTime:
            timeUp[0] = 1
            self.start = 0
            self.end = 0
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
            self.numbers.append(pygame.transform.scale(pygame.image.load("Game_Images/Object/Numbers/" + add_str + ".png"), (width, height)))
        #endfor
        self.small = []
        for x in range(26):
            add_str = str(x+1)
            self.small.append(pygame.transform.scale(pygame.image.load("Game_Images/Object/Characters/Small" + add_str + ".png"), (width, height)))
        #endfor
        self.capital = []
        for x in range(26):
            add_str = str(x+1)
            self.capital.append(pygame.transform.scale(pygame.image.load("Game_Images/Object/Characters/Capital" + add_str + ".png"), (width, height)))
        #endfor
        self.exclamation = [pygame.transform.scale(pygame.image.load("Game_Images/Object/Characters/Exclamation.png"), (width, height))]
        self.comma = [pygame.transform.scale(pygame.image.load("Game_Images/Object/Characters/Comma.png"), (width, height))]

        if self.wordType == 0:
            
            self.image = self.numbers[int(self.num)]

        elif self.wordType == 1:

            if self.num >= 97 and self.num <= 122:
                
                self.image = self.small[self.num-97]

            elif self.num >= 65 and self.num <= 90:

                self.image = self.capital[self.num-65]

            elif self.num == 44:

                self.image = self.comma[0]

            elif self.num == 33:

                self.image = self.exclamation[0]

            #endif

        #endif

    #endprocedure

    def Update(self, num):

        self.image = self.numbers[num]

    #endprocedure

#endclass

#Write Words
def WriteWords(typeOfWord, line, x, y, file_list, levelOne_list, levelTwo_list, levelThree_list, currentLine_list, level, gameLevel, pauseTime):

    line = line.rstrip("\n") #Get rid of next line (\n)
    length = len(str(line))
    if typeOfWord == 1:
        x = 242.5
    for i in range(length): #Loop

        if typeOfWord == 0: #If type is number
            width = 24
            height = 31
            xIncrement = 29
            if line[i] != " ":
                word = WordClass(0, line[i], width, height, x, y) #Create word
            #endif
            x += xIncrement #Move Further
            
            if level == 3:
                file_list.add(word) #Add to list
            #endif

        elif typeOfWord == 1:
            officialY = y
            charNum = ord(line[i])
            xIncrement = 16
            if line[i] != " ":
                if charNum >= 97 and charNum <= 122:
                    width = 14
                    height = 20
                    xIncrement = 16
                    if charNum == 105 or charNum == 108:
                        width = 4
                        xIncrement = 6
                    elif charNum == 121 or charNum == 103 or charNum == 112 or charNum == 113:
                        height = 25
                    elif charNum == 100 or charNum == 104 or charNum == 107 or charNum == 98:
                        height = 25
                        y = y - 5
                    #endif
                elif charNum >= 65 and charNum <= 90:
                    width = 16
                    height = 23
                    xIncrement = 18
                    y = y - 3
                    if charNum == 73:
                        width = 8
                        xIncrement = 10
                    #endif
                elif charNum == 44:
                    width = 4
                    height = 8
                    xIncrement = 6
                    y = y + 12
                elif charNum == 33:
                    width = 4
                    height = 25
                    xIncrement = 6
                    y = y - 5
                #endif
                word = WordClass(1, charNum, width, height, x, y) #Create word
                currentLine_list.add(word)
                y = officialY
                if level == 4:
                    if gameLevel == 1:
                        levelOne_list.add(word)
                    elif gameLevel == 2:
                        levelTwo_list.add(word)
                    elif gameLevel == 3:
                        levelThree_list.add(word)
                    #endif
                #endif
            #endif
            x += xIncrement
        #endif

    #endfor

#endprocedure

def SetCrown(crown_list):

    maxMoney = 0
    xPos = 0

    #Open File 1
    f = open("Game_Files/File1.txt","r+") #Open file 1
    lines = f.readlines() #All data
    f.close() #Close

    if lines[0][0] == "0" and lines[0][1] == "0" and lines[0][2] == "0":
        currency = int(lines[0][3])
    elif lines[0][0] == "0" and lines[0][1] == "0":
        currency = int(lines[0][2] + lines[0][3])
    elif lines[0][0] == "0":
        currency = int(lines[0][1] + lines[0][2] + lines[0][3])
    else:
        currency = int(lines[0].rstrip("\n"))
    #endif

    if currency >= maxMoney:

        maxMoney = currency
        xPos = 163.5

    #endif

    #Open File 2
    f = open("Game_Files/File2.txt","r+") #Open file 2
    lines = f.readlines() #All data
    f.close() #Close

    if lines[0][0] == "0" and lines[0][1] == "0" and lines[0][2] == "0":
        currency = int(lines[0][3])
    elif lines[0][0] == "0" and lines[0][1] == "0":
        currency = int(lines[0][2] + lines[0][3])
    elif lines[0][0] == "0":
        currency = int(lines[0][1] + lines[0][2] + lines[0][3])
    else:
        currency = int(lines[0].rstrip("\n"))
    #endif

    if currency > maxMoney:

        maxMoney = currency
        xPos = 583.5

    #endif

    #Open File 3
    f = open("Game_Files/File3.txt","r+") #Open file 3
    lines = f.readlines() #All data
    f.close() #Close

    if lines[0][0] == "0" and lines[0][1] == "0" and lines[0][2] == "0":
        currency = int(lines[0][3])
    elif lines[0][0] == "0" and lines[0][1] == "0":
        currency = int(lines[0][2] + lines[0][3])
    elif lines[0][0] == "0":
        currency = int(lines[0][1] + lines[0][2] + lines[0][3])
    else:
        currency = int(lines[0].rstrip("\n"))
    #endif

    if currency > maxMoney:

        maxMoney = currency
        xPos = 1003.5

    #endif

    for crown in crown_list:

        crown.rect.x = xPos

    #endfor

#endprocedure

#Loading Class--------------------------------------------------------------------------------------
#Load Animation
class LoadingClass(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        
        self.image = pygame.Surface([149, 42])
        self.rect = self.image.get_rect() #Get the shape
        self.rect.x = 1270
        self.rect.y = 800

        self.loading = [pygame.transform.scale(pygame.image.load('Game_Images/Text/Loading1.png'), (149, 42)), pygame.transform.scale(pygame.image.load('Game_Images/Text/Loading2.png'), (157, 42)), pygame.transform.scale(pygame.image.load('Game_Images/Text/Loading3.png'), (165, 42)), pygame.transform.scale(pygame.image.load('Game_Images/Text/Loading4.png'), (173, 42))]
        self.image = self.loading[0]

    #endprocedure
    
    def Animation(self, num):

        self.image = self.loading[num]

    #endprocedure

#endclass

#Instruction Class----------------------------------------------------------------------------------
class InstructionClass(pygame.sprite.Sprite): #Instruction is a sprite, because I need to create multiple instructions
    
    def __init__(self, typeNum, width, height, x, y):
        super().__init__()
        
        self.image = pygame.Surface([width,height])
        self.rect = self.image.get_rect() #Get the shape

        self.rect.x = x
        self.rect.y = y

        self.move = [pygame.transform.scale(pygame.image.load('Game_Images/Text/MoveInstruction.png'), (439, 27))]
        self.jump = [pygame.transform.scale(pygame.image.load('Game_Images/Text/JumpInstruction.png'), (210, 25))]
        self.dJump = [pygame.transform.scale(pygame.image.load('Game_Images/Text/DoubleJumpInstruction.png'), (305, 25))]
        self.attack = [pygame.transform.scale(pygame.image.load('Game_Images/Text/AttackInstruction.png'), (289, 25))]
        self.roll = [pygame.transform.scale(pygame.image.load('Game_Images/Text/RollInstruction.png'), (230, 20))]
        self.block = [pygame.transform.scale(pygame.image.load('Game_Images/Text/BlockInstruction.png'), (189, 20))]
        self.minus = [pygame.transform.scale(pygame.image.load('Game_Images/Text/-.png'), (18, 8))]
        self.coin = [pygame.transform.scale(pygame.image.load('Game_Images/Text/CoinsInstruction.png'), (487, 27))]
        self.fake = [pygame.transform.scale(pygame.image.load('Game_Images/Text/FakeCoinInstruction.png'), (327, 20))]
        self.quit = [pygame.transform.scale(pygame.image.load('Game_Images/Text/QuitInstruction.png'), (698, 77))]

        if typeNum == 1:

            self.image = self.move[0]

        elif typeNum == 2:

            self.image = self.jump[0]

        elif typeNum == 3:

            self.image = self.attack[0]

        elif typeNum == 4:

            self.image = self.roll[0]

        elif typeNum == 5:

            self.image = self.dJump[0]

        elif typeNum == 6:

            self.image = self.block[0]

        elif typeNum == 7:

            self.image = self.minus[0]

        elif typeNum == 8:

            self.image = self.coin[0]

        elif typeNum == 9:

            self.image = self.fake[0]

        elif typeNum == 10:

            self.image = self.quit[0]

        #endif

    #endprocedure

#endclass

#Gameplay Class ------------------------------------------------------------------------------------
#Draw / Remove object on / from Canvas
def DrawOrRemove(num, listOne, listTwo):
    if num == 0:
        for stuff in listTwo:
            listOne.remove(stuff)
        #endfor
    elif num == 1:
        for stuff in listTwo:
            listOne.add(stuff)
        #endfor
    #endif
#endprocedure
            
#Convert Image
def loadify(img):
    
    return pygame.image.load(img).convert_alpha()

#endfunction

#Block
class BlockClass(pygame.sprite.Sprite): #Block is a sprite, because I need to create multiple blocks
    
    def __init__(self, typeOfBlock, width, height, x, y):
        super().__init__()
        
        self.image = pygame.Surface([width,height])
        self.rect = self.image.get_rect() #Get the shape

        self.rect.x = x
        self.rect.y = y

        self.originalX = x

        self.grassBlock = [pygame.transform.scale(pygame.image.load('Game_Images/Background/GroundBlock.png'), (240, 40))]
        self.saveFileBlock = [pygame.transform.scale(pygame.image.load('Game_Images/Text/SaveFileBox.png'), (333, 639))]
        self.crown = [pygame.transform.scale(pygame.image.load('Game_Images/Text/Crown.png'), (333, 141))]
        self.chooseDifficulty = [pygame.transform.scale(pygame.image.load('Game_Images/Text/ChooseDifficulty.png'), (1220, 202))]
        self.wordBlock = [pygame.transform.scale(pygame.image.load('Game_Images/Text/TextBox.png'), (1065, 150))]
        self.optionBlock = [pygame.transform.scale(pygame.image.load('Game_Images/Text/OptionBox.png'), (800, 475))]

        if typeOfBlock == 1:

            self.image = self.grassBlock[0]

        elif typeOfBlock == 2:

            self.image = self.saveFileBlock[0]

        elif typeOfBlock == 3:

            self.image = self.crown[0]

        elif typeOfBlock == 4:

            self.image = self.chooseDifficulty[0]

        elif typeOfBlock == 5:

            self.image = self.wordBlock[0]

        elif typeOfBlock == 6:

            self.image = self.optionBlock[0]

        #endif
        
    #endprocedure

    def Reset(self):

        self.rect.x = self.originalX

    #endprocedure

#endclass

#Ground
class GroundClass(pygame.sprite.Sprite): #Block is a sprite, because I need to create multiple blocks
    
    def __init__(self, num, x, y):
        super().__init__()
        
        self.image = pygame.Surface([1500,100])
        self.rect = self.image.get_rect() #Get the shape

        self.rect.x = x
        self.rect.y = y

        self.originalX = x

        self.num = num

        self.ground = []
        for x in range(1):
            add_str = str(x+1)
            self.ground.append(pygame.transform.scale(loadify("Game_Images/Background/Ground" + add_str + ".png"), (3000, 100)))
        #endfor

        if self.num == 1:

            self.image = self.ground[0]

        #endif
        
    #endprocedure

    def Update(self, num):

        if num == 1:
            self.rect.x -= 10
        elif num == 0:
            self.rect.x = self.originalX
        #endif

    #endprocedure

#endclass

#Background Class
class BackgroundClass(pygame.sprite.Sprite): #Class of the background
 
    def __init__(self, typeBackground, picNum, width, height, x, y):
        
        super().__init__()
 
        self.image = pygame.Surface([width, height])
        self.rect = self.image.get_rect()

        self.scalex = x*10 #Scaled up x and y position
        self.scaley = y*10

        self.rect.x = self.scalex//10
        self.rect.y = self.scaley//10

        self.typeBack = typeBackground
        self.num = picNum

        self.mountains = [] #Mountains
        for x in range(4):
            add_str = str(x+1)
            self.mountains.append(pygame.transform.scale(loadify("Game_Images/Background/Mountains/Mountain" + add_str + ".png"), (2560, 800)))
        #endfor

        if self.typeBack == 1:

            self.image = self.mountains[self.num]

        #endif

    #endprocedure

    def BackUpdate(self):
            
        if self.num == 0:
            
            self.scalex -= 12

        elif self.num == 1:

            self.scalex -= 6

        elif self.num == 2:

            self.scalex -= 3

        elif self.num == 3:

            self.scalex -= 2

        #endif
                
        self.rect.x = self.scalex//10

    #endprocedure

    def CloudUpdate(self):

        if self.num == 2:

            self.scalex -= 10
            if self.scalex <= -25600:
                self.scalex = 25600
            #endif

        elif self.num == 3:

            self.scalex -= 5
            if self.scalex <= -25600:
                self.scalex = 25600
            #endif

        #endif
            
        self.rect.x = self.scalex//10

    #endprocedure

#endclass

#Attack Class
class AttackClass(pygame.sprite.Sprite): #Class of Attack

    def __init__(self, width, height, x, y):
        
        super().__init__()
 
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

    #endprocedure

#endclass

#Health Class
class HealthClass(pygame.sprite.Sprite): #Class of Attack

    def __init__(self, healthType, num, width, height, xPos, yPos):
        
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.rect = self.image.get_rect()

        self.rect.x = xPos
        self.rect.y = yPos

        self.enemyHealth = [] #Health
        for x in range(6):
            add_str = str(x)
            self.enemyHealth.append(pygame.transform.scale(pygame.image.load("Game_Images/Object/Hearts/Health" + add_str + ".png"), (100, 20)))
        #endfor

        if healthType == 1:

            self.image = self.enemyHealth[num]

        #endif

    #endprocedure

    def Update(self,num):

        self.image = self.enemyHealth[num]

    #endprocedure
        
#endclass

#Player Class
class PlayerClass(pygame.sprite.Sprite): #Class of the player
 
    def __init__(self, x, y, playerAttack_list):
        
        super().__init__()
 
        self.image = pygame.Surface([50, 100])
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

        self.playerAnimation = PlayerAnimation(self.rect.x, self.rect.y) #Animation
        self.playerAttack = AttackClass(120, 130, -1000, 0) #Attack
        playerAttack_list.add(self.playerAttack)
        self.playerHealth = HealthClass(1, 5, 100, 20, 25, 675) #Health
        
        #Attributes
        self.hp = 5
        self.hp2 = 0
        self.reduceHealth = False
        self.speedX = 10
        self.horiSpeed = 0
        self.lastHoriSpeed = 4
        self.doubleJump = False
        self.vertSpeed = -0.4
        self.jumped = False
        self.doubleJumped = False
        self.attacked = False
        self.attackStep = 1
        self.stopSelf = False
        self.resetAttack = False
        self.freeze = False
        self.freezeAnimation = False
        self.block = False
        self.blocked = False
        self.unblock = False
        self.roll = False
        self.hurt = False
        self.keepMoving = False
        self.death = False

        #Background
        self.backMove = 0

        #Timers
        self.endAnimation = 0
        self.startAnimation = 0
        self.startAttack = 0
        self.endAttack = 0
        self.startCombo = 0
        self.endCombo = 0
        self.startBlocked = 0
        self.endBlocked = 0
        self.startRoll = 0
        self.endRoll = 0
        self.startDeath = 0
        self.endDeath = 0
        self.startHurt = 0
        self.endHurt = 0
        self.startRest = 0
        self.endRest = 0

        #Counter
        self.idleCounter = 0
        self.runCounter = 0
        self.jumpCounter = 0
        self.fallCounter = 0
        self.attackCounter1 = 0
        self.attackCounter2 = 0
        self.attackCounter3 = 0
        self.blockCounter = 0
        self.blockedCounter = 0
        self.rollCounter = 0
        self.deathCounter = 0
        self.hurtCounter = 0
        
    #endprocedure

    def DrawOnCanvas(self, tutorial_list, levelOne_list, levelTwo_list, levelThree_list):

        tutorial_list.add(self.playerHealth, self.playerAnimation)
        levelOne_list.add(self.playerHealth, self.playerAnimation)
        levelTwo_list.add(self.playerHealth, self.playerAnimation)
        levelThree_list.add(self.playerHealth, self.playerAnimation)

    #endprocedure

    def ResetLive(self, live):

        self.hp = live[0]
        self.playerHealth.Update(self.hp)

    #endprocedure

    def Reset(self):

        self.lastHoriSpeed = 4
        self.horiSpeed = 0
        self.jumped = False
        self.attacked = False
        self.attackStep = 1
        self.stopSelf = False
        self.resetAttack = False
        self.freeze = False
        self.freezeAnimation = False
        self.block = False
        self.blocked = False
        self.unblock = False
        self.roll = False
        self.hurt = False
        self.keepMoving = False
        self.death = False
        self.jumpCounter = 0
        self.fallCounter = 0
        self.attackCounter1 = 0
        self.attackCounter2 = 0
        self.attackCounter3 = 0
        self.blockedCounter = 0
        self.rollCounter = 0
        self.deathCounter = 0
        self.hurtCounter = 0
        self.rect.x = 50
        self.rect.y = 700

        self.playerAttack.rect.x = -1000
        self.Animation()

    #endprocedure

    def FreezeTrigger(self, num):

        if num == 1:
            self.freeze = True
        elif num != 1:
            self.freeze = False
        #endif

    #endprocedure

    def Freeze(self, num):

        if num == 1:
            self.freezeAnimation = True
        else:
            self.freezeAnimation = False
        #endif

    #endprocedure

    def Animation(self):

        if self.startAnimation == 0: #If start timer has not started yet

            self.startAnimation = pygame.time.get_ticks() #Record current time

        #endif

        self.endAnimation = pygame.time.get_ticks() #Get current time for end time

        self.playerAnimation.rect.y = self.rect.y - 38
        self.playerAnimation.rect.x = self.rect.x - 100

        if self.death == False and not self.freezeAnimation:
        
            if self.hurt == False and self.attacked == False and self.horiSpeed == 0 and self.jumped == False and self.block == False and self.blocked == False:

                if self.endAnimation - self.startAnimation >= 160: #If next image
                    
                    self.startAnimation = self.endAnimation #If player is idle
                    self.playerAnimation.PlayerIdle(self.lastHoriSpeed, self.idleCounter)

                    if self.idleCounter != 7: #If reached the end
                        self.idleCounter += 1
                    else:
                        self.idleCounter = 0
                    #endif

                #endif

            elif not self.hurt and self.attacked == False and self.horiSpeed != 0 and self.jumped == False and self.roll == False:

                if self.endAnimation - self.startAnimation >= 80:
                    
                    self.startAnimation = self.endAnimation #If player running
                    self.playerAnimation.PlayerRun(self.lastHoriSpeed, self.runCounter)

                    if self.runCounter != 9: #If reached the end
                        self.runCounter += 1
                    else:
                        self.runCounter = 0
                    #endif

                #endif

            elif self.jumped == True and self.vertSpeed >= 0:

                if self.endAnimation - self.startAnimation >= 200:

                    self.startAnimation = self.endAnimation #If player jumping
                    self.playerAnimation.PlayerJump(self.lastHoriSpeed, self.jumpCounter)

                    if self.jumpCounter != 2: #If reached the end
                        self.jumpCounter += 1
                    else:
                        self.jumpCounter = 2 #Stay at the last frame
                    #endif

                #endif

            elif self.jumped == True and self.vertSpeed < 0:

                if self.endAnimation - self.startAnimation >= 200:

                    self.startAnimation = self.endAnimation #If player falling
                    self.playerAnimation.PlayerFall(self.lastHoriSpeed, self.fallCounter)

                    if self.fallCounter != 3: #If reached the end
                        self.fallCounter += 1
                    else:
                        self.fallCounter = 3 #Stay at the last frame
                    #endif

                #endif

            elif self.attacked == True and self.attackStep == 1:

                if self.endAnimation - self.startAnimation >= 60:

                    self.startAnimation = self.endAnimation 
                    self.playerAnimation.PlayerAttack1(self.lastHoriSpeed, self.attackCounter1)

                    if self.attackCounter1 != 5: 
                        self.attackCounter1 += 1
                    else:
                        self.attackCounter1 = 5
                    #endif

                #endif

            elif self.attacked == True and self.attackStep == 2:

                if self.endAnimation - self.startAnimation >= 60:

                    self.startAnimation = self.endAnimation 
                    self.playerAnimation.PlayerAttack2(self.lastHoriSpeed, self.attackCounter2)

                    if self.attackCounter2 != 5: 
                        self.attackCounter2 += 1
                    else:
                        self.attackCounter2 = 5
                    #endif

                #endif

            elif self.attacked == True and self.attackStep == 3:

                if self.endAnimation - self.startAnimation >= 60:

                    self.startAnimation = self.endAnimation 
                    self.playerAnimation.PlayerAttack3(self.lastHoriSpeed, self.attackCounter3)

                    if self.attackCounter3 != 7: 
                        self.attackCounter3 += 1
                    else:
                        self.attackCounter3 = 7
                    #endif

                #endif

            elif self.block == True and self.blocked == False:

                if self.endAnimation - self.startAnimation >= 80:

                    self.startAnimation = self.endAnimation #If player blocking
                    self.playerAnimation.PlayerBlock(self.lastHoriSpeed, self.blockCounter)

                    if self.blockCounter != 7: #If reached the end
                        self.blockCounter += 1
                    else:
                        self.blockCounter = 0 #Start over
                    #endif

                #endif

            elif self.blocked:

                if self.endAnimation - self.startAnimation >= 80:

                    self.startAnimation = self.endAnimation #If player blocking
                    self.playerAnimation.PlayerBlocked(self.lastHoriSpeed, self.blockedCounter)

                    if self.blockedCounter != 4: #If reached the end
                        self.blockedCounter += 1
                    else:
                        self.blockedCounter = 4 #Stops
                    #endif

                #endif

            elif self.roll == True:

                if self.endAnimation - self.startAnimation >= 50:

                    self.startAnimation = self.endAnimation #If player falling
                    self.playerAnimation.PlayerRoll(self.lastHoriSpeed, self.rollCounter)

                    if self.rollCounter != 8: #If reached the end
                        self.rollCounter += 1
                    else:
                        self.rollCounter = 8 #Stay at the last frame
                    #endif

                #endif

            #endif

            elif self.hurt == True:

                if self.endAnimation - self.startAnimation >= 80:

                    self.startAnimation = self.endAnimation #If player is hurt
                    self.playerAnimation.PlayerHurt(self.lastHoriSpeed, self.hurtCounter)

                    if self.hurtCounter != 2: #If reached the end
                        self.hurtCounter += 1
                    else:
                        self.hurtCounter = 2 #Stay at the last frame
                    #endif

                #endif

            #endif

        elif self.death == True and not self.freezeAnimation:

            if self.endAnimation - self.startAnimation >= 75: #If next image
                    
                self.startAnimation = self.endAnimation #If player is Dead
                self.playerAnimation.PlayerDeath(self.lastHoriSpeed, self.deathCounter)

                if self.deathCounter != 7: #If reached the end
                    self.deathCounter += 1
                else:
                    self.deathCounter == 7
                #endif

            #endif

        #endif

    #endprocedure

    def EnemyAttackDetection(self,attack_list):

        playerGetHit_list = pygame.sprite.spritecollide(self, attack_list, False)#If get hit
        for attack in playerGetHit_list:
            if not self.hurt and not self.reduceHealth and not self.death and not self.freezeAnimation:
                if self.block:
                    self.blocked = True
                elif not self.block and not self.roll:
                    self.hurt = True
                    self.reduceHealth = True
                #endif
            #endif
        #endfor

    #endprocedure

    def RogueDetection(self,attack_list):

        playerGetHit_list = pygame.sprite.spritecollide(self, attack_list, False)#If get hit
        for attack in playerGetHit_list:
            if self.hurt == False and not self.death and not self.freezeAnimation:
                self.hurt = True
                self.reduceHealth = True
                self.block = False
                self.hp2 = -1
            #endif
        #endfor

    #endprocedure

    def Jump(self):

        if not self.freeze and self.blocked == False and self.hurt == False and self.attacked == False and self.roll == False and not self.death:

            if self.jumped == False: #If player has not jumped yet

                self.block = False
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

        if self.freezeAnimation == False:

            if self.vertSpeed == 0: #Keep testing if player hits something
                self.vertSpeed = -0.4
            else: #Gravity
                self.vertSpeed -= 0.6
            #endif

            if self.rect.y >= 700 and self.vertSpeed <= 0: #If sinks into the ground

                self.rect.y = 700 #Stands on the ground
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

    def RollTrigger(self):

        if self.attacked == False and self.jumped == False and self.blocked == False and self.hurt == False and not self.death and not self.freeze:

            self.block = False
            self.roll = True

        #endif

    #endprocedure

    def BlockTrigger(self,num):

        if self.attacked == False and self.jumped == False and num == 1 and self.hurt == False and not self.death and not self.freeze:

            self.horiSpeed = 0
            self.block = True
            self.unblock = False

        elif num == 0 and not self.freezeAnimation:

            self.block = False
            self.unblock = True
            if not self.blocked:
                if not self.keepMoving:
                    self.horiSpeed = 0
                else:
                    if self.lastHoriSpeed < 0:
                        self.horiSpeed = -self.speedX
                    elif self.lastHoriSpeed > 0:
                        self.horiSpeed = self.speedX
                    #endif
                #endif
            #endif

        #endif

    #endprocedure

    def Blocked(self):

        if self.blocked and not self.freezeAnimation:

            self.horiSpeed = 0
            
            if self.startBlocked == 0:
                self.startBlocked = pygame.time.get_ticks()
            #endif

            self.endBlocked = pygame.time.get_ticks()
            if self.endBlocked - self.startBlocked > 410:
                self.endBlocked = 0
                self.startBlocked = 0
                self.blocked = False
                self.blockedCounter = 0
                if self.unblock:
                    self.block = False
                    self.unblock = False
                #endif
            #endif

        #endif

    #endprocedure

    def Health(self, live):

        if self.reduceHealth == True and not self.freezeAnimation:

            self.reduceHealth = False
            if self.hp > 0:
                self.hp -= 1
                self.hp += self.hp2
                self.hp2 = 0
                if self.hp < 0:
                    self.hp = 0
                #endif
                self.playerHealth.Update(self.hp)
            if self.hp == 0:
                self.death = True
            #endif
            live[0] = self.hp

        #endif

        if self.hp == 5:
            self.playerHealth.rect.x = self.rect.x - 25
        elif self.hp == 4:
            self.playerHealth.rect.x = self.rect.x - 15
        elif self.hp == 3:
            self.playerHealth.rect.x = self.rect.x - 5
        elif self.hp == 2:
            self.playerHealth.rect.x = self.rect.x + 5
        elif self.hp == 1:
            self.playerHealth.rect.x = self.rect.x + 15
        #endif
        self.playerHealth.rect.y = self.rect.y - 25

    #endprocedure

    def Death(self):
        
        if self.death == True:

            self.horiSpeed = 0

        #endif

    #endprocedure

    def Revive(self, live):
        
        if self.death == True:

            self.horiSpeed = 0
            
            if self.startDeath == 0:
                self.startDeath = pygame.time.get_ticks()
            #endif

            self.endDeath = pygame.time.get_ticks()
            if self.endDeath - self.startDeath > 3000:
                self.endDeath = 0
                self.startDeath = 0
                self.death = False
                self.deathCounter = 0
                live[0] = 5
                self.hp = 5
                self.playerHealth.Update(self.hp)
            #endif

        #endif

    #endprocedure

    def Hurt(self):
        
        if self.hurt == True and self.death == False and not self.freezeAnimation:

            self.horiSpeed = 0
            
            if self.startHurt == 0:
                self.startHurt = pygame.time.get_ticks()
            #endif

            self.endHurt = pygame.time.get_ticks()
            if self.endHurt - self.startHurt > 250:
                self.endHurt = 0
                self.startHurt = 0
                self.hurt = False
                self.hurtCounter = 0
                if not self.keepMoving:
                    self.horiSpeed = 0
                else:
                    if self.lastHoriSpeed < 0:
                        self.horiSpeed = -self.speedX
                    elif self.lastHoriSpeed > 0:
                        self.horiSpeed = self.speedX
                    #endif
                #endif
            #endif

        #endif

    #endprocedure

    def AttackTrigger(self):

        if self.attacked == False and self.jumped == False and self.roll == False and self.hurt == False and self.blocked == False and self.death == False and not self.freeze:

            self.endRest = pygame.time.get_ticks()
            if self.endRest - self.startRest >= 100 and self.resetAttack:
                self.block = False
                self.attacked = True
                self.startRest = 0
                self.endRest = 0
            else:
                self.block = False
                self.attacked = True
                self.endRest = 0
                self.startRest = 0
            #endif

        #endif

    #endprocedure

    def KeepMove(self, speed):

        if speed == 0:
            self.keepMoving = False
        else:
            self.keepMoving = True
        #endif

    #endprocedure

    def AttackChecker(self):

        if self.stopSelf and not self.freezeAnimation: #If the player should stop

            if not self.keepMoving:
                self.horiSpeed = 0
            else:
                if self.lastHoriSpeed < 0:
                    self.horiSpeed = -self.speedX
                elif self.lastHoriSpeed > 0:
                    self.horiSpeed = self.speedX
                #endif
            #endif
            self.stopSelf = False

        #endif

    #endprocedure

    def Roll(self):

        if self.roll == True and not self.freezeAnimation:

            if self.startRoll == 0:
                self.startRoll = pygame.time.get_ticks()
            #endif
            self.endRoll = pygame.time.get_ticks()
            if self.lastHoriSpeed < 0:
                self.horiSpeed = -12
            else:
                self.horiSpeed = 12
            #endif
            if self.endRoll - self.startRoll > 450:
                self.endRoll = 0
                self.startRoll = 0
                self.roll = False
                if not self.keepMoving: #If keep going
                    self.horiSpeed = 0
                else:
                    if self.lastHoriSpeed < 0:
                        self.horiSpeed = -self.speedX
                    elif self.lastHoriSpeed > 0:
                        self.horiSpeed = self.speedX
                    #endif
                #endif
                self.rollCounter = 0
            #endif

        #endif

    #endprocedure

    def Attack(self):

        if self.attacked == False:
            
            self.endCombo = pygame.time.get_ticks()
            if self.startCombo == 0:
                self.startCombo = pygame.time.get_ticks()
            #endif
            if self.endCombo - self.startCombo >= 500:
                self.attackStep = 1
                self.startCombo = 0
                self.endCombo = 0
            #endif
        
        elif self.attacked == True and not self.freezeAnimation:

            self.horiSpeed = 0
            self.endCombo = 0
            self.startCombo = 0
            if self.attackStep == 1: #Attack 1
                if self.startAttack == 0:
                    self.startAttack = pygame.time.get_ticks()
                #endif
                self.endAttack = pygame.time.get_ticks()
                if self.attackCounter1 == 2 or self.attackCounter1 == 3:
                    if self.lastHoriSpeed > 0 and not self.hurt and not self.death:
                        self.playerAttack.rect.x = self.rect.x + 35
                        self.playerAttack.rect.y = self.rect.y - 30
                    elif self.lastHoriSpeed < 0 and not self.hurt and not self.death:
                        self.playerAttack.rect.x = self.rect.x - 105
                        self.playerAttack.rect.y = self.rect.y - 30
                    #endif
                elif self.attackCounter1 != 2 and self.attackCounter1 != 3:
                    self.playerAttack.rect.x = -1000
                elif self.hurt:
                    self.playerAttack.rect.x = -1000
                #endif
                if self.endAttack - self.startAttack > 360:
                    self.playerAttack.rect.x = -1000
                    if self.lastHoriSpeed < 0:
                        self.horiSpeed = -7
                    else:
                        self.horiSpeed = 7
                    #endif
                    self.stopSelf = True
                    self.endAttack = 0
                    self.startAttack = 0
                    self.attackStep = 2
                    self.attacked = False
                    self.attackCounter1 = 0
                #endif
            elif self.attackStep == 2: #Attack 2
                if self.startAttack == 0:
                    self.startAttack = pygame.time.get_ticks()
                #endif
                self.endAttack = pygame.time.get_ticks()
                if self.attackCounter2 == 2 or self.attackCounter2 == 1:
                    if self.lastHoriSpeed > 0 and not self.hurt and not self.death:
                        self.playerAttack.rect.x = self.rect.x + 35
                        self.playerAttack.rect.y = self.rect.y - 30
                    elif self.lastHoriSpeed < 0 and not self.hurt and not self.death:
                        self.playerAttack.rect.x = self.rect.x - 105
                        self.playerAttack.rect.y = self.rect.y - 30
                    #endif
                elif self.attackCounter2 != 2 and self.attackCounter2 != 1:
                    self.playerAttack.rect.x = -1000
                elif self.hurt:
                    self.playerAttack.rect.x = -1000
                #endif
                if self.endAttack - self.startAttack > 360:
                    self.playerAttack.rect.x = -1000
                    if self.lastHoriSpeed < 0:
                        self.horiSpeed = -7
                    else:
                        self.horiSpeed = 7
                    #endif
                    self.stopSelf = True
                    self.endAttack = 0
                    self.startAttack = 0
                    self.attackStep = 3
                    self.attacked = False
                    self.attackCounter2 = 0
                #endif
            elif self.attackStep == 3: #Attack 3
                if self.startAttack == 0:
                    self.startAttack = pygame.time.get_ticks()
                #endif
                self.endAttack = pygame.time.get_ticks()
                if self.attackCounter3 == 2 or self.attackCounter3 == 3:
                    if self.lastHoriSpeed > 0 and not self.hurt and not self.death:
                        self.playerAttack.rect.x = self.rect.x + 35
                        self.playerAttack.rect.y = self.rect.y - 30
                    elif self.lastHoriSpeed < 0 and not self.hurt and not self.death:
                        self.playerAttack.rect.x = self.rect.x - 105
                        self.playerAttack.rect.y = self.rect.y - 30
                    #endif
                elif self.attackCounter3 != 2 and self.attackCounter3 != 3:
                    self.playerAttack.rect.x = -1000
                elif self.hurt:
                    self.playerAttack.rect.x = -1000
                #endif
                if self.endAttack - self.startAttack > 480:
                    self.playerAttack.rect.x = -1000
                    if self.lastHoriSpeed < 0:
                        self.horiSpeed = -9
                    else:
                        self.horiSpeed = 9
                    #endif
                    self.stopSelf = True
                    self.endAttack = 0
                    self.startAttack = 0
                    self.attackStep = 1
                    self.attacked = False
                    self.attackCounter3 = 0
                    self.startRest = pygame.time.get_ticks()
                    self.resetAttack = True
                #endif
            #endif

        #endif

    #endprocedure

    def ChangeSpeed(self,num):

        if self.freeze == False and self.attacked == False and self.roll == False and self.hurt == False and self.blocked == False and not self.death:

            if num == 0:

                self.horiSpeed = -self.speedX
                self.block = False
                self.lastHoriSpeed = self.horiSpeed

            elif num == 1:

                self.horiSpeed = self.speedX
                self.block = False
                self.lastHoriSpeed = self.horiSpeed

            elif num == 2:

                self.horiSpeed = 0

            #endif

        #endif

    #endprocedure

    def MoveHori2(self):

        self.rect.x += self.horiSpeed

    #endprocedure

    def MoveHori(self, block_list):

        if self.freezeAnimation == False:
            
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

            elif self.rect.x >= 1450:

                self.rect.x = 1450

            #endif

    #endprocedure

#endclass

#Player Animation Class
class PlayerAnimation(pygame.sprite.Sprite): #Class of player's animation
 
    def __init__(self, x, y):
        
        super().__init__()
 
        self.image = pygame.Surface([50, 100])
        self.rect = self.image.get_rect()

        self.rect.x = x #Set pos
        self.rect.y = y

        #Animation
        self.playerIdle = [] #Idle
        for x in range(8):
            add_str = str(x+1)
            self.playerIdle.append(pygame.transform.scale(pygame.image.load("Game_Images/Player/HeroIdle" + add_str + ".png"), (250, 138)))
        #endfor
        self.playerRun = [] #Run
        for x in range(10):
            add_str = str(x+1)
            self.playerRun.append(pygame.transform.scale(pygame.image.load("Game_Images/Player/HeroRun" + add_str + ".png"), (250, 138)))
        #endfor
        self.playerJump = [] #Jump
        for x in range(3):
            add_str = str(x+1)
            self.playerJump.append(pygame.transform.scale(pygame.image.load("Game_Images/Player/HeroJump" + add_str + ".png"), (250, 138)))
        #endfor
        self.playerFall = [] #Fall
        for x in range(4):
            add_str = str(x+1)
            self.playerFall.append(pygame.transform.scale(pygame.image.load("Game_Images/Player/HeroFall" + add_str + ".png"), (250, 138)))
        #endfor
        self.playerAttack1 = [] #Attack 1
        for x in range(6):
            add_str = str(x+1)
            self.playerAttack1.append(pygame.transform.scale(pygame.image.load("Game_Images/Player/HeroAttack1-" + add_str + ".png"), (250, 138)))
        #endfor
        self.playerAttack2 = [] #Attack 2
        for x in range(6):
            add_str = str(x+1)
            self.playerAttack2.append(pygame.transform.scale(pygame.image.load("Game_Images/Player/HeroAttack2-" + add_str + ".png"), (250, 138)))
        #endfor
        self.playerAttack3 = [] #Attack 3
        for x in range(8):
            add_str = str(x+1)
            self.playerAttack3.append(pygame.transform.scale(pygame.image.load("Game_Images/Player/HeroAttack3-" + add_str + ".png"), (250, 138)))
        #endfor
        self.playerBlock = [] #Block
        for x in range(8):
            add_str = str(x+1)
            self.playerBlock.append(pygame.transform.scale(pygame.image.load("Game_Images/Player/HeroBlock" + add_str + ".png"), (250, 138)))
        #endfor
        self.playerBlocked = [] #Blocked
        for x in range(5):
            add_str = str(x+1)
            self.playerBlocked.append(pygame.transform.scale(pygame.image.load("Game_Images/Player/HeroBlocked" + add_str + ".png"), (250, 138)))
        #endfor
        self.playerRoll = [] #Roll
        for x in range(9):
            add_str = str(x+1)
            self.playerRoll.append(pygame.transform.scale(pygame.image.load("Game_Images/Player/HeroRoll" + add_str + ".png"), (250, 138)))
        #endfor
        self.playerHurt = [] #Hurt
        for x in range(3):
            add_str = str(x+1)
            self.playerHurt.append(pygame.transform.scale(pygame.image.load("Game_Images/Player/HeroHurt" + add_str + ".png"), (250, 138)))
        #endfor
        self.playerDeath = [] #Death
        for x in range(8):
            add_str = str(x+1)
            self.playerDeath.append(pygame.transform.scale(pygame.image.load("Game_Images/Player/HeroDeath" + add_str + ".png"), (250, 138)))
        #endfor
        self.image = self.playerIdle[0]
            
        self.image = self.playerIdle[0]
        
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

    def PlayerAttack1(self, speed, i):

        if speed > 0:
            self.image = self.playerAttack1[i]
        else:
            self.image = pygame.transform.flip(self.playerAttack1[i],1,0)
        #endif

    #endprocedure

    def PlayerAttack2(self, speed, i):

        if speed > 0:
            self.image = self.playerAttack2[i]
        else:
            self.image = pygame.transform.flip(self.playerAttack2[i],1,0)
        #endif

    #endprocedure

    def PlayerAttack3(self, speed, i):

        if speed > 0:
            self.image = self.playerAttack3[i]
        else:
            self.image = pygame.transform.flip(self.playerAttack3[i],1,0)
        #endif

    #endprocedure

    def PlayerBlock(self, speed, i):

        if speed > 0:
            self.image = self.playerBlock[i]
        else:
            self.image = pygame.transform.flip(self.playerBlock[i],1,0)
        #endif

    #endprocedure

    def PlayerBlocked(self, speed, i):

        if speed > 0:
            self.image = self.playerBlocked[i]
        else:
            self.image = pygame.transform.flip(self.playerBlocked[i],1,0)
        #endif

    #endprocedure

    def PlayerRoll(self, speed, i):

        if speed > 0:
            self.image = self.playerRoll[i]
        else:
            self.image = pygame.transform.flip(self.playerRoll[i],1,0)
        #endif

    #endprocedure

    def PlayerHurt(self, speed, i):

        if speed > 0:
            self.image = self.playerHurt[i]
        else:
            self.image = pygame.transform.flip(self.playerHurt[i],1,0)
        #endif

    #endprocedure

    def PlayerDeath(self, speed, i):

        if speed > 0:
            self.image = self.playerDeath[i]
        else:
            self.image = pygame.transform.flip(self.playerDeath[i],1,0)
        #endif

    #endprocedure

#endclass

#Enemy Class----------------------------------------------------------------
#Bandit Class
class BanditClass(pygame.sprite.Sprite): #Class of the bandit
 
    def __init__(self, num , x, y, sprites_list, enemyAttack_list):
        
        super().__init__()
 
        self.image = pygame.Surface([50, 100])
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

        self.originalX = x
        self.originalY = y

        self.num = num

        if self.num == 1:
            self.banditAnimation = EnemyAnimation(1, 130, 130, self.rect.x, self.rect.y)
            self.hp = 3
            self.runningSpeed = 11
            self.jumpNum = randint(3,5)
            self.concentrateTime = randint(120,160)
            self.waitTime = randint(150,200)
            self.randomTime = randint(800,1000)
        elif self.num == 0:
            self.banditAnimation = EnemyAnimation(0, 130, 130, self.rect.x, self.rect.y)
            self.hp = 5
            self.runningSpeed = 12
            self.jumpNum = randint(2,4)
            self.concentrateTime = randint(50,70)
            self.waitTime = randint(70,100)
            self.randomTime = randint(500,700)
        #endif
        self.banditAttack = AttackClass(65, 130, -1000, 0)
        enemyAttack_list.add(self.banditAttack)
        self.banditHealth = HealthClass(1, self.hp, 100, 20, self.rect.x - 5, self.rect.y - 25)
        sprites_list.add(self.banditAnimation, self.banditHealth)

        #Attributes
        self.horiSpeed = 0
        self.lastHoriSpeed = -4
        self.vertSpeed = -0.4
        self.jumped = False
        self.attacked = False
        self.attackPhase = 1
        self.stopSelf = False 
        self.freeze = False
        self.hurt = False
        self.death = False
        self.adle = False
        self.reduceHealth = False
        self.dropCoin = False
        self.random = False
        self.random2 = False
        self.jumpTime = 0

        #Timers
        self.endAnimation = 0
        self.startAnimation = 0
        self.startAttack = 0
        self.endAttack = 0
        self.startAttackRest = -1500
        self.endAttackRest = 0
        self.startDeath = 0
        self.endDeath = 0
        self.startHurt = 0
        self.endHurt = 0
        self.startRandom = 0
        self.endRandom = 0
        self.startRandom2 = 0
        self.endRandom2 = 0
        self.startAbove = 0
        self.endAbove = 0

        #Counter
        self.idleCounter = randint(0,3)
        self.adleCounter = randint(0,3)
        self.runCounter = randint(0,7)
        self.jumpCounter = 0
        self.fallCounter = 0
        self.attackCounter = 0
        self.hurtCounter = 0
        self.deathCounter = 0
        
    #endprocedure

    def Freeze(self, num):

        if num == 1:
            self.freeze = True
        else:
            self.freeze = False
        #endif

    #endprocedure

    def Reset(self):

        #Attributes
        self.rect.x = self.originalX
        self.rect.y = self.originalY
        self.hp = 3
        self.horiSpeed = 0
        self.lastHoriSpeed = -4
        self.vertSpeed = -0.4
        self.jumped = False
        self.attacked = False
        self.attackPhase = 1
        self.stopSelf = False 
        self.freeze = False
        self.hurt = False
        self.death = False
        self.adle = False
        self.reduceHealth = False
        self.dropCoin = False
        self.random = False
        self.random2 = False
        self.jumpTime = 0

        #Timers
        self.startAttack = 0
        self.endAttack = 0
        self.startAttackRest = -1500
        self.endAttackRest = 0
        self.startDeath = 0
        self.endDeath = 0
        self.startHurt = 0
        self.endHurt = 0
        self.startRandom = 0
        self.endRandom = 0
        self.startRandom2 = 0
        self.endRandom2 = 0

        #Counter
        self.jumpCounter = 0
        self.attackCounter = 0
        self.hurtCounter = 0
        self.deathCounter = 0

        self.banditAttack.rect.x = -1000
        self.banditHealth.Update(self.hp)
        self.banditHealth.rect.x = self.rect.x - 5
        self.banditHealth.rect.y = self.rect.y - 25
        self.Animation()

    #endprocedure

    def Animation(self):

        if self.startAnimation == 0: #If start timer has not started yet

            self.startAnimation = pygame.time.get_ticks() #Record current time

        #endif

        self.endAnimation = pygame.time.get_ticks() #Get current time for end time

        if self.num == 1:
            self.banditAnimation.rect.y = self.rect.y - 30
        elif self.num == 0:
            self.banditAnimation.rect.y = self.rect.y - 24.6
        #endif
        self.banditAnimation.rect.x = self.rect.x - 40

        if self.death == False and not self.freeze:
        
            if not self.hurt and self.attacked == False and self.horiSpeed == 0 and self.jumped == False and not self.adle:

                if self.endAnimation - self.startAnimation >= 160: #If next image
                    
                    self.startAnimation = self.endAnimation #If player is idle
                    self.banditAnimation.Idle(-self.lastHoriSpeed, self.idleCounter)

                    if self.idleCounter != 3: #If reached the end
                        self.idleCounter += 1
                    else:
                        self.idleCounter = 0
                    #endif

                #endif

            elif not self.hurt and self.attacked == False and self.horiSpeed == 0 and self.jumped == False and self.adle:

                if self.endAnimation - self.startAnimation >= 160: #If next image
                    
                    self.startAnimation = self.endAnimation #If player is idle
                    self.banditAnimation.Adle(-self.lastHoriSpeed, self.adleCounter)

                    if self.adleCounter != 3: #If reached the end
                        self.adleCounter += 1
                    else:
                        self.adleCounter = 0
                    #endif

                #endif

            elif not self.hurt and self.attacked == False and self.horiSpeed != 0 and self.jumped == False:

                if self.endAnimation - self.startAnimation >= 80:
                    
                    self.startAnimation = self.endAnimation #If player running
                    self.banditAnimation.Run(-self.lastHoriSpeed, self.runCounter)

                    if self.runCounter != 7: #If reached the end
                        self.runCounter += 1
                    else:
                        self.runCounter = 0
                    #endif

                #endif

            elif self.jumped == True:

                if self.endAnimation - self.startAnimation >= 200:

                    self.startAnimation = self.endAnimation #If player jumping
                    self.banditAnimation.Jump(-self.lastHoriSpeed, self.jumpCounter)

                    self.jumpCounter = 0

                #endif

            
            elif self.hurt == True:

                if self.endAnimation - self.startAnimation >= 100:

                    self.startAnimation = self.endAnimation #If player is hurt
                    self.banditAnimation.Hurt(-self.lastHoriSpeed, self.hurtCounter)

                    if self.hurtCounter != 2: #If reached the end
                        self.hurtCounter += 1
                    else:
                        self.hurtCounter = 2
                    #endif

                #endif
                    
            elif self.attacked == True:

                if self.endAnimation - self.startAnimation >= 50:

                    self.startAnimation = self.endAnimation 
                    self.banditAnimation.Attack(-self.lastHoriSpeed, self.attackCounter)

                    if self.attackPhase == 1 and self.attackCounter != 3: 
                        self.attackCounter += 1
                    elif self.attackPhase == 3 and self.attackCounter != 7:
                        self.attackCounter += 1
                    #endif

                #endif

            #endif

        elif self.death and not self.freeze:

            if self.endAnimation - self.startAnimation >= 50:

                self.startAnimation = self.endAnimation 
                self.banditAnimation.Death(-self.lastHoriSpeed, self.deathCounter)

                self.deathCounter = 0

            #endif
                    
        #endif

    #endprocedure

    def Control(self, player_list):

        for player in player_list:

            if not self.random and not self.random2 and not self.freeze:

                if player.rect.y == self.rect.y:
                    self.ChangeSpeed(2)
                    self.startAbove = 0
                    self.endAbove = 0
                    if self.rect.x - player.rect.x < 90 and self.rect.x - player.rect.x > 0:
                        self.AttackTrigger()
                        self.random2 = True
                    elif player.rect.x - self.rect.x > 0 and player.rect.x - self.rect.x <= 90:
                        self.AttackTrigger()
                        self.random2 = True
                    elif player.rect.x <= self.rect.x and abs(player.rect.x - self.rect.x) >= 90:
                        self.ChangeSpeed(0)
                    elif player.rect.x > self.rect.x and abs(player.rect.x - self.rect.x) >= 90:
                        self.ChangeSpeed(1)
                    #endif
                elif player.rect.y > self.rect.y:
                    self.ChangeSpeed(2)
                    if self.startAbove == 0: #If start timer has not started yet
                        self.startAbove = pygame.time.get_ticks() #Record current time
                    #endif
                    self.endAbove = pygame.time.get_ticks()
                    if self.endAbove - self.startAbove >= 2000:
                        self.random2 = True
                        self.startAbove = 0
                        self.endAbove = 0
                    #endif
                    if player.rect.x <= self.rect.x and abs(player.rect.x - self.rect.x) >= 90:
                        self.ChangeSpeed(0)
                    elif player.rect.x > self.rect.x and abs(player.rect.x - self.rect.x) >= 90:
                        self.ChangeSpeed(1)
                    #endif
                elif player.rect.y < self.rect.y:
                    self.startAbove = 0
                    self.endAbove = 0
                    self.ChangeSpeed(2)
                    if player.rect.x <= self.rect.x and abs(player.rect.x - self.rect.x) >= 90:
                        self.ChangeSpeed(0)
                    elif player.rect.x > self.rect.x and abs(player.rect.x - self.rect.x) >= 90:
                        self.ChangeSpeed(1)
                    #endif
                    self.Jump()
                    if self.jumpTime > self.jumpNum:
                        self.random = True
                    #endif
                #endif

            elif self.random and not self.freeze:

                if self.startRandom == 0: #If start timer has not started yet
                    self.startRandom = pygame.time.get_ticks() #Record current time
                #endif
                self.jumpTime = 0
                self.endRandom = pygame.time.get_ticks()
                if self.endRandom - self.startRandom > 1500:
                    self.startRandom = self.endRandom
                    self.ChangeSpeed(randint(0,1))
                    self.Jump()
                #endif
                if player.rect.y >= self.rect.y:
                    self.startRandom = 0
                    self.endRandom = 0
                    self.random = False
                #endif

            elif self.random2 and not self.freeze:

                if self.startRandom2 == 0: #If start timer has not started yet

                    self.startRandom2 = pygame.time.get_ticks() #Record current time
                    self.ChangeSpeed(randint(0,1))

                #endif
                    
                self.endRandom2 = pygame.time.get_ticks()
                if self.endRandom2 - self.startRandom2 > self.randomTime:
                    self.startRandom2 = 0
                    self.endRandom2 = 0
                    self.random2 = False

                #endif
                    
            #endif

            if self.rect.x <= 0: #If player reach the end of screen

                self.rect.x = 0

            elif self.rect.x >= 1450:

                self.rect.x = 1450

            #endif

        #endfor

    #endprocedure

    def AttackStance(self,num):

        if num == 1:
            self.adle = True
        else:
            self.adle = False

        #endif

    #endprocedure

    def Health(self, coin_list, sprite_list, level, gameLevel):

        if self.reduceHealth == True and not self.freeze:

            self.reduceHealth = False
            if self.hp > 0:
                self.hp -= 1
                self.banditHealth.Update(self.hp)
            if self.hp == 0:
                if self.num == 1:
                    coinNum = 2
                elif self.num == 0:
                    coinNum = 4
                #endif
                self.death = True
                if not self.dropCoin:
                    self.dropCoin = True
                    for i in range(coinNum):
                        if level == 2:
                            coin = ItemClass(1, 20, 20, self.rect.x + 10, self.rect.y + 70, 2)
                        elif level == 4:
                            coin = ItemClass(1, 20, 20, self.rect.x + 10, self.rect.y + 70, 4)
                        #endif
                        sprite_list.add(coin)
                        coin_list.add(coin)
                    #endfor
                #endif
            #endif

        #endif

        if self.hp == 5:
            self.banditHealth.rect.x = self.rect.x - 25
        elif self.hp == 4:
            self.banditHealth.rect.x = self.rect.x - 15
        elif self.hp == 3:
            self.banditHealth.rect.x = self.rect.x - 5
        elif self.hp == 2:
            self.banditHealth.rect.x = self.rect.x + 5
        elif self.hp == 1:
            self.banditHealth.rect.x = self.rect.x + 15
        #endif
        self.banditHealth.rect.y = self.rect.y - 25

    #endprocedure

    def EnemyAttackDetection(self,playerAttack_list):
        
        enemyGetHit_list = pygame.sprite.spritecollide(self, playerAttack_list, False)#If get hit
        for attack in enemyGetHit_list:
            if self.hurt == False and not self.death and not self.freeze:
                self.hurt = True
                self.reduceHealth = True
            #endif
        #endfor

    #endprocedure

    def Death(self):
        
        if self.death == True and not self.freeze:

            self.horiSpeed = 0
            
            if self.startDeath == 0:
                self.startDeath = pygame.time.get_ticks()
            #endif

            self.endDeath = pygame.time.get_ticks()
            if self.endDeath - self.startDeath > 3000:
                self.endDeath = 0
                self.startDeath = 0
                self.death = False
                self.deathCounter = 0
                self.hp = 3
                self.dropCoin = False
                self.banditHealth.Update(self.hp)
            #endif

        #endif

    #endprocedure

    def Revive(self):
        
        if self.death == True:

            self.horiSpeed = 0
            
            if self.startDeath == 0:
                self.startDeath = pygame.time.get_ticks()
            #endif

            self.endDeath = pygame.time.get_ticks()
            if self.endDeath - self.startDeath > 3000:
                self.endDeath = 0
                self.startDeath = 0
                self.death = False
                self.deathCounter = 0
                if self.num == 1:
                    self.hp = 3
                else:
                    self.hp = 5
                #endif
                self.dropCoin = False
                self.banditHealth.Update(self.hp)
            #endif

        #endif

    #endprocedure

    def Hurt(self):
        
        if self.hurt == True and not self.freeze:

            self.horiSpeed = 0
            
            if self.startHurt == 0:
                self.startHurt = pygame.time.get_ticks()
            #endif

            self.endHurt = pygame.time.get_ticks()
            if self.endHurt - self.startHurt > 300:
                self.endHurt = 0
                self.startHurt = 0
                self.hurt = False
                self.hurtCounter = 0
            #endif

        #endif

    #endprocedure

    def Jump(self):

        if self.freeze == False and self.attacked == False and self.death == False:

            if self.jumped == False: #If player has not jumped yet

                self.jumpTime += 1
                self.vertSpeed = 18
                self.jumped = True
                self.jumpCounter = 0
                self.fallCounter = 0

            #endif

        #endif

    #endprocedure

    def MoveVert(self, block1_list, block2_list, block3_list, tutorialBlock_list, level, gameLevel):

        if self.freeze == False:

            if self.vertSpeed == 0: #Keep testing if player hits something
                self.vertSpeed = -0.4
            else: #Gravity
                self.vertSpeed -= 0.6
            #endif

            if self.rect.y >= 700 and self.vertSpeed <= 0: #If sinks into the ground

                self.rect.y = 700 #Stands on the ground
                self.vertSpeed = 0
                self.jumped = False

            elif self.rect.y <= 0 and self.vertSpeed > 0:

                self.rect.y = 0
                self.vertSpeed = 0

            #endif

            self.rect.y -= self.vertSpeed #Player move

            if level == 4:
                
                selfVertBlock_list = pygame.sprite.spritecollide(self, block1_list, False)#If collide
                for block in selfVertBlock_list:
                    
                    if self.vertSpeed <= 0: #If player is falling

                        self.rect.bottom = block.rect.top
                        self.jumped = False
                        self.startRandom = 0
                        self.endRandom = 0
                        self.random = False

                    elif self.vertSpeed >= 0: #If player is jumping

                        self.rect.top = block.rect.bottom

                    #endif

                    self.vertSpeed = 0 #Stop player

                #endfor

            elif level == 2:

                selfVertBlock_list = pygame.sprite.spritecollide(self, tutorialBlock_list, False)#If collide
                for block in selfVertBlock_list:
                    
                    if self.vertSpeed <= 0: #If player is falling

                        self.rect.bottom = block.rect.top
                        self.jumped = False
                        self.startRandom = 0
                        self.endRandom = 0
                        self.random = False

                    elif self.vertSpeed >= 0: #If player is jumping

                        self.rect.top = block.rect.bottom

                    #endif

                    self.vertSpeed = 0 #Stop player

                #endfor

            #endif

        #endif

    #endprocedure

    def AttackTrigger(self):

        self.endAttackRest = pygame.time.get_ticks() #Get current time for end time
        
        if self.attacked == False and self.jumped == False and self.death == False and self.endAttackRest - self.startAttackRest >= 1500 and not self.freeze:

            self.attacked = True
            self.endAttackRest = 0
            self.startAttackRest = 0

        #endif

    #endprocedure

    def AttackChecker(self):

        if self.stopSelf: #If the enemy should stop

            self.stopSelf = False
            self.horiSpeed = 0

        #endif

    #endprocedure

    def Attack(self):
        
        if self.attacked == True and self.freeze == False:

            self.horiSpeed = 0

            if self.attackPhase == 1:
                if self.attackCounter == 3:
                    self.attackPhase = 2
                #endif
            elif self.attackPhase == 2:
                if self.startAttack == 0:
                    self.startAttack = pygame.time.get_ticks()
                #endif
                self.endAttack = pygame.time.get_ticks()
                if self.endAttack - self.startAttack >= self.concentrateTime:
                    self.endAttack = 0
                    self.startAttack = 0
                    self.attackPhase = 3
                #endif
            elif self.attackPhase == 3:
                if self.lastHoriSpeed > 0 and not self.hurt and not self.death and self.attackCounter < 6:
                    self.banditAttack.rect.x = self.rect.x + 25
                    self.banditAttack.rect.y = self.rect.y - 30
                elif self.lastHoriSpeed < 0 and not self.hurt and not self.death and self.attackCounter < 6:
                    self.banditAttack.rect.x = self.rect.x - 40
                    self.banditAttack.rect.y = self.rect.y - 30
                elif self.attackCounter > 6:
                    self.banditAttack.rect.x = -1000
                elif self.hurt:
                    self.banditAttack.rect.x = -1000
                #endif
                if self.attackCounter == 7:
                    self.attackPhase = 4
                    self.banditAttack.rect.x = -1000
                #endif
            elif self.attackPhase == 4:
                if self.startAttack == 0:
                    self.startAttack = pygame.time.get_ticks()
                #endif
                self.endAttack = pygame.time.get_ticks()
                if self.endAttack - self.startAttack > self.waitTime:
                    self.endAttack = 0
                    self.startAttack = 0
                    self.attacked = False
                    self.attackPhase = 1
                    self.attackCounter = 0
                    self.startAttackRest = pygame.time.get_ticks() #Record current time
                #endif
            #endif

        #endif

    #endprocedure     

    def ChangeSpeed(self,num):

        if self.freeze == False and self.attacked == False and not self.death:

            if num == 0:

                self.horiSpeed = -self.runningSpeed
                self.lastHoriSpeed = self.horiSpeed

            elif num == 1:

                self.horiSpeed = self.runningSpeed
                self.lastHoriSpeed = self.horiSpeed

            elif num == 2:

                self.horiSpeed = 0

            #endif

        #endif

    #endprocedure

    def MoveHori(self, block1_list, block2_list, block3_list, tutorialBlock_list, level, gameLevel):

        if self.freeze == False and not self.death:
            
            self.rect.x += self.horiSpeed

            if level == 2:
                
                for block in tutorialBlock_list:
                            
                    if self.rect.colliderect(block.rect): #If player hit block
                        if self.horiSpeed > 0:
                            self.rect.right = block.rect.left
                        else:
                            self.rect.left = block.rect.right
                        #endif
                    #endif

                #endfor
                            
            elif level == 4:
                
                for block in block1_list:
                            
                    if self.rect.colliderect(block.rect): #If player hit block
                        if self.horiSpeed > 0:
                            self.rect.right = block.rect.left
                        else:
                            self.rect.left = block.rect.right
                        #endif
                    #endif

                #endfor
                            
            #endif

        #endif

    #endprocedure

#endclass

#Warlock Class
class WarlockClass(pygame.sprite.Sprite): #Class of the warlock
 
    def __init__(self, x, y, levelOne_list):
        
        super().__init__()
 
        self.image = pygame.Surface([80, 70])
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

        self.originalX = x
        self.originalY = y

        self.warlockAnimation = EnemyAnimation(2, 160, 160, 150, 730)
        self.warlockHealth = HealthClass(1, 5, 100, 20, self.rect.x - 10, self.rect.y - 35)
        levelOne_list.add(self.warlockAnimation, self.warlockHealth)

        #Attributes
        self.hp = 1
        self.horiSpeed = 0
        self.lastHoriSpeed = -4
        self.vertSpeed = -0.4
        self.attacked = False
        self.freeze = False
        self.hurt = False
        self.death = False
        self.reduceHealth = False

        #Timers
        self.endAnimation = 0
        self.startAnimation = 0
        self.startAttack = 0
        self.endAttack = 0
        self.startDeath = 0
        self.endDeath = 0
        self.startHurt = 0
        self.endHurt = 0

        #Counter
        self.idleCounter = 0
        self.runCounter = 0
        self.attackCounter = 0
        self.hurtCounter = 0
        self.deathCounter = 0
        
    #endprocedure

    def Reset(self):

        #Attributes
        self.rect.x = self.originalX
        self.rect.y = self.originalY
        self.hp = 1
        self.horiSpeed = 0
        self.lastHoriSpeed = -4
        self.vertSpeed = -0.4
        self.attacked = False
        self.freeze = False
        self.hurt = False
        self.death = False
        self.reduceHealth = False

        #Timers
        self.endAnimation = 0
        self.startAnimation = 0
        self.startAttack = 0
        self.endAttack = 0
        self.startDeath = 0
        self.endDeath = 0
        self.startHurt = 0
        self.endHurt = 0

        #Counter
        self.attackCounter = 0
        self.hurtCounter = 0
        self.deathCounter = 0
        
        self.warlockHealth.Update(5)
        self.warlockHealth.rect.x = self.rect.x - 10
        self.warlockHealth.rect.y = self.rect.y - 35
        self.Animation()

    #endprocedure

    def Freeze(self, num):

        if num == 1:
            self.freeze = True
        else:
            self.freeze = False
        #endif

    #endprocedure

    def Animation(self):

        if self.startAnimation == 0: #If start timer has not started yet

            self.startAnimation = pygame.time.get_ticks() #Record current time

        #endif

        self.endAnimation = pygame.time.get_ticks() #Get current time for end time

        self.warlockAnimation.rect.y = self.rect.y - 90
        self.warlockAnimation.rect.x = self.rect.x - 40

        if self.death == False and self.freeze == False:
        
            if not self.hurt and self.horiSpeed == 0:

                if self.endAnimation - self.startAnimation >= 70: #If next image
                    
                    self.startAnimation = self.endAnimation #If player is idle
                    self.warlockAnimation.Idle(self.lastHoriSpeed, self.idleCounter)

                    if self.idleCounter != 11: #If reached the end
                        self.idleCounter += 1
                    else:
                        self.idleCounter = 0
                    #endif

                #endif

            elif not self.hurt and self.horiSpeed != 0:

                if self.endAnimation - self.startAnimation >= 100:
                    
                    self.startAnimation = self.endAnimation #If player running
                    self.warlockAnimation.Run(self.lastHoriSpeed, self.runCounter)

                    if self.runCounter != 7: #If reached the end
                        self.runCounter += 1
                    else:
                        self.runCounter = 0
                    #endif

                #endif
            
            elif self.hurt == True:

                if self.endAnimation - self.startAnimation >= 100:

                    self.startAnimation = self.endAnimation #If player is hurt
                    self.warlockAnimation.Hurt(self.lastHoriSpeed, self.hurtCounter)

                    if self.hurtCounter != 3: #If reached the end
                        self.hurtCounter += 1
                    #endif

                #endif

            #endif

        elif self.death:

            if self.endAnimation - self.startAnimation >= 50:

                self.startAnimation = self.endAnimation 
                self.warlockAnimation.Death(self.lastHoriSpeed, self.deathCounter)

                if self.deathCounter != 12:
                    self.deathCounter += 1
                #endif

            #endif
                    
        #endif

    #endprocedure

    def Health(self):

        if self.reduceHealth == True and not self.freeze:

            self.reduceHealth = False
            self.hp = 0
            self.death = True
            self.warlockHealth.Update(self.hp)

        #endif

        self.warlockHealth.rect.x = self.rect.x - 10
        self.warlockHealth.rect.y = self.rect.y - 35

    #endprocedure

    def EnemyAttackDetection(self,attack_list):

        enemyGetHit_list = pygame.sprite.spritecollide(self, attack_list, False)#If get hit
        for attack in enemyGetHit_list:
            if self.hurt == False and not self.death and not self.freeze:
                self.hurt = True
                self.reduceHealth = True
            #endif
        #endfor

    #endprocedure

    def Hurt(self):
        
        if self.hurt == True and not self.freeze:

            self.horiSpeed = 0
            
            if self.startHurt == 0:
                self.startHurt = pygame.time.get_ticks()
            #endif

            self.endHurt = pygame.time.get_ticks()
            if self.endHurt - self.startHurt > 390:
                self.endHurt = 0
                self.startHurt = 0
                self.hurt = False
                self.hurtCounter = 0
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

            if self.rect.y >= 730 and self.vertSpeed <= 0: #If sinks into the ground

                self.rect.y = 730 #Stands on the ground
                self.vertSpeed = 0
                self.jumped = False

            elif self.rect.y <= 0 and self.vertSpeed > 0:

                self.rect.y = 0
                self.vertSpeed = 0

            #endif

            self.rect.y -= self.vertSpeed #Player move
                
            selfVertBlock_list = pygame.sprite.spritecollide(self, block_list, False)#If collide
            for block in selfVertBlock_list:
                
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

        if self.freeze == False and self.attacked == False and not self.death:

            if num == 0:

                self.horiSpeed = -7
                self.lastHoriSpeed = self.horiSpeed

            elif num == 1:

                self.horiSpeed = 7
                self.lastHoriSpeed = self.horiSpeed

            elif num == 2:

                self.horiSpeed = 0

            #endif

        #endif

    #endprocedure

    def MoveHori(self, block_list):

        if self.freeze == False:
            
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

        #endif

    #endprocedure

#endclass

#Rogue Class
class RogueClass(pygame.sprite.Sprite): #Class of the rogue
 
    def __init__(self, x, y, levelOne_list, enemyAttack_list, rogueAttack_list):
        
        super().__init__()
 
        self.image = pygame.Surface([80, 90])
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

        self.originalX = x
        self.originalY = y

        self.rogueAnimation = EnemyAnimation(3, 160, 160, -1000, -1000)
        self.rogueAttack = AttackClass(200, 70, -1000, 0)
        self.rogueSaAttack = AttackClass(200, 70, -1000, 0)
        rogueAttack_list.add(self.rogueSaAttack)
        enemyAttack_list.add(self.rogueAttack)
        self.rogueHealth = HealthClass(1, 5, 100, 20, self.rect.x - 10, self.rect.y - 25)
        levelOne_list.add(self.rogueAnimation, self.rogueHealth)

        #Attributes
        self.hp = 5
        self.horiSpeed = 0
        self.lastHoriSpeed = -4
        self.vertSpeed = -0.4
        self.attacked = False
        self.sa = False
        self.saMove = False
        self.freeze = False
        self.hurt = False
        self.death = False
        self.spell = False
        self.reduceHealth = False
        self.preyPosX = 0
        self.random = False
        self.attackCount = 0
        self.skill = False
        self.dropCoin = False

        #Timers
        self.endAnimation = 0
        self.startAnimation = 0
        self.startAttack = 0
        self.endAttack = 0
        self.startAttackRest = -750
        self.endAttackRest = 0
        self.startDeath = 0
        self.endDeath = 0
        self.startHurt = 0
        self.endHurt = 0
        self.startRandom = 0
        self.endRandom = 0

        #Counter
        self.idleCounter = 0
        self.runCounter = 0
        self.attackCounter = 0
        self.hurtCounter = 0
        self.deathCounter = 0
        self.saCounter = 0
        
    #endprocedure

    def Freeze(self, num):

        if num == 1:
            self.freeze = True
        elif num != 1:
            self.freeze = False
        #endif

    #endprocedure

    def Unrandom(self):

        self.random = False

    #endprocedure

    def Reset(self):

        #Attributes
        self.hp = 5
        self.horiSpeed = 0
        self.lastHoriSpeed = -4
        self.vertSpeed = -0.4
        self.attacked = False
        self.sa = False
        self.saMove = False
        self.freeze = False
        self.hurt = False
        self.death = False
        self.spell = False
        self.reduceHealth = False
        self.preyPosX = 0
        self.random = False
        self.attackCount = 0
        self.skill = False
        self.dropCoin = False
        self.rect.x = self.originalX
        self.rect.y = self.originalY

        #Timers
        self.endAnimation = 0
        self.startAnimation = 0
        self.startAttack = 0
        self.endAttack = 0
        self.startAttackRest = -750
        self.endAttackRest = 0
        self.startDeath = 0
        self.endDeath = 0
        self.startHurt = 0
        self.endHurt = 0
        self.startRandom = 0
        self.endRandom = 0

        #Counter
        self.attackCounter = 0
        self.hurtCounter = 0
        self.deathCounter = 0
        self.saCounter = 0
        
        self.rogueAttack.rect.x = -1000
        self.rogueSaAttack.rect.x = -1000
        self.rogueHealth.Update(self.hp)
        self.rogueHealth.rect.x = self.rect.x - 10
        self.rogueHealth.rect.y = self.rect.y - 30
        self.Animation()

    #endprocedure

    def Animation(self):

        if self.startAnimation == 0: #If start timer has not started yet

            self.startAnimation = pygame.time.get_ticks() #Record current time

        #endif

        self.endAnimation = pygame.time.get_ticks() #Get current time for end time

        if self.death == False and not self.freeze:

            
            self.rogueAnimation.rect.y = self.rect.y - 160
            self.rogueAnimation.rect.x = self.rect.x - 85
        
            if not self.hurt and self.horiSpeed == 0 and not self.attacked and not self.sa:

                if self.endAnimation - self.startAnimation >= 70: #If next image
                    
                    self.startAnimation = self.endAnimation #If player is idle
                    self.rogueAnimation.Idle(self.lastHoriSpeed, self.idleCounter)

                    if self.idleCounter != 10: #If reached the end
                        self.idleCounter += 1
                    else:
                        self.idleCounter = 0
                    #endif

                #endif

            elif not self.hurt and self.horiSpeed != 0 and not self.attacked and not self.sa:

                if self.endAnimation - self.startAnimation >= 80:
                    
                    self.startAnimation = self.endAnimation #If player running
                    self.rogueAnimation.Run(self.lastHoriSpeed, self.runCounter)

                    if self.runCounter != 9: #If reached the end
                        self.runCounter += 1
                    else:
                        self.runCounter = 0
                    #endif

                #endif
            
            elif self.hurt == True:

                if self.endAnimation - self.startAnimation >= 100:

                    self.startAnimation = self.endAnimation #If player is hurt
                    self.rogueAnimation.Hurt(self.lastHoriSpeed, self.hurtCounter)

                    if self.hurtCounter != 2: #If reached the end
                        self.hurtCounter += 1
                    #endif

                #endif

            elif self.attacked == True and not self.hurt and not self.sa:

                if self.endAnimation - self.startAnimation >= 50:

                    self.startAnimation = self.endAnimation #If player is attacking
                    self.rogueAnimation.Attack(self.lastHoriSpeed, self.attackCounter)

                    if self.attackCounter != 9: #If reached the end
                        self.attackCounter += 1
                    #endif

                #endif

            elif self.sa == True and not self.hurt and not self.attacked:

                if self.endAnimation - self.startAnimation >= 70:

                    self.saMove = True
                    self.startAnimation = self.endAnimation #If player is special attacking
                    self.rogueAnimation.SA(self.lastHoriSpeed, self.saCounter)

                    if self.saCounter != 17: #If reached the end
                        self.saCounter += 1
                    #endif

                #endif

            elif self.spell == True and not self.hurt:

                if self.endAnimation - self.startAnimation >= 90:

                    self.startAnimation = self.endAnimation #If player is casting spell
                    self.rogueAnimation.Spell(self.lastHoriSpeed, self.spellCounter)

                    if self.spellCounter != 11: #If reached the end
                        self.spellCounter += 1
                    #endif

                #endif

            #endif

        elif self.death and not self.freeze:

            if self.endAnimation - self.startAnimation >= 70:

                self.startAnimation = self.endAnimation 
                self.rogueAnimation.Death(self.lastHoriSpeed, self.deathCounter)

                if self.deathCounter != 13:
                    self.deathCounter += 1
                #endif

            #endif
                    
        #endif

    #endprocedure

    def AttackTrigger(self):

        self.endAttackRest = pygame.time.get_ticks() #Get current time for end time
        
        if not self.freeze and self.attacked == False and self.jumped == False and self.death == False and self.endAttackRest - self.startAttackRest >= 750:

            self.attacked = True
            self.endAttackRest = 0
            self.startAttackRest = 0
            self.attackCount += 1
            
        #endif

    #endprocedure

    def AttackChecker(self):

        if self.stopSelf: #If the enemy should stop

            self.stopSelf = False
            self.horiSpeed = 0

        #endif

    #endprocedure

    def Attack(self):
        
        if self.attacked == True and self.freeze == False:

            self.horiSpeed = 0

            if self.lastHoriSpeed > 0 and not self.hurt and not self.death and self.attackCounter == 4:
                self.rogueAttack.rect.x = self.rect.x - 50
                self.rogueAttack.rect.y = self.rect.y
            elif self.lastHoriSpeed < 0 and not self.hurt and not self.death and self.attackCounter == 4:
                self.rogueAttack.rect.x = self.rect.x - 70
                self.rogueAttack.rect.y = self.rect.y
            elif self.attackCounter != 4:
                self.rogueAttack.rect.x = -1000
            elif self.hurt or self.death:
                self.rogueAttack.rect.x = -1000
            #endif
            if self.attackCounter == 9:
                self.rogueAttack.rect.x = -1000
                self.attacked = False
                self.attackCounter = 0
                if self.attackCount == 3:
                    self.attackCount = 0
                    self.skill = True
                #endif
            #endif

        #endif

    #endprocedure

    def Control(self, x):

        if not self.freeze:

            if not self.random and not self.skill:

                self.ChangeSpeed(2)
                if self.rect.x - x < 100 and self.rect.x - x > 0:
                    self.AttackTrigger()
                elif x - self.rect.x > 0 and x - self.rect.x <= 130:
                    self.AttackTrigger()
                elif x <= self.rect.x and abs(x - self.rect.x) >= 100:
                    self.ChangeSpeed(0)
                elif x > self.rect.x and abs(x - self.rect.x) >= 130:
                    self.ChangeSpeed(1)
                #endif

            elif self.skill:

                self.ChangeSpeed(2)
                self.SATrigger(x)

            elif self.random:

                if self.startRandom == 0: #If start timer has not started yet

                    self.startRandom = pygame.time.get_ticks() #Record current time
                    self.ChangeSpeed(randint(0,1))

                #endif
                    
                self.endRandom = pygame.time.get_ticks()
                if self.endRandom - self.startRandom > 400:
                    self.startRandom = 0
                    self.endRandom = 0
                    self.random = False

                #endif

            #endif
                
        #endif

        if self.rect.x <= 0: #If player reach the end of screen

            self.rect.x = 0

        elif self.rect.x >= 1420:

            self.rect.x = 1420

        #endif

    #endprocedure

    def SATrigger(self, xPos):

        if not self.attacked and not self.hurt and not self.death and not self.freeze:

            self.sa = True
            self.preyPosX = xPos - 15

        #endif

    #endprocedure

    def SA(self):

        if self.sa == True and self.freeze == False:

            self.horiSpeed = 0
            self.vertSpeed = 0
            
            if self.saCounter == 8:
                self.rect.x = self.preyPosX
                self.rect.y = 110
            #endif
            if self.saCounter >= 9 and self.saCounter <= 12 and self.saMove:
                self.rect.y += 150
                self.saMove = False
            #endif
            if self.lastHoriSpeed > 0 and not self.hurt and not self.death and self.saCounter >= 12 and self.saCounter <= 14:
                self.rogueSaAttack.rect.x = self.rect.x - 35
                self.rogueSaAttack.rect.y = self.rect.y + 20
            elif self.lastHoriSpeed < 0 and not self.hurt and not self.death and self.saCounter >= 12 and self.saCounter <= 14:
                self.rogueSaAttack.rect.x = self.rect.x - 85
                self.rogueSaAttack.rect.y = self.rect.y + 20
            elif self.saCounter < 12 or self.saCounter > 14:
                self.rogueSaAttack.rect.x = -1000
            elif self.hurt or self.death:
                self.rogueSaAttack.rect.x = -1000
            #endif
            if self.saCounter == 17:
                self.sa = False
                self.rogueSaAttack.rect.x = -1000
                self.rect.y = 710
                self.saCounter = 0
                self.skill = False
                self.random = True
            #endif

        #endif

    #endprocedure

    def Health(self, sprite_list, coin_list):

        if self.reduceHealth == True and not self.freeze:

            self.reduceHealth = False
            if self.hp > 0:
                self.hp -= 1
                self.rogueHealth.Update(self.hp)
            if self.hp == 0:
                self.death = True
                if not self.dropCoin:
                    self.dropCoin = True
                    for i in range(8):
                        coin = ItemClass(1, 20, 20, self.rect.x + 30, self.rect.y + 70, 4)
                        sprite_list.add(coin)
                        coin_list.add(coin)
                    #endfor
                #endif
            #endif

        #endif

        if self.hp == 5:
            self.rogueHealth.rect.x = self.rect.x - 10
        elif self.hp == 4:
            self.rogueHealth.rect.x = self.rect.x
        elif self.hp == 3:
            self.rogueHealth.rect.x = self.rect.x + 10
        elif self.hp == 2:
            self.rogueHealth.rect.x = self.rect.x + 20
        elif self.hp == 1:
            self.rogueHealth.rect.x = self.rect.x + 30
        #endif
        self.rogueHealth.rect.y = self.rect.y - 30

    #endprocedure

    def EnemyAttackDetection(self,attack_list):

        enemyGetHit_list = pygame.sprite.spritecollide(self, attack_list, False)#If get hit
        for attack in enemyGetHit_list:
            if self.hurt == False and not self.death and not self.freeze:
                self.hurt = True
                self.reduceHealth = True
            #endif
        #endfor

    #endprocedure

    def Hurt(self):
        
        if self.hurt == True and not self.freeze:

            self.horiSpeed = 0
            
            if self.startHurt == 0:
                self.startHurt = pygame.time.get_ticks()
            #endif

            self.endHurt = pygame.time.get_ticks()
            if self.endHurt - self.startHurt > 390:
                self.endHurt = 0
                self.startHurt = 0
                self.hurt = False
                self.hurtCounter = 0
                self.attackCount = 0
                self.skill = True
            #endif

        #endif

    #endprocedure

    def MoveVert(self, block_list):

        if self.freeze == False and not self.sa:

            if self.vertSpeed == 0: #Keep testing if player hits something
                self.vertSpeed = -0.4
            else: #Gravity
                self.vertSpeed -= 0.6
            #endif

            if self.rect.y >= 710 and self.vertSpeed <= 0: #If sinks into the ground

                self.rect.y = 710 #Stands on the ground
                self.vertSpeed = 0
                self.jumped = False

            elif self.rect.y <= 0 and self.vertSpeed > 0:

                self.rect.y = 0
                self.vertSpeed = 0

            #endif

            self.rect.y -= self.vertSpeed #Player move
                
            selfVertBlock_list = pygame.sprite.spritecollide(self, block_list, False)#If collide
            for block in selfVertBlock_list:
                
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

        if self.freeze == False and self.attacked == False and not self.death:

            if num == 0:

                self.horiSpeed = -12
                self.lastHoriSpeed = self.horiSpeed

            elif num == 1:

                self.horiSpeed = 12
                self.lastHoriSpeed = self.horiSpeed

            elif num == 2:

                self.horiSpeed = 0

            #endif

        #endif

    #endprocedure

    def MoveHori(self, block_list):

        if self.freeze == False:
            
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

        #endif

    #endprocedure

#endclass

#Enemy Animation Class
class EnemyAnimation(pygame.sprite.Sprite): #Class of player's animation
 
    def __init__(self, enemyType, width, height, x, y):
        
        super().__init__()
 
        self.image = pygame.Surface([width, height])
        self.rect = self.image.get_rect()

        self.rect.x = x #Set pos
        self.rect.y = y

        self.enemy = enemyType

        #Animation
        #Light Bandit
        self.banditIdle1 = [] #Idle 
        for x in range(4):
            add_str = str(x+1)
            self.banditIdle1.append(pygame.transform.scale(pygame.image.load("Game_Images/LightBandit/BanditIdle" + add_str + ".png"), (130, 130)))
        #endfor
        self.banditAdle1 = [] #Attack Idle 
        for x in range(4):
            add_str = str(x+1)
            self.banditAdle1.append(pygame.transform.scale(pygame.image.load("Game_Images/LightBandit/BanditAdle" + add_str + ".png"), (130, 130)))
        #endfor
        self.banditRun1 = [] #Run
        for x in range(8):
            add_str = str(x+1)
            self.banditRun1.append(pygame.transform.scale(pygame.image.load("Game_Images/LightBandit/BanditRun" + add_str + ".png"), (130, 130)))
        #endfor
        self.banditJump1 = [] #Jump
        for x in range(1):
            add_str = str(x+1)
            self.banditJump1.append(pygame.transform.scale(pygame.image.load("Game_Images/LightBandit/BanditJump" + add_str + ".png"), (130, 130)))
        #endfor
        self.banditAttack1 = [] #Attack 1
        for x in range(8):
            add_str = str(x+1)
            self.banditAttack1.append(pygame.transform.scale(pygame.image.load("Game_Images/LightBandit/BanditAttack" + add_str + ".png"), (130, 130)))
        #endfor
        self.banditHurt1 = [] #Hurt 1
        for x in range(3):
            add_str = str(x+1)
            self.banditHurt1.append(pygame.transform.scale(pygame.image.load("Game_Images/LightBandit/BanditHurt" + add_str + ".png"), (130, 130)))
        #endfor
        self.banditDeath1 = [] #Death 1
        for x in range(1):
            self.banditDeath1.append(pygame.transform.scale(pygame.image.load("Game_Images/LightBandit/BanditDeath" + str(1) + ".png"), (130, 130)))
        #endfor
        self.banditRecover1 = [] #Recover 1
        for x in range(8):
            add_str = str(x+1)
            self.banditRecover1.append(pygame.transform.scale(pygame.image.load("Game_Images/LightBandit/BanditRecover" + add_str + ".png"), (130, 130)))
        #endfor

        #Heavy Bandit
        self.banditIdle2 = [] #Idle 
        for x in range(4):
            add_str = str(x)
            self.banditIdle2.append(pygame.transform.scale(pygame.image.load("Game_Images/HeavyBandit/Idle/HeavyBandit_Idle_" + add_str + ".png"), (130, 130)))
        #endfor
        self.banditAdle2 = [] #Attack Idle 
        for x in range(4):
            add_str = str(x)
            self.banditAdle2.append(pygame.transform.scale(pygame.image.load("Game_Images/HeavyBandit/Adle/HeavyBandit_CombatIdle_" + add_str + ".png"), (130, 130)))
        #endfor
        self.banditRun2 = [] #Run
        for x in range(8):
            add_str = str(x)
            self.banditRun2.append(pygame.transform.scale(pygame.image.load("Game_Images/HeavyBandit/Run/HeavyBandit_Run_" + add_str + ".png"), (130, 130)))
        #endfor
        self.banditJump2 = [] #Jump
        for x in range(1):
            add_str = str(x)
            self.banditJump2.append(pygame.transform.scale(pygame.image.load("Game_Images/HeavyBandit/Jump/HeavyBandit_Jump_0.png"), (130, 130)))
        #endfor
        self.banditAttack2 = [] #Attack 2
        for x in range(8):
            add_str = str(x)
            self.banditAttack2.append(pygame.transform.scale(pygame.image.load("Game_Images/HeavyBandit/Attack/HeavyBandit_Attack_" + add_str + ".png"), (130, 130)))
        #endfor
        self.banditHurt2 = [] #Hurt 2
        for x in range(3):
            add_str = str(x)
            self.banditHurt2.append(pygame.transform.scale(pygame.image.load("Game_Images/HeavyBandit/Hurt/HeavyBandit_Hurt_" + add_str + ".png"), (130, 130)))
        #endfor
        self.banditDeath2 = [] #Death 2
        for x in range(1):
            self.banditDeath2.append(pygame.transform.scale(pygame.image.load("Game_Images/HeavyBandit/Death/HeavyBandit_Death_0.png"), (130, 130)))
        #endfor
        self.banditRecover2 = [] #Recover 2
        for x in range(8):
            add_str = str(x)
            self.banditRecover2.append(pygame.transform.scale(pygame.image.load("Game_Images/HeavyBandit/Recover/HeavyBandit_Recover_" + add_str + ".png"), (130, 130)))
        #endfor

        #Warlock
        self.warlockIdle = [] #Idle 
        for x in range(12):
            add_str = str(x+1)
            self.warlockIdle.append(pygame.transform.scale(pygame.image.load("Game_Images/Warlock/WarlockIdle" + add_str + ".png"), (160, 160)))
        #endfor
        self.warlockRun = [] #Run
        for x in range(8):
            add_str = str(x+1)
            self.warlockRun.append(pygame.transform.scale(pygame.image.load("Game_Images/Warlock/WarlockRun" + add_str + ".png"), (160, 160)))
        #endfor
        self.warlockDeath = [] #Death
        for x in range(13):
            add_str = str(x+1)
            self.warlockDeath.append(pygame.transform.scale(pygame.image.load("Game_Images/Warlock/WarlockDeath" + add_str + ".png"), (160, 160)))
        #endfor
        self.warlockHurt = [] #Hurt
        for x in range(4):
            add_str = str(x+1)
            self.warlockHurt.append(pygame.transform.scale(pygame.image.load("Game_Images/Warlock/WarlockHurt" + add_str + ".png"), (160, 160)))
        #endfor

        #Rogue
        self.rogueIdle = [] #Idle 
        for x in range(11):
            add_str = str(x+1)
            self.rogueIdle.append(pygame.transform.scale(pygame.image.load("Game_Images/Rogue/RogueIdle" + add_str + ".png"), (250, 250)))
        #endfor
        self.rogueRun = [] #Run
        for x in range(10):
            add_str = str(x+1)
            self.rogueRun.append(pygame.transform.scale(pygame.image.load("Game_Images/Rogue/RogueRun" + add_str + ".png"), (250, 250)))
        #endfor
        self.rogueDeath = [] #Death
        for x in range(14):
            add_str = str(x+1)
            self.rogueDeath.append(pygame.transform.scale(pygame.image.load("Game_Images/Rogue/RogueDeath" + add_str + ".png"), (250, 250)))
        #endfor
        self.rogueHurt = [] #Hurt
        for x in range(3):
            add_str = str(x+1)
            self.rogueHurt.append(pygame.transform.scale(pygame.image.load("Game_Images/Rogue/RogueHurt" + add_str + ".png"), (250, 250)))
        #endfor
        self.rogueDeath = [] #Death
        for x in range(14):
            add_str = str(x+1)
            self.rogueDeath.append(pygame.transform.scale(pygame.image.load("Game_Images/Rogue/RogueDeath" + add_str + ".png"), (250, 250)))
        #endfor
        self.rogueAttack = [] #Attack
        for x in range(10):
            add_str = str(x+1)
            self.rogueAttack.append(pygame.transform.scale(pygame.image.load("Game_Images/Rogue/RogueAttack" + add_str + ".png"), (250, 250)))
        #endfor
        self.rogueSA = [] #Special Attack
        for x in range(18):
            add_str = str(x+1)
            self.rogueSA.append(pygame.transform.scale(pygame.image.load("Game_Images/Rogue/RogueSA" + add_str + ".png"), (250, 250)))
        #endfor
        self.rogueSpell = [] #Spell
        for x in range(12):
            add_str = str(x+1)
            self.rogueSpell.append(pygame.transform.scale(pygame.image.load("Game_Images/Rogue/RogueSpell" + add_str + ".png"), (250, 250)))
        #endfor

        if self.enemy == 1: #Set
            self.image = pygame.transform.flip(self.banditIdle1[0],1,0)
        elif self.enemy == 2:
            self.image = pygame.transform.flip(self.warlockIdle[0],1,0)
        elif self.enemy == 3:
            self.image = pygame.transform.flip(self.rogueIdle[0],1,0)
        #endif
        
    #endprocedure

    def Idle(self, speed, i): #When enemy not moving

        if self.enemy == 1:
            if speed > 0:
                self.image = self.banditIdle1[i] #Right
            else:
                self.image = pygame.transform.flip(self.banditIdle1[i],1,0) #Left
            #endif
        elif self.enemy == 2:
            if speed > 0:
                self.image = self.warlockIdle[i] #Right
            else:
                self.image = pygame.transform.flip(self.warlockIdle[i],1,0) #Left
            #endif
        elif self.enemy == 3:
            if speed > 0:
                self.image = self.rogueIdle[i] #Right
            else:
                self.image = pygame.transform.flip(self.rogueIdle[i],1,0) #Left
            #endif
        elif self.enemy == 0:
            if speed > 0:
                self.image = self.banditIdle2[i] #Right
            else:
                self.image = pygame.transform.flip(self.banditIdle2[i],1,0) #Left
            #endif
        #endif

    #endprocedure

    def Adle(self, speed, i): #When enemy not moving 2

        if self.enemy == 1:
            if speed > 0:
                self.image = self.banditAdle1[i] #Right
            else:
                self.image = pygame.transform.flip(self.banditAdle1[i],1,0) #Left
            #endif
        elif self.enemy == 0:
            if speed > 0:
                self.image = self.banditAdle2[i] #Right
            else:
                self.image = pygame.transform.flip(self.banditAdle2[i],1,0) #Left
            #endif
        #endif

    #endprocedure

    def Run(self, speed, i):

        if self.enemy == 1:
            if speed > 0:
                self.image = self.banditRun1[i]
            else:
                self.image = pygame.transform.flip(self.banditRun1[i],1,0)
            #endif
        elif self.enemy == 2:
            if speed > 0:
                self.image = self.warlockRun[i] #Right
            else:
                self.image = pygame.transform.flip(self.warlockRun[i],1,0) #Left
            #endif
        elif self.enemy == 3:
            if speed > 0:
                self.image = self.rogueRun[i] #Right
            else:
                self.image = pygame.transform.flip(self.rogueRun[i],1,0) #Left
            #endif
        elif self.enemy == 0:
            if speed > 0:
                self.image = self.banditRun2[i] #Right
            else:
                self.image = pygame.transform.flip(self.banditRun2[i],1,0) #Left
            #endif
        #endif

    #endprocedure

    def Jump(self, speed, i):

        if self.enemy == 1:
            if speed > 0:
                self.image = self.banditJump1[i]
            else:
                self.image = pygame.transform.flip(self.banditJump1[i],1,0)
            #endif
        elif self.enemy == 0:
            if speed > 0:
                self.image = self.banditJump2[i] #Right
            else:
                self.image = pygame.transform.flip(self.banditJump2[i],1,0) #Left
            #endif
        #endif

    #endprocedure

    def Attack(self, speed, i):

        if self.enemy == 1:
            if speed > 0:
                self.image = self.banditAttack1[i]
            else:
                self.image = pygame.transform.flip(self.banditAttack1[i],1,0)
            #endif
        elif self.enemy == 3:
            if speed > 0:
                self.image = self.rogueAttack[i] #Right
            else:
                self.image = pygame.transform.flip(self.rogueAttack[i],1,0) #Left
            #endif
        elif self.enemy == 0:
            if speed > 0:
                self.image = self.banditAttack2[i] #Right
            else:
                self.image = pygame.transform.flip(self.banditAttack2[i],1,0) #Left
            #endif
        #endif

    #endprocedure

    def Hurt(self, speed, i):

        if self.enemy == 1:
            if speed > 0:
                self.image = self.banditHurt1[i]
            else:
                self.image = pygame.transform.flip(self.banditHurt1[i],1,0)
            #endif
        elif self.enemy == 2:
            if speed > 0:
                self.image = self.warlockHurt[i] #Right
            else:
                self.image = pygame.transform.flip(self.warlockHurt[i],1,0) #Left
            #endif
        elif self.enemy == 3:
            if speed > 0:
                self.image = self.rogueHurt[i] #Right
            else:
                self.image = pygame.transform.flip(self.rogueHurt[i],1,0) #Left
            #endif
        elif self.enemy == 0:
            if speed > 0:
                self.image = self.banditHurt2[i] #Right
            else:
                self.image = pygame.transform.flip(self.banditHurt2[i],1,0) #Left
            #endif
        #endif

    #endprocedure

    def Recover(self, speed, i):

        if self.enemy == 1:
            if speed > 0:
                self.image = self.banditRecover1[i]
            else:
                self.image = pygame.transform.flip(self.banditRecover1[i],1,0)
            #endif
        elif self.enemy == 0:
            if speed > 0:
                self.image = self.banditRecover2[i] #Right
            else:
                self.image = pygame.transform.flip(self.banditRecover2[i],1,0) #Left
            #endif
        #endif

    #endprocedure

    def Death(self, speed, i):

        if self.enemy == 1:
            if speed > 0:
                self.image = self.banditDeath1[i]
            else:
                self.image = pygame.transform.flip(self.banditDeath1[i],1,0)
            #endif
        elif self.enemy == 2:
            if speed > 0:
                self.image = self.warlockDeath[i] #Right
            else:
                self.image = pygame.transform.flip(self.warlockDeath[i],1,0) #Left
            #endif
        elif self.enemy == 3:
            if speed > 0:
                self.image = self.rogueDeath[i] #Right
            else:
                self.image = pygame.transform.flip(self.rogueDeath[i],1,0) #Left
            #endif
        elif self.enemy == 0:
            if speed > 0:
                self.image = self.banditDeath2[i] #Right
            else:
                self.image = pygame.transform.flip(self.banditDeath2[i],1,0) #Left
            #endif
        #endif

    #endprocedure

    def Spell(self, speed, i):

        if self.enemy == 3:
            if speed > 0:
                self.image = self.rogueSpell[i] #Right
            else:
                self.image = pygame.transform.flip(self.rogueSpell[i],1,0) #Left
            #endif
        #endif

    #endprocedure

    def SA(self, speed, i):

        if self.enemy == 3:
            if speed > 0:
                self.image = self.rogueSA[i] #Right
            else:
                self.image = pygame.transform.flip(self.rogueSA[i],1,0) #Left
            #endif
        #endif

    #endprocedure

#endclass
        
#Gameplay
def Game():

    game_over = False #Not finish
    
    clock = pygame.time.Clock()

    #Scripts
    script1 = []
    script2 = []
    script3 = []
    scriptExtra = []

    #Variables
    currency = [0,0,0,0] #Money
    live = [5] #Player's live
    timeUp = [0]
    gameMode = 1
    gameDifficulty = 1
    gameLevel = 1 #Game Level
    gamePhase = 1
    gameChat = 1
    gameOver = False
    gamePause = False
    advanceLevel = False
    ReadyToClick = False
    startReadScript = 0
    endReadScript = 0
    timer = TimerClass()

    #Setting Variables
    difficulty = 0

    #Game Level Variable
    currentSpeed = 0 #Used to determine animation direction
    horiSpeed = 0#Used to determine background move
    level = -1 #Determines level
    tutorialReset = True

    #Tutorial Level Variable
    dummyStartAttack = 0
    dummyEndAttack = 0

    #Level Load Variables
    gameInitiated = False #If game has been intiated
    levelCreated = False #If level has been created
    loadNum = 0 #Animation Count
    startLoadTime = 0 #Timer
    endLoadTime = 0
    currentFile = 0 #The player's file
    fileLoaded = False #If file has been loaded
    crownChecked = False
    levelToGo = 0
    tutorialLevel = False

    block1_list = pygame.sprite.Group() #Blocks list 1

    block2_list = pygame.sprite.Group() #Blocks list 2

    block3_list = pygame.sprite.Group() #Blocks list 3

    character1_list = pygame.sprite.Group()

    character2_list = pygame.sprite.Group()

    character3_list = pygame.sprite.Group()

    ground1_list = pygame.sprite.Group()

    ground2_list = pygame.sprite.Group()

    ground3_list = pygame.sprite.Group()

    tutorialBlock_list = pygame.sprite.Group() #Block tutorial list

    player_list = pygame.sprite.Group() #Player's list

    enemy_list = pygame.sprite.Group() #Enemy's list

    warlock_list = pygame.sprite.Group() #Warlock

    rogue_list = pygame.sprite.Group() #Rogue

    rogueAttack_list = pygame.sprite.Group() #Rogue Attack

    tutorialEnemy_list = pygame.sprite.Group() #Enemy's tutorial list

    banditGroup1_list = pygame.sprite.Group()

    banditGroup2_list = pygame.sprite.Group()

    banditGroup3_list = pygame.sprite.Group()

    startEnd_list = pygame.sprite.Group() #The area determines the start and end of a level

    levelOne_list = pygame.sprite.Group() #All visible object lists in level one

    levelTwo_list = pygame.sprite.Group() #All visible object lists in level two

    levelThree_list = pygame.sprite.Group() #All visible object lists in level three

    menu_list = pygame.sprite.Group() #All visible objects in menu

    file_list = pygame.sprite.Group() #All visible objects in file

    playerAttack_list = pygame.sprite.Group() #Player's attack

    enemyAttack_list = pygame.sprite.Group() #Enemy's attack

    button_list = pygame.sprite.Group() #Buttons

    pauseButton_list = pygame.sprite.Group() #Pause Button

    optionBlock_list = pygame.sprite.Group() 

    panelButton_list = pygame.sprite.Group()

    nextButton_list = pygame.sprite.Group() #Next Button

    item_list = pygame.sprite.Group() #Group of items

    crown_list = pygame.sprite.Group() #Crown

    loading_list = pygame.sprite.Group() #Loading screen

    setting_list = pygame.sprite.Group() #Setting screen

    easy_list = pygame.sprite.Group() #Easy

    hard_list = pygame.sprite.Group() #Hard

    background1_list = pygame.sprite.Group() #Backgrounds

    cloud_list = pygame.sprite.Group() #Clouds

    tutorial_list = pygame.sprite.Group() #Tutorial

    coin_list = pygame.sprite.Group() #Coins

    thousand_list = pygame.sprite.Group()

    hundred_list = pygame.sprite.Group()

    ten_list = pygame.sprite.Group()

    one_list = pygame.sprite.Group()

    wordBox_list = pygame.sprite.Group() #WordBox

    currentLine_list = pygame.sprite.Group() #Current Line

    CreateLoad(loading_list)

    while not game_over:
        
    # -- User input and controls
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()#Track Mouse' Position
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.MOUSEBUTTONDOWN: #Mouse Click
                if level == 0 and pos[0] >= 595.5 and pos[1] >= 420 and pos[0] <= 904.5 and pos[1] <= 513: #Select save files
                    level = 3 #Start game
                    tutorialLevel = False
                    fileLoaded = False
                elif level == 0 and pos[0] >= 442.5 and pos[1] >= 560 and pos[0] <= 1057.5 and pos[1] <= 653: #Select Settings
                    level = 1 #Settings
                elif level == 0 and pos[0] >= 430.5 and pos[1] >= 700 and pos[0] <= 1069.5 and pos[1] <= 793: #Select tutorial
                    levelToGo = 2
                    level = -1 #Tutorial
                    tutorialLevel = True
                    for dummy in tutorialEnemy_list:
                        dummy.AttackStance(1)
                        dummy.ChangeSpeed(1)
                        dummy.ChangeSpeed(2)
                        dummy.rect.x = 295
                    #endfor
                    player.Freeze(0)
                    player.FreezeTrigger(0)
                    fileLoaded = True
                elif level == 1 and pos[0] >= 529.5 and pos[1] >= 300 and pos[0] <= 970.5 and pos[1] <= 420: #Select Difficulty
                    if difficulty == 0:
                        difficulty = 1
                        for easy in easy_list:
                            setting_list.remove(easy)
                        #endfor
                        for hard in hard_list:
                            setting_list.add(hard)
                        #endfor
                    else:
                        difficulty = 0
                        for easy in easy_list:
                            setting_list.add(easy)
                        #endfor
                        for hard in hard_list:
                            setting_list.remove(hard)
                        #endfor
                    #endif
                elif level == 3 and pos[0] >= 249.5 and pos[1] >= 680.5 and pos[0] <= 410.5 and pos[1] <= 711.5: #Select file 1
                    level = -1
                    levelToGo = 4
                    currentFile = 1
                    player.FreezeTrigger(0)
                elif level == 3 and pos[0] >= 669.5 and pos[1] >= 680.5 and pos[0] <= 830.5 and pos[1] <= 711.5: #Select file 2
                    level = -1
                    levelToGo = 4
                    currentFile = 2
                    player.FreezeTrigger(0)
                elif level == 3 and pos[0] >= 1089.5 and pos[1] >= 680.5 and pos[0] <= 1250.5 and pos[1] <= 711.5: #Select file 3
                    level = -1
                    levelToGo = 4
                    currentFile = 3
                    player.FreezeTrigger(0)
                elif level == 3 and pos[0] >= 50 and pos[1] >= 820 and pos[0] <= 156 and pos[1] <= 851: #Go back to menu
                    level = 0
                    fileLoaded = True
                elif level == 1 and pos[0] >= 50 and pos[1] >= 820 and pos[0] <= 156 and pos[1] <= 851: #Go back to menu
                    level = 0
                elif level == 2 and pos[0] >= 1430 and pos[1] >= 10 and pos[0] <= 1490 and pos[1] <= 70: #Go back to menu
                    levelToGo = 0
                    tutorialLevel = True
                    fileLoaded = False
                    level = -1
                    player.Reset()
                    player.ResetLive([5])
                    currency[0] = 0
                    currency[1] = 0
                    currency[2] = 0
                    currency[3] = 0
                elif level == 4 and pos[0] >= 1430 and pos[1] >= 10 and pos[0] <= 1490 and pos[1] <= 70 and not gamePause and not gameOver and not advanceLevel: #Pause game
                    gamePause = True
                    for optionBlock in optionBlock_list:
                        levelOne_list.add(optionBlock)
                        levelTwo_list.add(optionBlock)
                        levelThree_list.add(optionBlock)
                    #endfor
                    for button in panelButton_list:
                        levelOne_list.add(button)
                        levelTwo_list.add(button)
                        levelThree_list.add(button)
                    #endfor
                    for button in pauseButton_list:
                        levelOne_list.remove(button)
                        levelTwo_list.remove(button)
                        levelThree_list.remove(button)
                    #endfor
                    if gameLevel == 1:
                        for character in character1_list:
                            character.Freeze(1)
                        #endfor
                        player.FreezeTrigger(1)
                    #endif
                elif level == 4 and pos[0] >= 1068 and pos[1] >= 234 and pos[0] <= 1128 and pos[1] <= 294 and gamePause and not gameOver and not advanceLevel: #Continue
                    gamePause = False
                    for optionBlock in optionBlock_list:
                        levelOne_list.remove(optionBlock)
                        levelTwo_list.remove(optionBlock)
                        levelThree_list.remove(optionBlock)
                    #endfor
                    for button in panelButton_list:
                        levelOne_list.remove(button)
                        levelTwo_list.remove(button)
                        levelThree_list.remove(button)
                    #endfor
                    for button in pauseButton_list:
                        levelOne_list.add(button)
                        levelTwo_list.add(button)
                        levelThree_list.add(button)
                    #endfor
                    if gameLevel == 1:
                        for character in character1_list:
                            character.Freeze(0)
                        #endfor
                        player.FreezeTrigger(0)
                    #endif
                elif level == 4 and pos[0] >= 700 and pos[1] >= 530 and pos[0] <= 800 and pos[1] <= 570 and gamePause and not gameOver and not advanceLevel: #Quit game
                    levelToGo = 0
                    level = -1
                    fileLoaded = False
                    timeUp[0] = 0
                    gamePhase = 1
                    gameChat = 1
                    gameOver = False
                    gamePause = False
                    ReadyToClick = False
                    startReadScript = 0
                    endReadScript = 0
                    player.Reset()
                    player.ResetLive([5])
                    if gameLevel == 1:
                        for block in block1_list:
                            block.Reset()
                        #endfpr
                        for character in character1_list:
                            character.Reset()
                        #endfor
                        for optionBlock in optionBlock_list:
                            levelOne_list.remove(optionBlock)
                        #endfor
                        for button in panelButton_list:
                            levelOne_list.remove(button)
                        #endfor
                        for button in pauseButton_list:
                            levelOne_list.add(button)
                        #endfor
                        for ground in ground1_list:
                            ground.Update(0)
                        #endfor
                        DrawOrRemove(0, levelOne_list, nextButton_list)
                        DrawOrRemove(0, levelOne_list, currentLine_list)
                        DrawOrRemove(0, levelOne_list, wordBox_list)
                    #endif
                elif level == 4 and pos[0] >= 1195 and pos[1] >= 850 and pos[0] <= 1255 and pos[1] <= 870 and not gamePause:
                    if ReadyToClick:
                        gameChat += 1
                        ReadyToClick = False
                    #endif
                #endif
            elif level >= 2 and event.type == pygame.KEYDOWN: #Press Key Down
                if event.key == pygame.K_SPACE:
                    for player in player_list:
                        player.AttackTrigger()
                    #endfor
                if event.key == pygame.K_w:
                    for player in player_list:
                        player.Jump()
                    #endfor
                if event.key == pygame.K_a:
                    for player in player_list:
                        player.ChangeSpeed(0)
                        player.KeepMove(1)
                    #endfor
                    currentSpeed = -1
                    horiSpeed = -1
                if event.key == pygame.K_d:
                    for player in player_list:
                        player.ChangeSpeed(1)
                        player.KeepMove(1)
                    #endfor
                    currentSpeed = 1
                    horiSpeed = 1
                if event.key == pygame.K_s:
                    for player in player_list:
                        player.BlockTrigger(1)
                    #endfor
                if event.key == pygame.K_LSHIFT:
                    for player in player_list:
                        player.RollTrigger()
                    #endfor
                #endif
            elif level >= 2 and event.type == pygame.KEYUP: #Release Key
                if event.key == pygame.K_a and currentSpeed < 0:
                    for player in player_list:
                        player.ChangeSpeed(2)
                        player.KeepMove(0)
                    #endfor
                    horiSpeed = 0
                if event.key == pygame.K_d and currentSpeed > 0:
                    for player in player_list:
                        player.ChangeSpeed(2)
                        player.KeepMove(0)
                    #endfor
                    horiSpeed = 0
                if event.key == pygame.K_s:
                    for player in player_list:
                        player.BlockTrigger(0)
                    #endfor
                #endif
            #endif
        #endfor

        if level == 0:

            screen.fill(BLACK)

            for button in button_list:
                
                button.Change(pos, level)

            #endfor

            menu_list.draw(screen) #Display all visible objects

        elif level == -1:

            screen.fill(BLACK)

            if startLoadTime == 0: #If start timer has not started yet

                startLoadTime = pygame.time.get_ticks() #Record current time

            #endif

            if gameInitiated == False:

                endLoadTime = pygame.time.get_ticks() #Record current time
                if endLoadTime - startLoadTime >= 700:

                    startLoadTime = endLoadTime #Reset Timer
                    for load in loading_list:

                        load.Animation(loadNum) #Animation
                        loadNum += 1

                        if loadNum == 4: #If animation finished

                            gameInitiated = True #Reset Loading
                            loadNum = 0
                            load.Animation(loadNum)
                            startLoadTime = 0
                            endLoadTime = 0
                            fileLoaded = False
                            level = 0 #Go to menu

                        #endif

                    #endfor
                            
                #endif
                
                loading_list.draw(screen) #Display objects

                if levelCreated == False:

                    levelCreated = True

                    CreateFile(file_list, button_list, item_list, crown_list)
                    CreateMenu(menu_list, button_list)
                    CreateSettings(setting_list, button_list, easy_list, hard_list)
                    CreateLevelOnePlatform(block1_list, levelOne_list, startEnd_list, background1_list, cloud_list, ground1_list) #Create Level One Platforms
                    CreatePause(button_list, optionBlock_list, pauseButton_list, panelButton_list, levelOne_list, levelTwo_list, levelThree_list)
                    CreateTutorialPlatform(tutorialBlock_list, tutorial_list, button_list)
                    CreateCharacters1(player_list, playerAttack_list, tutorialEnemy_list, tutorial_list, levelOne_list, levelTwo_list, levelThree_list, enemyAttack_list, character1_list)
                    CreateCharacters2(levelOne_list, enemy_list, warlock_list, wordBox_list, nextButton_list, rogue_list, enemyAttack_list, rogueAttack_list, banditGroup1_list, banditGroup2_list, character1_list)
                    CreateMoney(tutorial_list, levelOne_list, levelTwo_list, levelThree_list, thousand_list, hundred_list, ten_list, one_list)
                    for player in player_list:
                        player.DrawOnCanvas(tutorial_list, levelOne_list, levelTwo_list, levelThree_list)
                    #endfor
                    ReadScript(script1, script2, script3)

                #endif

            #endif
            elif gameInitiated == True and tutorialLevel == False:

                endLoadTime = pygame.time.get_ticks() #Record current time
                if endLoadTime - startLoadTime >= 700:

                    startLoadTime = endLoadTime #Reset Timer
                    for load in loading_list:

                        load.Animation(loadNum) #Animation
                        loadNum += 1

                        if loadNum == 4: #If animation finished

                            loadNum = 0
                            load.Animation(loadNum)
                            startLoadTime = 0
                            endLoadTime = 0
                            level = levelToGo #Go to gameplay
                            fileLoaded = False
                            crownChecked = False

                        #endif
                            
                    #endfor

                #endif

                loading_list.draw(screen) #Display objects

                if crownChecked == False: #Crown

                    crownChecked = True
                    SetCrown(crown_list)

                #endif

                if not fileLoaded and not tutorialLevel:

                    fileLoaded = True
                    
                    if currentFile == 1:

                        #Open File 1
                        f = open("Game_Files/File1.txt","r+") #Open file 1
                        lines = f.readlines() #All data
                        f.close() #Close

                    elif currentFile == 2:

                        #Open File 2
                        f = open("Game_Files/File2.txt","r+") #Open file 2
                        lines = f.readlines() #All data
                        f.close() #Close

                    elif currentFile == 3:

                        #Open File 3
                        f = open("Game_Files/File3.txt","r+") #Open file 3
                        lines = f.readlines() #All data
                        f.close() #Close

                    #endif

                    #Set currency
                    currency[3] = int(lines[0][3])
                    currency[2] = int(lines[0][2])
                    currency[1] = int(lines[0][1])
                    currency[0] = int(lines[0][0])

                    #Set live
                    live[0] = int(lines[1].rstrip("\n"))

                    for player in player_list:
                        player.ResetLive(live)
                        player.FreezeTrigger(1)
                    #endfor

                    #Set Level
                    gameLevel = int(lines[2][0])

                #endif

            elif tutorialLevel == True:

                endLoadTime = pygame.time.get_ticks() #Record current time
                if endLoadTime - startLoadTime >= 500:

                    startLoadTime = endLoadTime #Reset Timer
                    for load in loading_list:

                        load.Animation(loadNum) #Animation
                        loadNum += 1

                        if loadNum == 4: #If animation finished

                            loadNum = 0
                            load.Animation(loadNum)
                            startLoadTime = 0
                            endLoadTime = 0
                            level = levelToGo #Go to gameplay
                            fileLoaded = False
                            crownChecked = False

                        #endif
                            
                    #endfor

                #endif

                loading_list.draw(screen) #Display objects

            #endif

        elif level == 1: #Settings

            screen.fill(BLACK)

            for button in button_list:

                button.Change(pos, level)

            #endfor

            setting_list.draw(screen) #Display objects

        elif level == 2: #Tutorial

            screen.fill(WHITE)

            if tutorialReset == True:
                for cloud in cloud_list:
                    cloud.rect.x = 0
                #endfor
                tutorialReset = False
            #endif

            for thousand in thousand_list:
                thousand.Update(currency[0])
            #endfor
            for hundred in hundred_list:
                hundred.Update(currency[1])
            #endfor
            for ten in ten_list:
                ten.Update(currency[2])
            #endfor
            for one in one_list:
                one.Update(currency[3])
            #endfor

            for button in button_list: #Button Change

                button.Change(pos, level)

            #endfor

            for cloud in cloud_list:

                cloud.CloudUpdate()

            #endfor

            for coin in coin_list:

                coin.Change()
                coin.CoinUpdate(player_list, block1_list, tutorialBlock_list, tutorial_list, levelOne_list, coin_list, currency)

            #endfor

            #Enemy Movement
            for enemy in tutorialEnemy_list:

                dummyEndAttack = pygame.time.get_ticks()
                if dummyEndAttack - dummyStartAttack > 3000:
                    dummyStartAttack = dummyEndAttack
                    enemy.AttackTrigger()
                #endif

                enemy.Attack()
                enemy.MoveHori(block1_list, block2_list, block3_list, tutorialBlock_list, level, gameLevel)
                enemy.AttackChecker()
                enemy.MoveVert(block1_list, block2_list, block3_list, tutorialBlock_list, level, gameLevel)
                enemy.Revive()
                enemy.Hurt()
                enemy.EnemyAttackDetection(playerAttack_list)
                enemy.Health(coin_list, tutorial_list, level, gameLevel)
                enemy.Animation()

            #endfor

            #Player Movement
            for player in player_list:

                #Detection
                player.EnemyAttackDetection(enemyAttack_list)
                #Blocked
                player.Blocked()
                #Hurt
                player.Hurt()
                #Attack
                player.Attack()
                #Roll
                player.Roll()
                #Horizontal Movement
                player.MoveHori(tutorialBlock_list) #Player move horizontally
                #Attack Checker
                player.AttackChecker()
                #Vertical Movement
                player.MoveVert(tutorialBlock_list)
                #Death
                player.Revive(live)
                #Health
                player.Health(live)
                #Animation
                player.Animation()

            #endfor

            tutorial_list.draw(screen) #Display all visible objects

        elif level == 3: #Save Files

            screen.fill(BLACK)

            for button in button_list:

                button.Change(pos, level)

            #endfor

            for item in item_list:

                item.Change()

            #endfor

            file_list.draw(screen) #Display all visible objects

        elif level == 4: #Gameplay

            screen.fill(WHITE)

            if not gamePause:

                if gameLevel == 1: #Level 1------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                    
                    for cloud in cloud_list: #Cloud

                        cloud.CloudUpdate()

                    #endfor

                    for button in button_list: #Button Change

                        button.Change(pos, level)

                    #endfor

                    for coin in coin_list:

                        coin.Change()
                        coin.CoinUpdate(player_list, block1_list, tutorialBlock_list, tutorial_list, levelOne_list, coin_list, currency)

                    #endfor

                    for thousand in thousand_list:
                        thousand.Update(currency[0])
                    #endfor
                    for hundred in hundred_list:
                        hundred.Update(currency[1])
                    #endfor
                    for ten in ten_list:
                        ten.Update(currency[2])
                    #endfor
                    for one in one_list:
                        one.Update(currency[3])
                    #endfor

                    #Player Movement
                    for player in player_list:

                        #Detection
                        player.EnemyAttackDetection(enemyAttack_list)
                        if gamePhase == 19:
                            player.RogueDetection(rogueAttack_list)
                        #endif
                        #Blocked
                        player.Blocked()
                        #Hurt
                        player.Hurt()
                        #Attack
                        player.Attack()
                        #Roll
                        player.Roll()
                        #Horizontal Movement
                        if gamePhase != 9 and gamePhase != 10 and gamePhase != 16 and gamePhase != 17 and gamePhase != 20 and gamePhase != 21:
                            player.MoveHori(block1_list) #Player move horizontally
                        else:
                            player.MoveHori2()
                        #endif
                        #Attack Checker
                        player.AttackChecker()
                        #Vertical Movement
                        player.MoveVert(block1_list)
                        #Death
                        player.Revive(live)
                        #Health
                        player.Health(live)
                        #Animation
                        player.Animation()

                    #endfor

                    #Warlock
                    if gamePhase <= 5:
                        for warlock in warlock_list:
                            warlock.MoveHori(block1_list)
                            warlock.MoveVert(block1_list)
                            warlock.Hurt()
                            warlock.Health()
                            warlock.EnemyAttackDetection(rogueAttack_list)
                            warlock.Animation()
                        #endfor
                    #endif

                    #Rogue
                    if gamePhase <= 5 or gamePhase >= 10:
                        for rogue in rogue_list:
                            if gamePhase == 19:
                                rogue.Control(player.rect.x)
                            #endif
                            rogue.MoveHori(block1_list)
                            rogue.MoveVert(block1_list)
                            rogue.Hurt()
                            rogue.EnemyAttackDetection(playerAttack_list)
                            rogue.Attack()
                            rogue.Health(levelOne_list, coin_list)
                            rogue.SA()
                            rogue.Animation()
                        #endfor
                    #endif

                    if gamePhase >= 5 and gamePhase <= 8:

                        #Bandit Movement
                        for enemy in banditGroup1_list:

                            enemy.Attack()
                            enemy.MoveHori(block1_list, block2_list, block3_list, tutorialBlock_list, level, gameLevel)
                            enemy.AttackChecker()
                            enemy.MoveVert(block1_list, block2_list, block3_list, tutorialBlock_list, level, gameLevel)
                            if gamePhase == 8:
                                enemy.Control(player_list)
                            #endif
                            enemy.Hurt()
                            enemy.EnemyAttackDetection(playerAttack_list)
                            enemy.Health(coin_list, levelOne_list, level, gameLevel)
                            enemy.Animation()

                        #endfor

                    #endif

                    if gamePhase >= 10 and gamePhase <= 15:

                        #Bandit Movement
                        for enemy in banditGroup2_list:

                            enemy.Attack()
                            enemy.MoveHori(block1_list, block2_list, block3_list, tutorialBlock_list, level, gameLevel)
                            enemy.AttackChecker()
                            enemy.MoveVert(block1_list, block2_list, block3_list, tutorialBlock_list, level, gameLevel)
                            if gamePhase == 15:
                                enemy.Control(player_list)
                            #endif
                            enemy.Hurt()
                            enemy.EnemyAttackDetection(playerAttack_list)
                            enemy.Health(coin_list, levelOne_list, level, gameLevel)
                            enemy.Animation()

                        #endfor

                    #endif

                    if gamePhase == 1:
                        #Warlock
                        if gameChat == 1:
                            DrawOrRemove(1, levelOne_list, wordBox_list)
                            WriteWords(1, script1[0], 0, 815, file_list, levelOne_list, levelTwo_list, levelThree_list, currentLine_list, 4, 1, 0)
                            gameChat = 2
                        elif gameChat == 2:
                            if timeUp[0] == 0 and not ReadyToClick:
                                timer.Counter(2000, timeUp)
                            elif timeUp[0] == 1 and not ReadyToClick:
                                timeUp[0] = 0
                                ReadyToClick = True
                                DrawOrRemove(1, levelOne_list, nextButton_list)
                            #endif
                            for button in nextButton_list:
                                button.Change(pos, level)
                            #endfor
                        elif gameChat == 3:
                            DrawOrRemove(0, levelOne_list, nextButton_list)
                            DrawOrRemove(0, levelOne_list, currentLine_list)
                            WriteWords(1, script1[1], 0, 815, file_list, levelOne_list, levelTwo_list, levelThree_list, currentLine_list, 4, 1, 0)
                            gameChat = 4
                        elif gameChat == 4:
                            if timeUp[0] == 0 and not ReadyToClick:
                                timer.Counter(2000, timeUp)
                            elif timeUp[0] == 1 and not ReadyToClick:
                                timeUp[0] = 0
                                ReadyToClick = True
                                DrawOrRemove(1, levelOne_list, nextButton_list)
                            #endif
                            for button in nextButton_list:
                                button.Change(pos, level)
                            #endfor
                        elif gameChat == 5:
                            DrawOrRemove(0, levelOne_list, nextButton_list)
                            DrawOrRemove(0, levelOne_list, currentLine_list)
                            WriteWords(1, script1[2], 0, 815, file_list, levelOne_list, levelTwo_list, levelThree_list, currentLine_list, 4, 1, 0)
                            gameChat = 6
                        elif gameChat == 6:
                            if timeUp[0] == 0 and not ReadyToClick:
                                timer.Counter(2000, timeUp)
                            elif timeUp[0] == 1 and not ReadyToClick:
                                timeUp[0] = 0
                                ReadyToClick = True
                                DrawOrRemove(1, levelOne_list, nextButton_list)
                            #endif
                            for button in nextButton_list:
                                button.Change(pos, level)
                            #endfor
                        elif gameChat == 7:
                            DrawOrRemove(0, levelOne_list, nextButton_list)
                            DrawOrRemove(0, levelOne_list, currentLine_list)
                            DrawOrRemove(0, levelOne_list, wordBox_list)
                            gamePhase = 2
                            gameChat = 1
                            for warlock in warlock_list:
                                warlock.ChangeSpeed(1)
                            #endfor
                            for rogue in rogue_list:
                                rogue.ChangeSpeed(0)
                            #endfor
                        #endif
                    elif gamePhase == 2:
                        if warlock.rect.x >= 675:
                            warlock.rect.x = 675
                            for warlock in warlock_list:
                                warlock.ChangeSpeed(2)
                            #endfor
                            for rogue in rogue_list:
                                rogue.ChangeSpeed(2)
                                rogue.SATrigger(690)
                            #endfor
                            gamePhase = 3
                        #endif
                    elif gamePhase == 3:
                        if timeUp[0] == 0:
                            timer.Counter(1900, timeUp)
                        elif timeUp[0] == 1:
                            timeUp[0] = 0
                            gamePhase = 4
                            endTimer = 0
                            startTimer = 0
                        #endif
                    elif gamePhase == 4:
                        if gameChat == 1:
                            DrawOrRemove(1, levelOne_list, wordBox_list)
                            WriteWords(1, script1[3], 0, 815, file_list, levelOne_list, levelTwo_list, levelThree_list, currentLine_list, 4, 1, 0)
                            gameChat = 2
                        elif gameChat == 2:
                            if timeUp[0] == 0 and not ReadyToClick:
                                timer.Counter(2000, timeUp)
                            elif timeUp[0] == 1 and not ReadyToClick:
                                timeUp[0] = 0
                                ReadyToClick = True
                                DrawOrRemove(1, levelOne_list, nextButton_list)
                            #endif
                            for button in nextButton_list:
                                button.Change(pos, level)
                            #endfor
                        elif gameChat == 3:
                            DrawOrRemove(0, levelOne_list, nextButton_list)
                            DrawOrRemove(0, levelOne_list, currentLine_list)
                            DrawOrRemove(0, levelOne_list, wordBox_list)
                            gameChat = 0
                            gamePhase = 5
                            gameChat = 1
                        #endif
                    elif gamePhase == 5:
                        for bandit in banditGroup1_list:
                            bandit.ChangeSpeed(0)
                        #endfor
                        for rogue in rogue_list:
                            rogue.ChangeSpeed(1)
                        #endfor
                        for rogue in rogue_list:
                            if rogue.rect.x >= 1700:
                                timeUp[0] = 0
                                gamePhase = 6
                                endTimer = 0
                                startTimer = 0
                                for bandit in banditGroup1_list:
                                    bandit.ChangeSpeed(2)
                                #endfor
                                rogue.ChangeSpeed(0)
                                rogue.ChangeSpeed(2)
                                rogue.rect.x = 2210
                                rogue.rect.y = 290
                                rogue.Animation()
                            #endif
                        #endfor
                    elif gamePhase == 6:
                        if timeUp[0] == 0:
                            timer.Counter(600, timeUp)
                        elif timeUp[0] == 1:
                            timeUp[0] = 0
                            gamePhase = 7
                            endTimer = 0
                            startTimer = 0
                            for enemy in banditGroup1_list:
                                enemy.AttackStance(1)
                            #endfor
                        #endif
                    elif gamePhase == 7:
                        if timeUp[0] == 0:
                            timer.Counter(1200, timeUp)
                        elif timeUp[0] == 1:
                            timeUp[0] = 0
                            gamePhase = 8
                            for player in player_list:
                                player.FreezeTrigger(0)
                            #endfor
                        #endif
                    elif gamePhase == 8:
                        if currency[3] == 6 and live[0] > 0:
                            if timeUp[0] == 0:
                                for player in player_list:
                                    player.FreezeTrigger(0)
                                    player.ChangeSpeed(2)
                                    player.FreezeTrigger(1)
                                #endfor
                                timer.Counter(1200, timeUp)
                            elif timeUp[0] == 1:
                                gamePhase = 9
                                for player in player_list:
                                    player.FreezeTrigger(0)
                                    player.ChangeSpeed(1)
                                    player.FreezeTrigger(1)
                                #endfor
                            #endif
                        #endif
                        if live[0] == 0:
                            gameOver = True
                        #endif
                    elif gamePhase == 9:
                        if player.rect.x >= 1550:
                            player.FreezeTrigger(0)
                            player.ChangeSpeed(2)
                            player.FreezeTrigger(1)
                            player.rect.x = 1550
                            gamePhase = 10
                        #endif
                    elif gamePhase == 10:
                        if player.rect.x > 50:
                            player.rect.x -= 10
                            for block in block1_list:
                                block.rect.x -= 10
                            #endfor
                            for warlock in warlock_list:
                                warlock.rect.x -= 10
                                warlock.Animation()
                            #endfor
                            for enemy in banditGroup1_list:
                                enemy.rect.x -= 10
                                enemy.Animation()
                            #endfor
                            for rogue in rogue_list:
                                rogue.rect.x -= 10
                                rogue.Animation()
                            #endfor
                            for bandit in banditGroup2_list:
                                bandit.rect.x -= 10
                            #endfor
                            for background in background1_list:
                                background.BackUpdate()
                            #endfor
                            for ground in ground1_list:
                                ground.Update(1)
                            #endfor
                        elif player.rect.x == 50:
                            gamePhase = 11
                            for ground in ground1_list:
                                ground.Update(0)
                            #endfor
                        #endif
                    elif gamePhase == 11:
                        if gameChat == 1:
                            DrawOrRemove(1, levelOne_list, wordBox_list)
                            WriteWords(1, script1[4], 0, 815, file_list, levelOne_list, levelTwo_list, levelThree_list, currentLine_list, 4, 1, 0)
                            gameChat = 2
                        elif gameChat == 2:
                            if timeUp[0] == 0 and not ReadyToClick:
                                timer.Counter(2000, timeUp)
                            elif timeUp[0] == 1 and not ReadyToClick:
                                timeUp[0] = 0
                                ReadyToClick = True
                                DrawOrRemove(1, levelOne_list, nextButton_list)
                            #endif
                            for button in nextButton_list:
                                button.Change(pos, level)
                            #endfor
                        elif gameChat == 3:
                            DrawOrRemove(0, levelOne_list, nextButton_list)
                            DrawOrRemove(0, levelOne_list, currentLine_list)
                            DrawOrRemove(0, levelOne_list, wordBox_list)
                            gameChat = 0
                            gamePhase = 12
                            gameChat = 1
                        #endif
                    elif gamePhase == 12:
                        for rogue in rogue_list:
                            rogue.SATrigger(1800)
                        #endfor
                        gamePhase = 13
                    elif gamePhase == 13:
                        if timeUp[0] == 0:
                            timer.Counter(1000, timeUp)
                        elif timeUp[0] == 1:
                            timeUp[0] = 0
                            gamePhase = 14
                            for enemy in banditGroup2_list:
                                enemy.AttackStance(1)
                            #endfor
                        #endif
                    elif gamePhase == 14:
                        if timeUp[0] == 0:
                            timer.Counter(600, timeUp)
                        elif timeUp[0] == 1:
                            timeUp[0] = 0
                            gamePhase = 15
                            for player in player_list:
                                player.FreezeTrigger(0)
                            #endfor
                        #endif
                    elif gamePhase == 15:
                        if currency[2] == 1 and currency[3] == 8 and live[0] > 0:
                            if timeUp[0] == 0:
                                for player in player_list:
                                    player.FreezeTrigger(0)
                                    player.ChangeSpeed(2)
                                    player.FreezeTrigger(1)
                                #endfor
                                timer.Counter(1200, timeUp)
                            elif timeUp[0] == 1:
                                gamePhase = 16
                                for player in player_list:
                                    player.FreezeTrigger(0)
                                    player.ChangeSpeed(1)
                                    player.FreezeTrigger(1)
                                #endfor
                            #endif
                        #endif
                        if live[0] == 0:
                            gameOver = True
                        #endif
                    elif gamePhase == 16:
                        if player.rect.x >= 1550:
                            player.FreezeTrigger(0)
                            player.ChangeSpeed(2)
                            player.FreezeTrigger(1)
                            player.rect.x = 1550
                            for rogue in rogue_list:
                                rogue.ChangeSpeed(0)
                                rogue.ChangeSpeed(2)
                                rogue.Unrandom()
                                rogue.rect.x = 2870
                                rogue.rect.y = 710
                            #endfor
                            gamePhase = 17
                        #endif
                    elif gamePhase == 17:
                        if player.rect.x > 50:
                            player.rect.x -= 10
                            for block in block1_list:
                                block.rect.x -= 10
                            #endfor
                            for rogue in rogue_list:
                                rogue.rect.x -= 10
                                rogue.Animation()
                            #endfor
                            for bandit in banditGroup2_list:
                                bandit.rect.x -= 10
                                bandit.Animation()
                            #endfor
                            for background in background1_list:
                                background.BackUpdate()
                            #endfor
                            for ground in ground1_list:
                                ground.Update(1)
                            #endfor
                        elif player.rect.x == 50:
                            gamePhase = 18
                            for ground in ground1_list:
                                ground.Update(0)
                            #endfor
                        #endif
                    elif gamePhase == 18:
                        if gameChat == 1:
                            DrawOrRemove(1, levelOne_list, wordBox_list)
                            WriteWords(1, script1[5], 0, 815, file_list, levelOne_list, levelTwo_list, levelThree_list, currentLine_list, 4, 1, 0)
                            gameChat = 2
                        elif gameChat == 2:
                            if timeUp[0] == 0 and not ReadyToClick:
                                timer.Counter(2000, timeUp)
                            elif timeUp[0] == 1 and not ReadyToClick:
                                timeUp[0] = 0
                                ReadyToClick = True
                                DrawOrRemove(1, levelOne_list, nextButton_list)
                            #endif
                            for button in nextButton_list:
                                button.Change(pos, level)
                            #endfor
                        elif gameChat == 3:
                            DrawOrRemove(0, levelOne_list, nextButton_list)
                            DrawOrRemove(0, levelOne_list, currentLine_list)
                            WriteWords(1, script1[6], 0, 815, file_list, levelOne_list, levelTwo_list, levelThree_list, currentLine_list, 4, 1, 0)
                            gameChat = 4
                        elif gameChat == 4:
                            if timeUp[0] == 0 and not ReadyToClick:
                                timer.Counter(2000, timeUp)
                            elif timeUp[0] == 1 and not ReadyToClick:
                                timeUp[0] = 0
                                ReadyToClick = True
                                DrawOrRemove(1, levelOne_list, nextButton_list)
                            #endif
                            for button in nextButton_list:
                                button.Change(pos, level)
                            #endfor
                        elif gameChat == 5:
                            DrawOrRemove(0, levelOne_list, nextButton_list)
                            DrawOrRemove(0, levelOne_list, currentLine_list)
                            DrawOrRemove(0, levelOne_list, wordBox_list)
                            gamePhase = 19
                            gameChat = 1
                            player.FreezeTrigger(0)
                        #endif
                    elif gamePhase == 19:
                        if currency[2] == 2 and currency[3] == 6 and live[0] > 0:
                            if timeUp[0] == 0:
                                for player in player_list:
                                    player.FreezeTrigger(0)
                                    player.ChangeSpeed(2)
                                    player.FreezeTrigger(1)
                                #endfor
                                timer.Counter(1200, timeUp)
                            elif timeUp[0] == 1:
                                gamePhase = 20
                                for player in player_list:
                                    player.FreezeTrigger(0)
                                    player.ChangeSpeed(1)
                                    player.FreezeTrigger(1)
                                #endfor
                            #endif
                        #endif
                        if live[0] <= 0:
                            gameOver = True
                        #endif
                    elif gamePhase == 20:
                        if player.rect.x >= 1550:
                            player.FreezeTrigger(0)
                            player.ChangeSpeed(2)
                            player.FreezeTrigger(1)
                            player.rect.x = 1550
                            gamePhase = 21
                        #endif
                    levelOne_list.draw(screen) #Display all visible objects

                #endif

            elif gamePause:

                for button in panelButton_list:

                    button.Change(pos, level)

                #endfor

                if gameLevel == 1:
                    levelOne_list.draw(screen) #Display all visible objects
                #endif

            #endif

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
pygame.display.set_caption("HEROTALE")
    
### -- Game Loop

Game() #Calls game

pygame.quit()
