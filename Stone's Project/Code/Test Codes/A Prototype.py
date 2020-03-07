import pygame
from random import randint
# -- Global Constants

f = open("Blocks.txt","r+")
nodes = f.readlines()
nodesNum = len(nodes)
f.close()

#Images

# -- Colours

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

# -- Classes

#Text_Object
def text_objects(msg, color, size):
    if size == "small":
        font = pygame.font.Font('freesansbold.ttf',40)
        textSurface = font.render(msg, True, color)
    if size == "medium":
        medfont = pygame.font.Font('freesandbolf,ttf',60)
        textSurface = medfont.render(msg, True, color)
    if size == "large":
        largefont = pygame.font.Font('freesandbolf,ttf',80)
        textSurface = largefont.render(msg, True, color)
    #endif
    return textSurface, textSurface.get_rect()
#endfunction

#Button
def buttonText(msg, color, x, y, width, height, size):
    textSurf, textRect = text_objects(msg,color,size)
    textRect.center = ((x+(width/2)), y+(height/2))
    screen.blit(textSurf, textRect)
#endprocedure

def Text(Size,Colour,x,y,text):
    font = pygame.font.Font('freesansbold.ttf',Size)
    text = font.render(text, True, Colour, BLACK) 
    textRect = text.get_rect()
    textRect.center = (x,y)
    screen.blit(text, textRect)
#endprocedure

class Block(pygame.sprite.Sprite):
    def __init__(self,colour,width,height):
        super().__init__()
        
        self.image = pygame.Surface([width,height])
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        
    #endprocedure

#endclass

class InviBlock(pygame.sprite.Sprite):
    def __init__(self,width,height):
        super().__init__()
        
        self.image = pygame.Surface([width,height])
        self.rect = self.image.get_rect()
        
    #endprocedure

#endclass

#Player class
class Player(pygame.sprite.Sprite):
 
    def __init__(self):
        
        super().__init__()
 
        self.image = pygame.Surface([65, 95])
        self.idleCounter = 0
        self.runCounter = 0
        self.playerStand = [pygame.transform.scale(pygame.image.load('IdlePlayer1.png'), (112, 95)), pygame.transform.scale(pygame.image.load('IdlePlayer2.png'), (112, 95)), pygame.transform.scale(pygame.image.load('IdlePlayer3.png'), (107, 95)), pygame.transform.scale(pygame.image.load('IdlePlayer4.png'), (107, 95)), pygame.transform.scale(pygame.image.load('IdlePlayer5.png'), (110, 95)), pygame.transform.scale(pygame.image.load('IdlePlayer6.png'), (110, 95)), pygame.transform.scale(pygame.image.load('IdlePlayer7.png'), (107, 95)), pygame.transform.scale(pygame.image.load('IdlePlayer8.png'), (107, 95))]
        #self.playerRun = [pygame.transform.scale(pygame.image.load('PlayerRun1.png'), (62, 82)), pygame.transform.scale(pygame.image.load('PlayerRun2.png'), (72, 82)), pygame.transform.scale(pygame.image.load('PlayerRun3.png'), (80, 87)), pygame.transform.scale(pygame.image.load('PlayerRun4.png'), (62, 87)), pygame.transform.scale(pygame.image.load('PlayerRun5.png'), (50, 82)), pygame.transform.scale(pygame.image.load('PlayerRun6.png'), (77, 80)), pygame.transform.scale(pygame.image.load('PlayerRun7.png'), (77, 87)), pygame.transform.scale(pygame.image.load('PlayerRun8.png'), (77, 87))]
        #self.playerJump = [pygame.transform.scale(pygame.image.load('PlayerJump.png'), (60, 92))]
 
        self.rect = self.image.get_rect()

    #endprocedure

    def IdleStance(self, face):

        if face == "L":
            self.image = self.playerStand[self.idleCounter]
        else:
            self.image = pygame.transform.flip(self.playerStand[self.idleCounter],1,0)
        #endif

        if self.idleCounter != 7:

            self.idleCounter += 1

        else:

            self.idleCounter = 0

        #endif

    #endprocedure

    def Run(self, face):

        if face == "L":
            self.image = self.playerRun[self.runCounter]
        else:
            self.image = pygame.transform.flip(self.playerRun[self.runCounter],1,0)
        #endif

        if self.runCounter != 7:

            self.runCounter += 1

        else:

            self.runCounter = 0

        #endif

    #endprocedure

    def Jump(self, face):

        if face == "L":

            self.image = self.playerJump[0]

        else:

            self.image = pygame.transform.flip(self.playerJump[0],1,0)

        #endif

    #endprocedure
 
    def moveHori(self,speed):
        
        self.rect.x += speed

    #endprocedure

#endclass

