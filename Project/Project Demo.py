import pygame
from random import randint
# -- Global Constants

f = open("Blocks.txt","r+")
nodes = f.readlines()
nodesNum = len(nodes)
f.close()

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
 
        self.image = pygame.Surface([45, 80])
        self.image.fill(NICE)
 
        self.rect = self.image.get_rect()

    #endprocedure
 
    def update(self,move):
        
        if move == 1:

            self.rect.x -= 3

        elif move == 2:

            self.rect.x += 3

        #endif

    #endprocedure

#endclass

#Enemy Class
class Enemy(pygame.sprite.Sprite):

    def __init__(self, colour):
        
        super().__init__()
 
        self.image = pygame.Surface([45, 80])
        self.image.fill(colour)
 
        self.rect = self.image.get_rect()

    #endprocedure

    def move(self,xpos):

        if self.rect.x < xpos:

            self.rect.x += 3

        elif self.rect.x > xpos:

            self.rect.x -= 3

        #endif

    #endprocedure

#endclass

class BowMaster(Enemy):

    def __init__(self, colour):

        super().__init__(colour)

        self.speed = 0
        
        #finish

    #endprocedure

#endclass

class Warrior(Enemy)

    def __init__(self, colour):

        super().__init__(colour)

        self.speed = 4

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

    player_list = pygame.sprite.Group()

    block_list = pygame.sprite.Group()

    startEnd_list = pygame.sprite.Group()

    all_sprites_list = pygame.sprite.Group()

    enemy_list = pygame.sprite.Group()

    bow_list = pygame.sprite.Group()

    warrior_list = pygame.sprite.Group()

    #Player
    ground = Block(GREEN, 3600, 100)
    ground.rect.x = 0
    ground.rect.y = 700
    all_sprites_list.add(ground)

    player = Player()
    player.rect.x = 20
    player.rect.y = 620
    player_list.add(player)
    all_sprites_list.add(player)

    enemy = Warrior(DBLUE)
    enemy.rect.y = 620
    enemy.rect.x = 2000
    all_sprites_list.add(enemy)
    enemy_list.add(enemy)
    warrior_list.add(enemy)

    enemy = bowMaster(PINK)
    enemy.rect.y = 620
    enemy.rect.x = 1000
    all_sprites_list.add(enemy)
    enemy_list.add(enemy)
    bow_list.add(enemy)

    startArea = Block(GREEN,570, 700)
    startArea.rect.x = 0
    startArea.rect.y = 0
    startEnd_list.add(startArea)

    createBlock(nodesNum, block_list, all_sprites_list)
        
    while not game_over:
        
    # -- User input and controls
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
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
                if event.key == pygame.K_a:
                    horiSpeed = -4
                if event.key == pygame.K_d:
                    horiSpeed = 4
                #endif
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_a and horiSpeed < 0:
                    horiSpeed = 0
                if event.key == pygame.K_d and horiSpeed > 0:
                    horiSpeed = 0
            #endif
        #endfor

        screen.fill(BLACK)

        #Player Control   
        keys = pygame.key.get_pressed()

        #Player Update

        if vertSpeed == 0:
            vertSpeed = 1
        else:
            vertSpeed += 0.1
        #endif

        if player.rect.y >= 620 and vertSpeed >= 0:
            player.rect.y = 620
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

        #endfor

        
        
        if centered == True:
            
            for block in block_list:

                block.rect.x -= horiSpeed
                startArea.rect.x -= horiSpeed
                
                for enemy in enemy_list:

                    enemy.rect.x -= horiSpeed

                #endfor

                playerBlock_list = pygame.sprite.spritecollide(block, player_list, False)
                #Make player stand on platform
                for player in playerBlock_list:

                    for block in block_list:
                        
                        block.rect.x += horiSpeed
                        startArea.rect.x += horiSpeed

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
