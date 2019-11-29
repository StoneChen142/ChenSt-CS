import pygame
import random
# -- Global Constants

f = open("mazeSheet.txt","r+")
lines = f.readlines()
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

#Player Attributes

left = False
right = False
up = False
down = False
pmoveCount = 0
nextMove = [0]

#Animations

moveDown = [pygame.transform.scale(pygame.image.load('PacManRight1.png'), (36, 36)), pygame.transform.scale(pygame.image.load('PacManRight2.png'), (36, 36)),pygame.transform.scale(pygame.image.load('PacManFull.png'), (36, 36)),pygame.transform.scale(pygame.image.load('PacManRight2.png'), (36, 36))]
moveUp = [pygame.transform.scale(pygame.image.load('PacManLeft1.png'), (36, 36)), pygame.transform.scale(pygame.image.load('PacManLeft2.png'), (36, 36)),pygame.transform.scale(pygame.image.load('PacManFull.png'), (36, 36)),pygame.transform.scale(pygame.image.load('PacManLeft2.png'), (36, 36))]
moveRight = [pygame.transform.scale(pygame.image.load('PacManDown1.png'), (36, 36)), pygame.transform.scale(pygame.image.load('PacManDown2.png'), (36, 36)),pygame.transform.scale(pygame.image.load('PacManFull.png'), (36, 36)),pygame.transform.scale(pygame.image.load('PacManDown2.png'), (36, 36))]
moveLeft = [pygame.transform.scale(pygame.image.load('PacManUp1.png'), (36, 36)), pygame.transform.scale(pygame.image.load('PacManUp2.png'), (36, 36)),pygame.transform.scale(pygame.image.load('PacManFull.png'), (36, 36)),pygame.transform.scale(pygame.image.load('PacManUp2.png'), (36, 36))]

notMoving = pygame.transform.scale(pygame.image.load('PacManFull.png'), (36, 36))

# -- Classes

#Player class
class Player(pygame.sprite.Sprite):
 
    def __init__(self):
        super().__init__()
 
        self.image = pygame.Surface([36, 36])
        self.image = pygame.transform.scale(pygame.image.load('PacManFull.png'), (36, 36))
        self.rect = self.image.get_rect()
        self.num = 0
        
    #endfunction
 
    def update(self,n):
        global PlayerMoving
        global left
        global right
        global up
        global down

        if n == 1:
            if self.rect.x > 0:
                self.rect.x -= 3
                PlayerMoving = True
            else:
                self.image = notMoving
                PlayerMoving = False
                self.num = 0
                up = False
        elif n == 2:
            if self.rect.x < 504:
                self.rect.x += 3
                PlayerMoving = True
            else:
                self.image = notMoving
                PlayerMoving = False
                self.num = 0
                down = False
        elif n == 3:
            if self.rect.y > 0:
                self.rect.y -= 3
                PlayerMoving = True
            else:
                self.image = notMoving
                PlayerMoving = False
                self.num = 0
                left = False
        elif n == 4:
            if self.rect.y < 504:
                self.rect.y += 3
                PlayerMoving = True
            else:
                self.image = notMoving
                PlayerMoving = False
                self.num = 0
                right = False
        #endif

    #endprocedure

    def animation(self,num):
        global left
        global right
        global up
        global down

        if num == 0:
            
            self.image = notMoving
        
        elif num == 1:
            if self.num == 0:
                self.image = moveUp[self.num]
                self.num += 1
            elif self.num == 1:
                self.image = moveUp[self.num]
                self.num += 1
            elif self.num == 2:
                self.image = moveUp[self.num]
                self.num += 1
            elif self.num == 3:
                self.image = moveUp[self.num]
                self.num = 0
            #endif
        elif num == 2:
            if self.num == 0:
                self.image = moveDown[self.num]
                self.num += 1
            elif self.num == 1:
                self.image = moveDown[self.num]
                self.num += 1
            elif self.num == 2:
                self.image = moveDown[self.num]
                self.num += 1
            elif self.num == 3:
                self.image = moveDown[self.num]
                self.num = 0
            #endif
        elif num == 3:
            if self.num == 0:
                self.image = moveLeft[self.num]
                self.num += 1
            elif self.num == 1:
                self.image = moveLeft[self.num]
                self.num += 1
            elif self.num == 2:
                self.image = moveLeft[self.num]
                self.num += 1
            elif self.num == 3:
                self.image = moveLeft[self.num]
                self.num = 0
            #endif
        elif num == 4:
            if self.num == 0:
                self.image = moveRight[self.num]
                self.num += 1
            elif self.num == 1:
                self.image = moveRight[self.num]
                self.num += 1
            elif self.num == 2:
                self.image = moveRight[self.num]
                self.num += 1
            elif self.num == 3:
                self.image = moveRight[self.num]
                self.num = 0
            #endif
        #endif
               
    #endprocedure   
                
