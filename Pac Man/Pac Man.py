import pygame
from random import randint
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
# -- Classes

#Player class
class Player(pygame.sprite.Sprite):
 
    def __init__(self):
        super().__init__()
 
        self.image = pygame.Surface([36, 36])
        self.image = pygame.image.load("PacManFull.png").convert()
        self.image = pygame.transform.scale(self.image, (36, 36))
        self.rect = self.image.get_rect()
        self.angle = 0
        
    #endfunction
 
    def update(self,n):

        if n == 1:
            if self.rect.x > 0:
                self.rect.x -= 2
        elif n == 2:
            if self.rect.x < 564:
                self.rect.x += 2
        elif n == 3:
            if self.rect.y > 0:
                self.rect.y -= 3
        elif n == 4:
            if self.rect.y < 564:
                self.rect.y += 3
        #endif

    #endfunction
                
#EndClass

# -- Initialise PyGame
pygame.init()

# -- Manages how fast screen refreshes

clock = pygame.time.Clock()

# -- Blank Screen
size = (600,600)
screen = pygame.display.set_mode(size)

# -- Title of new window/screen
pygame.display.set_caption("Pac Man")

clock =pygame.time.Clock()

game_over = False

all_sprites_list = pygame.sprite.Group()

player = Player()
player.rect.x = 300
all_sprites_list.add(player)

PlayerMove = 0
    
while game_over == False:
# -- User input and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                PlayerMove = 1
            elif event.key == pygame.K_d:
                PlayerMove = 2
            elif event.key == pygame.K_w:
                PlayerMove = 3
            elif event.key == pygame.K_s:
                PlayerMove = 4
                #endif
            #endif
        #End If
    #Next event

    screen.fill(BLACK)

    player.update(PlayerMove)            
    
    all_sprites_list.draw(screen)
    # -- flip display to reveal new position of objects
    pygame.display.flip()

    # - The clock ticks over
    clock.tick(60)
#endprocedure

    
### -- Game Loop

#End While - End of game loop

pygame.quit()
