import pygame
from random import randint
# -- Global Constants

f = open("Blocks.txt","r+")
nodes = f.readlines()
nodesNum = len(nodes)
f.close()

#Images

playerStanding = [pygame.transform.scale(pygame.image.load('NotMovingPlayerLeft.png'), (83, 112)), pygame.transform.scale(pygame.image.load('NotMovingPlayerRight.png'), (83, 112))]
playerSlashing = [pygame.transform.scale(pygame.image.load('SlashPlayerLeft.png'), (83, 112)), pygame.transform.scale(pygame.image.load('SlashPlayerRight.png'), (83, 112))]
slashSword1 = [pygame.transform.scale(pygame.image.load('SlashSword1Left.png'), (64, 20)), pygame.transform.scale(pygame.image.load('SlashSword1Right.png'), (64, 20))]
warriorStanding = [pygame.transform.scale(pygame.image.load('NotMovingEnemy1Left.png'), (83, 112)), pygame.transform.scale(pygame.image.load('NotMovingEnemy1Right.png'), (83, 112))]
warriorSlashing = [pygame.transform.scale(pygame.image.load('SlashEnemy1Left.png'), (83, 112)), pygame.transform.scale(pygame.image.load('SlashEnemy1Right.png'), (83, 112))]
wSlashSword = [pygame.transform.scale(pygame.image.load('EnemySword1Left.png'), (83, 76)), pygame.transform.scale(pygame.image.load('EnemySword1Right.png'), (83, 76))]
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
 
        self.image = pygame.Surface([83, 112])
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
 
        self.image = pygame.Surface([64, 20])
        self.image = pygame.transform.scale(pygame.image.load('SlashSword1Left.png'), (64, 20))
 
        self.rect = self.image.get_rect()

    #endprocedure

    def slash(self,face):

        if face == "L":

            self.image = slashSword1[0]

        else:

            self.image = slashSword1[1]

        #endif

    #endfunction

#endclass

#Enemy Class
class Warrior(pygame.sprite.Sprite):

    def __init__(self, colour):
        
        super().__init__()
 
        self.image = pygame.Surface([83, 112])
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

#game
def game():

    game_over = False
    clock = pygame.time.Clock()

    startJump = 0
    endJump = 0

    #Player Attributes
    jumped = False
    doubleJump = False
    vertSpeed = 2.5
    horiSpeed = 0
    changeTime = 0
    centered = False
    blocked = False
    attack = False
    attackStep = 1

    #Player Attack More Attributes
    startAttack = 0
    endAttack = 0
    startAttTimeBet = 0
    endAttTimeBet = 0

    facing = "L"

    backGroundMove = 0

    player_list = pygame.sprite.Group()

    block_list = pygame.sprite.Group()

    startEnd_list = pygame.sprite.Group()

    all_sprites_list = pygame.sprite.Group()

    enemy_list = pygame.sprite.Group()

    bow_list = pygame.sprite.Group()

    warrior_list = pygame.sprite.Group()

    playerSword_list = pygame.sprite.Group()
    
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

    enemy = Warrior(DBLUE)
    enemy.rect.y = 620
    enemy.rect.x = 2000
    all_sprites_list.add(enemy)
    enemy_list.add(enemy)
    warrior_list.add(enemy)
##
##    enemy = BowMaster(PINK)
##    enemy.rect.y = 620
##    enemy.rect.x = 1000
##    all_sprites_list.add(enemy)
##    enemy_list.add(enemy)
##    bow_list.add(enemy)

    startArea = Block(GREEN,570, 700)
    startArea.rect.x = 0
    startArea.rect.y = 0
    startEnd_list.add(startArea)

    createBlock(nodesNum, block_list, all_sprites_list)

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
            elif event.type == pygame.KEYDOWN:
                #Jump
                if event.key == pygame.K_w:
                    if jumped == False:
                        changeTime = 0
                        jumped = True
                        doubleJump = False
                        vertSpeed = -5
                    elif jumped == True and doubleJump == False:
                        doubleJump = True
                        changeTime = 0
                        vertSpeed = -5
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
            vertSpeed = 1
        else:
            vertSpeed += 0.1
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

            endAttack = pygame.time.get_ticks()

            if endAttack - startAttack >= 300:
                print("Slash")
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

            endAttack = pygame.time.get_ticks()

            if endAttack - startAttack >= 300:
                print("Slash!")
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

            endAttack = pygame.time.get_ticks()

            if endAttack - startAttack >= 300:
                print("Slash!!")
                player.anime(facing,0)
                playerSword.rect.x = -1000
                playerSword.rect.y = -1000
                startAttack = 0
                endAttack = 0
                attackStep = 1
                attack = False
            #endif

        #endif

        if player.rect.y >= 588 and vertSpeed >= 0:
            player.rect.y = 588
            jumped = False
            vertSpeed = 0
        #endif

        for enemy in enemy_list:

            enemy.move(player.rect.x)

        #endfor

        playerStartEnd_list = pygame.sprite.spritecollide(startArea, player_list, False)
        for player in playerStartEnd_list:

            centered = False
            player.rect.x += horiSpeed
            if backGroundMove <= 600 and horiSpeed == 4:
                backGroundMove += 0.2
            elif backGroundMove >= 0 and horiSpeed == -4:
                backGroundMove -= 0.2
            #endif

        #endfor
        
        if centered == True:

            player.rect.x = 558.5
            
            for block in block_list:

                block.rect.x -= horiSpeed
                startArea.rect.x -= horiSpeed
                if backGroundMove <= 600 and horiSpeed == 4:
                    backGroundMove += 0.2
                elif backGroundMove >= 0 and horiSpeed == -4:
                    backGroundMove -= 0.2
                #endif
                
                for enemy in enemy_list:

                    enemy.rect.x -= horiSpeed

                #endfor

                playerBlock_list = pygame.sprite.spritecollide(block, player_list, False)
                #Make player stand on platform
                for player in playerBlock_list:

                    for block in block_list:
                        
                        block.rect.x += horiSpeed
                        startArea.rect.x += horiSpeed
                        if horiSpeed == 4:
                            backGroundMove -= 0.2
                        elif horiSpeed == -4:
                            backGroundMove += 0.2
                        #endif

                    #endfor

                #endfor

            #endfor

        #endif

        centered = True

        if player.rect.x <= 0:

            player.rect.x = 0

        #endif

        player.rect.y += vertSpeed
        
        playerBlock_list = pygame.sprite.spritecollide(player, block_list, False)
        #Make player stand on platform
        for block in playerBlock_list:

            if vertSpeed >= 0:

                player.rect.bottom = block.rect.top
                jumped = False

            elif vertSpeed <= 0:

                player.rect.top = block.rect.bottom

            #endif

            vertSpeed = 0
                
        #endfor

        backGroundPos(0 - backGroundMove, 0, BackGround1)

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

game()

pygame.quit()
