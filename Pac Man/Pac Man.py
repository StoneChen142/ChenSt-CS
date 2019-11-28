import pygame
import random
# -- Global Constants

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

#Animations

moveRight = [pygame.transform.scale(pygame.image.load('PacManRight1.png'), (36, 36)), pygame.transform.scale(pygame.image.load('PacManRight2.png'), (36, 36)),pygame.transform.scale(pygame.image.load('PacManFull.png'), (36, 36)),pygame.transform.scale(pygame.image.load('PacManRight2.png'), (36, 36))]
moveLeft = []
moveDown = [pygame.image.load('PacManDown1.png'), pygame.image.load('PacManDown2.png'), pygame.image.load('PacManFull.png'), pygame.image.load('PacManDown1.png')]
moveUp = [pygame.image.load('PacManUp1.png'), pygame.image.load('PacManUp2.png'), pygame.image.load('PacManFull.png'), pygame.image.load('PacManUp1.png')]

notMoving = pygame.image.load('PacManUp1.png')
#procedures

def drawWindow():
    global pmoveCount

    if pmoveCount + 1 >= 60:
        pmoveCount = 0
    #endif
    
    if right:
        screen.blit(moveRight[pmoveCount//12], (player.rect.x, player.rect.y))
        pmoveCount += 1

def createMaze():
    f = open("mazeSheet")
    f.close()

#endprocedure
    
# -- Classes

#Player class
class Player(pygame.sprite.Sprite):
 
    def __init__(self):
        super().__init__()
 
        self.image = pygame.Surface([36, 36])
        self.image = pygame.transform.scale(self.image, (36, 36))
        self.rect = self.image.get_rect()
        
    #endfunction
 
    def update(self,n):
        global PlayerMoving

        if n == 1:
            if self.rect.x > 0:
                self.rect.x -= 3
            else:
                self.image = self.full
                PlayerMoving = False
                self.num = 0
        elif n == 2:
            if self.rect.x < 564:
                self.rect.x += 3
            else:
                self.image = self.full
                PlayerMoving = False
                self.num = 0
        elif n == 3:
            if self.rect.y > 0:
                self.rect.y -= 3
            else:
                self.image = self.full
                PlayerMoving = False
                self.num = 0
        elif n == 4:
            if self.rect.y < 564:
                self.rect.y += 3
            else:
                screen.blit(notMoving, (self.rect.x, self.rect.y))
                PlayerMoving = False
                self.num = 0
        #endif

    #endfunction
                
    #endprocedure   
                
#EndClass

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

player = Player()
player.rect.x = 36
player.rect.y = 0
all_sprites_list.add(player)

PlayerMove = 0
PlayerMoving = False
    
while game_over == False:
# -- User input and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                PlayerMove = 1
                left = True
            elif event.key == pygame.K_d:
                PlayerMove = 2
                right = True
            elif event.key == pygame.K_w:
                PlayerMove = 3
                up = True
            elif event.key == pygame.K_s:
                PlayerMove = 4
                down = True
                #endif
            #endif
        #End If
    #Next event

    screen.fill(BLACK)

    player.update(PlayerMove)

    drawWindow()
            
    all_sprites_list.draw(screen)
    # -- flip display to reveal new position of objects
    pygame.display.flip()

    # - The clock ticks over
    clock.tick(60)
#endprocedure

    
### -- Game Loop

#End While - End of game loop

pygame.quit()