#Enemy Class
#Bandit
class Bandit(pygame.sprite.Sprite):
 
    def __init__(self):
        
        super().__init__()
 
        self.image = pygame.Surface([65, 90])
        self.idleCounter = 0
        self.runCounter = 0
        self.banditStand = [pygame.transform.scale(pygame.image.load('IdleBandit1.png'), (65, 92)), pygame.transform.scale(pygame.image.load('IdleBandit2.png'), (65, 92)), pygame.transform.scale(pygame.image.load('IdleBandit3.png'), (65, 90)), pygame.transform.scale(pygame.image.load('IdleBandit4.png'), (65, 90))]
        self.banditRun = [pygame.transform.scale(pygame.image.load('BanditRun1.png'), (62, 82)), pygame.transform.scale(pygame.image.load('BanditRun2.png'), (72, 82)), pygame.transform.scale(pygame.image.load('BanditRun3.png'), (80, 87)), pygame.transform.scale(pygame.image.load('BanditRun4.png'), (62, 87)), pygame.transform.scale(pygame.image.load('BanditRun5.png'), (50, 82)), pygame.transform.scale(pygame.image.load('BanditRun6.png'), (77, 80)), pygame.transform.scale(pygame.image.load('BanditRun7.png'), (77, 87)), pygame.transform.scale(pygame.image.load('BanditRun8.png'), (77, 87))]
        self.banditJump = [pygame.transform.scale(pygame.image.load('BanditJump.png'), (60, 92))]
 
        self.rect = self.image.get_rect()

    #endprocedure

    def IdleStance(self, face):

        if face == "L":
            self.image = self.banditStand[self.idleCounter]
        else:
            self.image = pygame.transform.flip(self.banditStand[self.idleCounter],1,0)
        #endif

        if self.idleCounter != 3:

            self.idleCounter += 1

        else:

            self.idleCounter = 0

        #endif

    #endprocedure

    def Run(self, face):

        if face == "L":
            self.image = self.banditRun[self.runCounter]
        else:
            self.image = pygame.transform.flip(self.banditRun[self.runCounter],1,0)
        #endif

        if self.runCounter != 7:

            self.runCounter += 1

        else:

            self.runCounter = 0

        #endif

    #endprocedure

    def Jump(self, face):

        if face == "L":

            self.image = self.banditJump[0]

        else:

            self.image = pygame.transform.flip(self.banditJump[0],1,0)

        #endif

    #endprocedure
 
    def moveHori(self,speed):
        
        self.rect.x += speed

    #endprocedure

#endclass

def createBlock(nodesNum, block_list, all_sprites_list):

    #Nodes
    for i in range(nodesNum):
        
        line = nodes[i-2]
        
        #x position
        if line[1] == "0" and line[2] == "0":
            xpos = int(str(line[3])+str(line[4]))
        elif line[1] == "0" and line[2] != "0":
            xpos = int(str(line[2])+str(line[3])+str(line[4]))
        elif line[4] == str(0) and line[3] == str(0) and line[2] == str(0) and line[1] == str(0) :
            xpos = 0
        else:
            xpos = int(str(line[1])+str(line[2])+str(line[3])+str(line[4]))
        #endif

        #y position
        if line[5] == str(0):
            ypos = int(str(line[6])+str(line[7]))
        else:
            ypos = int(str(line[5])+str(line[6])+str(line[7]))
        #endif

        #width
        if line[8] == str(0):
            width = int(str(line[9])+str(line[10]))
        else:
            width = int(str(line[8])+str(line[9])+str(line[10]))
        #endif

        #height
        if line[11] == str(0):
            height = int(str(line[12])+str(line[13]))
        else:
            height = int(str(line[11])+str(line[12])+str(line[13]))
        #endif
                
        if line[0] == str(1):

            block = Block(DGREEN,width,height)
            block.rect.x = xpos
            block.rect.y = ypos
            block_list.add(block)
            all_sprites_list.add(block)

        #endif
#endprocedure

def loadify(img):
    
    return pygame.image.load(img).convert_alpha()

#endfunction

def backGroundPos(x,y,img):
    
    screen.blit(img, (x,y))

#endfunction

