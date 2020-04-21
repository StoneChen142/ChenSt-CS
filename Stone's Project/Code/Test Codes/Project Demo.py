import pygame
from random import randint
# -- Global Constants

f = open("Blocks.txt","r+")
nodes = f.readlines()
nodesNum = len(nodes)
f.close()

#Images

playerStanding = [pygame.transform.scale(pygame.image.load('NotMovingPlayerLeft.png'), (46, 64)), pygame.transform.scale(pygame.image.load('NotMovingPlayerRight.png'), (46, 64))]
playerSlashing = [pygame.transform.scale(pygame.image.load('SlashPlayerLeft.png'), (46, 64)), pygame.transform.scale(pygame.image.load('SlashPlayerRight.png'), (46, 64))]
slashSword1 = [pygame.transform.scale(pygame.image.load('SlashSword1Left.png'), (40, 12)), pygame.transform.scale(pygame.image.load('SlashSword1Right.png'), (40, 12))]
warriorStanding = [pygame.transform.scale(pygame.image.load('NotMovingEnemy1Left.png'), (46, 64)), pygame.transform.scale(pygame.image.load('NotMovingEnemy1Right.png'), (46, 64))]
warriorSlashing = [pygame.transform.scale(pygame.image.load('SlashEnemy1Left.png'), (46, 64)), pygame.transform.scale(pygame.image.load('SlashEnemy1Right.png'), (46, 64))]
wSlashSword = [pygame.transform.scale(pygame.image.load('WarriorSword1Left.png'), (40, 12)), pygame.transform.scale(pygame.image.load('WarriorSword1Right.png'), (40, 12))]
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
 
        self.image = pygame.Surface([46, 64])
        self.image = playerStanding[0]
 
        self.rect = self.image.get_rect()

    #endprocedure

    def anime(self,face,state):

        if state == 0:
            
            if face == "L":

                self.image = playerStanding[0]

            else:

                self.image = playerStanding[1]

            #endif

        elif state == 1:
            
            if face == "L":

                self.image = playerSlashing[0]

            else:

                self.image = playerSlashing[1]

            #endif

        #endif

    #endprocedure
 
    def update(self,move):
        
        if move == 1:

            self.rect.x -= 3

        elif move == 2:

            self.rect.x += 3

        #endif

    #endprocedure

#endclass

class Sword(pygame.sprite.Sprite):

    def __init__(self):
        
        super().__init__()
 
        self.image = pygame.Surface([40, 12])
        self.image = pygame.transform.scale(pygame.image.load('SlashSword1Left.png'), (40, 12))
 
        self.rect = self.image.get_rect()

    #endprocedure

    def slash(self,face):

        if face == "L":

            self.image = slashSword1[0]

        else:

            self.image = slashSword1[1]

        #endif

    #endfunction

    def enemySlash(self,face):

        if face == "L":

            self.image = wSlashSword[0]

        else:

            self.image = wSlashSword[1]

        #endif

    #endfunction

#endclass

#Enemy Class
class Warrior(pygame.sprite.Sprite):

    def __init__(self):
        
        super().__init__()
 
        self.image = pygame.Surface([46, 64])
        self.image = warriorStanding[0]
 
        self.rect = self.image.get_rect()

    #endprocedure

    def anime(self,face,state):

        if state == 0:
            
            if face == "L":

                self.image = warriorStanding[0]

            else:

                self.image = warriorStanding[1]

            #endif

        elif state == 1:
            
            if face == "L":

                self.image = warriorSlashing[0]

            else:

                self.image = warriorSlashing[1]

            #endif

        #endif

    #endprocedure
 
    def update(self,move):
        
        if move == 1:

            self.rect.x -= 3

        elif move == 2:

            self.rect.x += 3

        #endif

    #endprocedure

#endclass

class BowMaster(pygame.sprite.Sprite):

    def __init__(self, colour):

        super().__init__(colour)

        self.speed = 0
        
        #finish

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

def Lose():
    clock = pygame.time.Clock()
    keepG = False
    while keepG == False:
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                pygame.quit()
            #endif
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pos>(525,385) and pos<(675,465):
                    keepG = True
                    Game()
                #endif
            #endif
        #endfor
        
        screen.fill (BLACK)

        

        #Button Code
        pygame.draw.rect(screen,YELLOW, (525, 385, 150, 80))
        buttonText("Retry", BLACK, 550, 400, 100,  50, size="small")

        pygame.display.flip()

        clock.tick(60)
    #endwhile

#endfunction