#EndClass

class Block(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        self.image = pygame.Surface([36,36])
        self.image = pygame.image.load("Brick.png").convert()
        self.image = pygame.transform.scale(self.image, (36, 36))
        self.rect = self.image.get_rect()
        
    #endprocedure

#endclass

class Node(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        self.image = pygame.Surface([36,36])
        self.rect = self.image.get_rect()
        
    #endprocedure

#endclass

def createMaze(node_list, block_list, all_sprites_list, lines):
    for j in range(15):
        line = lines[j]
        print(line)
        for i in range(15):
            if str(line[i]) == "b":
                block = Block()

                block.rect.x = 36*i
                block.rect.y = 36*j

                block_list.add(block)
                all_sprites_list.add(block)
            elif str(line[i]) == "n":
                node = Node()

                node.rect.x = 36*i
                node.rect.y = 36*j

                node_list.add(node)
            #endfor

        #endwhile
    #endfor
#endprocedure
    

# -- Initialise PyGame
pygame.init()

# -- Manages how fast screen refreshes

clock = pygame.time.Clock()

# -- Blank Screen
size = (540,540)
screen = pygame.display.set_mode(size)

# -- Title of new window/screen
pygame.display.set_caption("Pac Man")

clock =pygame.time.Clock()

game_over = False

#Variables

oldtime = 0

all_sprites_list = pygame.sprite.Group()

block_list = pygame.sprite.Group()

node_list = pygame.sprite.Group()

player_list = pygame.sprite.Group()

player = Player()
player.rect.x = 36
player.rect.y = 0
all_sprites_list.add(player)
player_list.add(player)

PlayerMove = 0
PlayerMoving = False

createMaze(node_list, block_list, all_sprites_list, lines)
    
while game_over == False:
# -- User input and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                nextMove.pop(0)
                nextMove.append(1)
                left = True
            elif event.key == pygame.K_d:
                nextMove.pop(0)
                nextMove.append(2)
                right = True
            elif event.key == pygame.K_w:
                nextMove.pop(0)
                nextMove.append(3)
                up = True
            elif event.key == pygame.K_s:
                nextMove.pop(0)
                nextMove.append(4)
                down = True
                #endif
            #endif
        #End If
    #Next event

    screen.fill(BLACK)

    player.update(PlayerMove)

    #Update PacMan
    newtime = pygame.time.get_ticks()

    if newtime - oldtime > 100 and PlayerMoving == True: 

        player.animation(PlayerMove)
        oldtime=newtime
            
    #endif

    #Colliding with box
    for block in block_list:
        
        collision_list = pygame.sprite.spritecollide(block, player_list, False)

        for player in collision_list:

            if PlayerMove == 4:
                player.update(0)
                PlayerMoving = False
                player.rect.y -= 3
                PlayerMove = 0
            elif PlayerMove == 3:
                player.update(0)
                PlayerMoving = False
                player.rect.y += 3
                PlayerMove = 0
            elif PlayerMove == 2:
                player.update(0)
                PlayerMoving = False
                player.rect.x -= 3
                PlayerMove = 0
            elif PlayerMove == 1:
                player.update(0)
                PlayerMoving = False
                player.rect.x += 3
                PlayerMove = 0
                
        #endfor

    for node in node_list:
        
        move_list = pygame.sprite.spritecollide(node, player_list, False)

        for player in move_list:

            if node.rect.x == player.rect.x and node.rect.y == player.rect.y:

                PlayerMove = nextMove[0]

            #endif
                
        #endfor
            
    all_sprites_list.draw(screen)
    # -- flip display to reveal new position of objects
    pygame.display.flip()

    # - The clock ticks over
    clock.tick(60)
#endprocedure

    
### -- Game Loop

#End While - End of game loop

pygame.quit()