#game
def Game():

    game_over = False
    clock = pygame.time.Clock()

    #Player Attributes
    jumped = False
    doubleJump = False
    vertSpeed = -2.5
    horiSpeed = 0
    changeTime = 0
    centered = False
    blocked = False
    attack = False
    attackStep = 1
    playerHealth = 500
    playerMaxHealth = 500
    playerHealthDisplay = 300
    startAttack = 0
    endAttack = 0
    startAttTimeBet = 0
    endAttTimeBet = 0
    playerGetHit = False
    Freeze = False
    combatPhase = False
    transition = False
    facing = "R"

    #Player Timers
    startAnimation = 0
    endAnimation = 0

    backGroundMove = 0

    player_list = pygame.sprite.Group()

    block_list = pygame.sprite.Group()

    startEnd_list = pygame.sprite.Group()

    all_sprites_list = pygame.sprite.Group()

    enemy_list = pygame.sprite.Group()

    bow_list = pygame.sprite.Group()

    warrior_list = pygame.sprite.Group()

    playerSword_list = pygame.sprite.Group()

    warriorSword_list = pygame.sprite.Group()
    
    ground = Block(GREEN, 3600, 100)
    ground.rect.x = 0
    ground.rect.y = 700
    all_sprites_list.add(ground)

    player = Player()
    player.rect.x = 20
    player.rect.y = 626
    player_list.add(player)
    all_sprites_list.add(player)

    #BackGround1 = pygame.transform.scale(loadify('BackGround1.png'), (1800, 700))

    startArea = Block(GREEN,558, 700)
    startArea.rect.x = 0
    startArea.rect.y = 0
    startEnd_list.add(startArea)

    createBlock(nodesNum, block_list, all_sprites_list)
        
    while not game_over:
        
    # -- User input and controls
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN and Freeze == False:
                #Jump
                if event.key == pygame.K_w:
                    if jumped == False and attack == False:
                        changeTime = 0
                        jumped = True
                        doubleJump = False
                        vertSpeed = 8
                    elif jumped == True and doubleJump == False and attack == False:
                        doubleJump = True
                        changeTime = 0
                        vertSpeed = 6
                    #endif
                #Left
                if event.key == pygame.K_a and attack == False:
                    facing = "L"
                    horiSpeed = -5
                #Right
                if event.key == pygame.K_d and attack == False:
                    facing = "R"
                    horiSpeed = 5
                #Attack
##                if event.key == pygame.K_SPACE and attack == False:
##                    endAttTimeBet = pygame.time.get_ticks()
##                    if endAttTimeBet - startAttTimeBet > 500:
##                        attackStep = 1
##                    #endif
##                    startAttTimeBet = 0
##                    endAttTimeBet = 0
##                    attack = True
##                #endif
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_a and horiSpeed < 0:
                    horiSpeed = 0
                if event.key == pygame.K_d and horiSpeed > 0:
                    horiSpeed = 0
            #endif
        #endfor

        screen.fill(WHITE)

        #Player Control   
        keys = pygame.key.get_pressed()

        #Player Update

        if vertSpeed == 0:
            vertSpeed = -1
        else:
            vertSpeed -= 0.2
        #endif

        #Player Idle Stance Timer
        endAnimation = pygame.time.get_ticks()
        if attack == False and endAnimation - startAnimation >= 200 and horiSpeed == 0 and jumped == False:

            startAnimation = endAnimation
            player.IdleStance(facing)

        elif attack == False and endAnimation - startAnimation >= 110 and horiSpeed != 0 and jumped == False:

            startAnimation = endAnimation
            player.Run(facing)

        elif jumped == True:

            player.Jump(facing)
            
        #endif

        if player.rect.y >= 605 and vertSpeed <= 0:
            player.rect.y = 605
            jumped = False
            vertSpeed = 0
        #endif

        playerStartEnd_list = pygame.sprite.spritecollide(startArea, player_list, False)
        for player in playerStartEnd_list:

            centered = False
            player.moveHori(horiSpeed)
            if backGroundMove <= 600 and horiSpeed == 4:
                backGroundMove += 0.4
            elif backGroundMove >= 0 and horiSpeed == -4:
                backGroundMove -= 0.4
            #endif

        #endfor
        
        if centered == True:

            player.rect.x = 567.5
            
            for block in block_list:

                block.rect.x -= horiSpeed
                startArea.rect.x -= horiSpeed
                if backGroundMove <= 600 and horiSpeed == 4:
                    backGroundMove += 0.4
                elif backGroundMove >= 0 and horiSpeed == -4:
                    backGroundMove -= 0.4
                #endif

                playerBlock_list = pygame.sprite.spritecollide(block, player_list, False)
                #Make player stand on platform
                for player in playerBlock_list:

                    for block in block_list:
                        
                        block.rect.x += horiSpeed
                        startArea.rect.x += horiSpeed
                        if horiSpeed == 4:
                            backGroundMove -= 0.4
                        elif horiSpeed == -4:
                            backGroundMove += 0.4
                        #endif

                    #endfor

                #endfor

            #endfor

        #endif

        if transition == False:
            centered = True
        #endif

        if player.rect.x <= 0:

            player.rect.x = 0

        #endif

        player.rect.y -= vertSpeed
        
        playerBlock_list = pygame.sprite.spritecollide(player, block_list, False)
        #Make player stand on platform
        for block in playerBlock_list:

            if vertSpeed <= 0:

                player.rect.bottom = block.rect.top
                jumped = False

            elif vertSpeed >= 0:

                player.rect.top = block.rect.bottom

            #endif

            vertSpeed = 0
                
        #endfor

        #backGroundPos(0 - backGroundMove, 0, BackGround1)

        all_sprites_list.draw(screen)
            
        # -- flip display to reveal new position of objects
        pygame.display.flip()

        # - The clock ticks over
        clock.tick(100)

    #endwhile

#endprocedure

# -- Initialise PyGame
pygame.init()

# -- Blank Screen
size = (1200,800)
screen = pygame.display.set_mode(size)

# -- Title of new window/screen
pygame.display.set_caption("2D RPG Game")
    
### -- Game Loop

Game()

pygame.quit()