#game
def Game():

    game_over = False
    clock = pygame.time.Clock()

    startJump = 0
    endJump = 0

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

    Freeze = False
    combatPhase = False

    #Player Attack More Attributes
    startAttack = 0
    endAttack = 0
    startAttTimeBet = 0
    endAttTimeBet = 0
    playerGetHit = False

    transition = False

    facing = "R"

    #Warrior Attributes
    warriorStartAttack = 0
    warriorEndAttack = 0
    warriorAttack = False
    warriorHealth = 1000
    warriorMaxHealth = 1000
    warriorGetHit = False
    warriorHori = 0
    enemyFace = "L"

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
    player.rect.y = 588
    player_list.add(player)
    all_sprites_list.add(player)

    BackGround1 = pygame.transform.scale(loadify('BackGround1.png'), (1800, 700))

##    enemy = BowMaster(PINK)
##    enemy.rect.y = 620
##    enemy.rect.x = 1000
##    all_sprites_list.add(enemy)
##    enemy_list.add(enemy)
##    bow_list.add(enemy)

    startArea = Block(GREEN,558, 700)
    startArea.rect.x = 0
    startArea.rect.y = 0
    startEnd_list.add(startArea)

    AreaOne = Block(GREEN, 1200, 700)
    AreaOne.rect.x = 1800
    AreaOne.rect.y = 0
    startEnd_list.add(AreaOne)

    createBlock(nodesNum, block_list, all_sprites_list)

    warriorSword = Sword()
    warriorSword.rect.x = -1000
    warriorSword.rect.y = -1500
    all_sprites_list.add(warriorSword)
    warriorSword_list.add(warriorSword)

    playerSword = Sword()
    playerSword.rect.x = -1000
    playerSword.rect.y = -1000
    all_sprites_list.add(playerSword)
    playerSword_list.add(playerSword)
        
    while not game_over:
        
    # -- User input and controls
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN and Freeze == False:
                #Jump
                if event.key == pygame.K_w:
                    if jumped == False:
                        changeTime = 0
                        jumped = True
                        doubleJump = False
                        vertSpeed = 5
                    elif jumped == True and doubleJump == False:
                        doubleJump = True
                        changeTime = 0
                        vertSpeed = 4
                    #endif
                #Left
                if event.key == pygame.K_a:
                    facing = "L"
                    horiSpeed = -4
                #Right
                if event.key == pygame.K_d:
                    facing = "R"
                    horiSpeed = 4
                #Attack
                if event.key == pygame.K_SPACE and attack == False:
                    endAttTimeBet = pygame.time.get_ticks()
                    if endAttTimeBet - startAttTimeBet > 500:
                        attackStep = 1
                    #endif
                    startAttTimeBet = 0
                    endAttTimeBet = 0
                    attack = True
                #endif
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

        if attack == False:

            player.anime(facing,0)

        #endif

        #Player Attacks
        if attack == True and attackStep == 1:

            if startAttack == 0:
                startAttack = pygame.time.get_ticks()
            #endif
            player.anime(facing,1)
            if facing == "L":
                playerSword.slash(facing)
                playerSword.rect.x = player.rect.x - 45
                playerSword.rect.y = player.rect.y + 51
                
            else:
                playerSword.slash(facing)
                playerSword.rect.x = player.rect.x + 68
                playerSword.rect.y = player.rect.y + 51
            #endif
            warriorHit_list = pygame.sprite.spritecollide(playerSword, warrior_list, False)
            if warriorGetHit == False:
                for warrior in warriorHit_list:
                    if facing == "L":
                        warrior.rect.x -= 30
                    else:
                        warrior.rect.x += 30
                    #endif
                    warriorHealth -= 20
                    if warriorHealth < 0:
                        warriorHealth = 0
                    #endif
                    warriorGetHit = True
                    print("Got hit")
                #endfor
            #endif

            endAttack = pygame.time.get_ticks()

            if endAttack - startAttack >= 300:
                warriorGetHit = False
                #print("Slash")
                player.anime(facing,0)
                playerSword.rect.x = -1000
                playerSword.rect.y = -1000
                startAttack = 0
                endAttack = 0
                attackStep = 2
                attack = False
                startAttTimeBet = pygame.time.get_ticks()
            #endif

        elif attack == True and attackStep == 2:

            if startAttack == 0:
                startAttack = pygame.time.get_ticks()
            #endif
            player.anime(facing,1)
            if facing == "L":
                playerSword.slash(facing)
                playerSword.rect.x = player.rect.x - 45
                playerSword.rect.y = player.rect.y + 51
            else:
                playerSword.slash(facing)
                playerSword.rect.x = player.rect.x + 68
                playerSword.rect.y = player.rect.y + 51
            #endif
            warriorHit_list = pygame.sprite.spritecollide(playerSword, warrior_list, False)
            if warriorGetHit == False:
                for warrior in warriorHit_list:
                    if facing == "L":
                        warrior.rect.x -= 30
                    else:
                        warrior.rect.x += 30
                    #endif
                    warriorHealth -= 30
                    if warriorHealth < 0:
                        warriorHealth = 0
                    #endif
                    warriorGetHit = True
                #endfor
            #endif

            endAttack = pygame.time.get_ticks()

            if endAttack - startAttack >= 300:
                warriorGetHit = False
                #print("Slash!")
                player.anime(facing,0)
                playerSword.rect.x = -1000
                playerSword.rect.y = -1000
                startAttack = 0
                endAttack = 0
                attackStep = 3
                attack = False
                startAttTimeBet = pygame.time.get_ticks()
            #endif

        elif attack == True and attackStep == 3:

            if startAttack == 0:
                startAttack = pygame.time.get_ticks()
            #endif
            player.anime(facing,1)
            if facing == "L":
                playerSword.slash(facing)
                playerSword.rect.x = player.rect.x - 45
                playerSword.rect.y = player.rect.y + 51
            else:
                playerSword.slash(facing)
                playerSword.rect.x = player.rect.x + 68
                playerSword.rect.y = player.rect.y + 51
            #endif
            warriorHit_list = pygame.sprite.spritecollide(playerSword, warrior_list, False)
            if warriorGetHit == False:
                for warrior in warriorHit_list:
                    if facing == "L":
                        warrior.rect.x -= 30
                    else:
                        warrior.rect.x += 30
                    #endif
                    warriorHealth -= 40
                    if warriorHealth < 0:
                        warriorHealth = 0
                    #endif
                    warriorGetHit = True
                #endfor
            #endif

            endAttack = pygame.time.get_ticks()

            if endAttack - startAttack >= 300:
                warriorGetHit = False
                #print("Slash!!")
                player.anime(facing,0)
                playerSword.rect.x = -1000
                playerSword.rect.y = -1000
                startAttack = 0
                endAttack = 0
                attackStep = 1
                attack = False
            #endif

        #endif

        if player.rect.y >= 588 and vertSpeed <= 0:
            player.rect.y = 588
            jumped = False
            vertSpeed = 0
        #endif

        playerStartEnd_list = pygame.sprite.spritecollide(startArea, player_list, False)
        for player in playerStartEnd_list:

            centered = False
            player.rect.x += horiSpeed
            if backGroundMove <= 600 and horiSpeed == 4:
                backGroundMove += 0.4
            elif backGroundMove >= 0 and horiSpeed == -4:
                backGroundMove -= 0.4
            #endif

        #endfor

        playerAreaOne_list = pygame.sprite.spritecollide(AreaOne, player_list, False)
        for player in playerAreaOne_list:

            if transition == False:
                centered = False
                transition = True
                Freeze = True
                phase = 2
            elif transition == True and phase == 2:
                centered = False
                player.rect.x -= 4
                backGroundMove += 0.4
                AreaOne.rect.x -= 4
                if player.rect.x <= 20:
                    player.rect.x = 20
                    phase = 3
                #endif
            elif phase == 3:        
                enemyWarrior = Warrior()
                enemyWarrior.rect.x = 1093
                enemyWarrior.rect.y = -300
                all_sprites_list.add(enemyWarrior)
                warrior_list.add(enemyWarrior)
                all_sprites_list.remove(player)
                all_sprites_list.add(player)
                all_sprites_list.remove(playerSword)
                all_sprites_list.add(playerSword)
                phase = 4
            elif phase == 4:
                if enemyWarrior.rect.y >= 588:
                    enemyWarrior.rect.y = 588
                    phase = 5
                elif enemyWarrior.rect.y < 300:
                    enemyWarrior.rect.y += 20
                elif enemyWarrior.rect.y >= 300:
                    enemyWarrior.rect.y += 25
                #endif

            #BattlePhaseOne----------------------------------------------------------------Battle One       
            elif transition == True and phase == 5:
                AreaOne.rect.x = 0
                centered = False
                Freeze = False
                combatPhase = True
                player.rect.x += horiSpeed
                if player.rect.x <= 0:
                    player.rect.x = 0
                elif player.rect.x >= 1113:
                    player.rect.x = 1113
                enemyWarrior.rect.x += warriorHori
                if enemyWarrior.rect.x >= 1113:
                    enemyWarrior.rect.x = 1113
                elif enemyWarrior.rect.x <= 0:
                    enemyWarrior.rect.x = 0
                #endif
                    
                #EnemyMove
                if warriorAttack == False:
                    if enemyWarrior.rect.x < player.rect.x:
                        warriorHori = 2
                        enemyFace = "R"
                    else:
                        warriorHori = -2
                        enemyFace = "L"
                    #endif
                    enemyWarrior.anime(enemyFace,0)
                #endif
                        
                #Enemy Attack Player
                if enemyWarrior.rect.x - player.rect.x <= 123 and enemyWarrior.rect.x - player.rect.x >= 83 and enemyFace == "L" and warriorAttack == False:
                    warriorAttack = True
                    warriorHori = 0
                    enemyWarrior.anime(enemyFace,1)
                    warriorStartAttack = pygame.time.get_ticks()
                elif player.rect.x - enemyWarrior.rect.x <= 123 and player.rect.x - enemyWarrior.rect.x >= 83 and enemyFace == "R" and warriorAttack == False:
                    warriorAttack = True
                    warriorHori = 0
                    enemyWarrior.anime(enemyFace,1)
                    warriorStartAttack = pygame.time.get_ticks()
                #endif

                if warriorHealth <= 0:

                    phase = 6

                #endif

                #Enemy Attacked
                if warriorAttack == True:
                    warriorEndAttack = pygame.time.get_ticks()
                    if warriorEndAttack - warriorStartAttack >= 300:
                        warriorAttack = False
                        warriorSword.rect.y = -1040
                        playerGetHit = False
                    else:
                        if enemyFace == "L":
                            warriorSword.enemySlash(enemyFace)
                            warriorSword.rect.x = enemyWarrior.rect.x - 45
                            warriorSword.rect.y = enemyWarrior.rect.y + 51
                        else:
                            warriorSword.enemySlash(enemyFace)
                            warriorSword.rect.x = enemyWarrior.rect.x + 68
                            warriorSword.rect.y = enemyWarrior.rect.y + 51
                        #endif

                        warriorHitPlayer_list = pygame.sprite.spritecollide(warriorSword, player_list, False)
                        if playerGetHit == False:
                            for player in warriorHitPlayer_list:
                                if facing == "L":
                                    player.rect.x -= 30
                                else:
                                    player.rect.x += 30
                                #endif
                                playerHealth -= 40
                                if playerHealth < 0:
                                    playerHealth = 0
                                    combatPhase= False
                                    Lose()
                                #endif
                                playerGetHit = True
                            #endfor
                        #endif
                    #endif

            elif phase == 6:

                Freeze = True
                if player.rect.x > 559:
                    player.rect.x -= 4
                    backGroundMove += 0.4
                    if player.rect.x <= 559:
                        player.rect.x = 559
                        phase = 7
                    #endif
                else:
                    player.rect.x += 4
                    backGroundMove -= 0.4
                    if player.rect.x >= 559:
                        player.rect.x = 559
                        phase = 7
                    #endif
                #endif
                all_sprites_list.remove(enemyWarrior)

            elif phase == 7:

                centered = True
                Freeze = False
                combatPhase = False
                
            #endif

        #endfor
        
        if centered == True:

            player.rect.x = 559
            
            for block in block_list:

                block.rect.x -= horiSpeed
                startArea.rect.x -= horiSpeed
                AreaOne.rect.x -= horiSpeed
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

        backGroundPos(0 - backGroundMove, 0, BackGround1)

        all_sprites_list.draw(screen)

        if combatPhase == True:
            pygame.draw.rect(screen, RED, (60, 720, (playerHealth/playerMaxHealth)*300, 30))
            pygame.draw.rect(screen, RED, (840, 720, (warriorHealth/warriorMaxHealth)*300, 30))
        #endif
            
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

##            else: #If player placed in the center, the blocks move instead of the player
##
##                self.rect.x = 717.5
##
##                if level == 4:
##
##                    for area in startEnd_list:
##
##                        area.rect.x -= self.horiSpeed
##
##                    #endfor
##
##                    for warlock in warlock_list:
##
##                        warlock.rect.x -= self.horiSpeed
##
##                    #endfor
##                    
##                    for block in block1_list:
##
##                        block.rect.x -= self.horiSpeed
##                        
##                        for back in background_list:
##
##                            if self.horiSpeed != 0:
##
##                                if self.horiSpeed < 0:
##                                    move = 5
##                                else:
##                                    move = -5
##                                #endif
##
##                                back.BackUpdate(move)
##
##                            #endif
##
##                        #endfor
##                        
##                        playerBlock_list = pygame.sprite.spritecollide(block, player_list, False)
##                        for player in playerBlock_list:
##
##                            for block in block1_list:
##                                
##                                block.rect.x += self.horiSpeed
##                                for back in background_list:
##
##                                    if self.horiSpeed != 0:
##                                        
##                                        if self.horiSpeed < 0:
##                                            move = -5
##                                        else:
##                                            move = 5
##                                        #endif
##
##                                    #endif
##
##                                    back.BackUpdate(move)
##
##                                #endfor
##
##                                for area in startEnd_list:
##
##                                    area.rect.x += self.horiSpeed
##
##                                #endfor
##
##                                for warlock in warlock_list:
##
##                                    warlock.rect.x += self.horiSpeed
##
##                                #endfor
##
##                            #endfor
##
##                        #endfor
##
##                    #endfor
##
##                #endif
##
##            #endif
