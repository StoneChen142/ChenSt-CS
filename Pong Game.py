import pygame
from random import randint
import math
import time

# -- Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)
RED = (255,0,0)

# -- Initialise PyGame
pygame.init()

# -- Manages how fast screen refreshes

clock = pygame.time.Clock()


# -- Blank Screen
size = (600,600)
screen = pygame.display.set_mode(size)

# -- Title of new window/screen
pygame.display.set_caption("Pong Game")

game_over = False
game_new = False
block_y = 300
com_y = 300
x_offset = 2
y_offset = 2
pos_x = 100
pos_y = 300
Round = 3
score = 0

### -- Game Loop
while not game_over:
    # -- User input and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        #End If
            
    # -- Game logic goes after this comment

    pos_x = pos_x + x_offset
    pos_y = pos_y + y_offset
    
    if pos_y == 582:#Ball Condition
        y_offset = y_offset*-1
    elif pos_y == 0:
        y_offset = y_offset*-1
    #elif pos_x == 582:
        #x_offset = x_offset*-1
    elif pos_x == 0:
        x_offset = x_offset*-1
    #Player Paddle
    elif pos_x < 12 and pos_y > block_y and pos_y < block_y + 65:
        x_offset = x_offset*-1
    #Computer Paddle
    elif pos_x > 588 and pos_y > com_y and pos_y < com_y + 65:
        x_offset = x_offset*-1
    #endif
    
    keys = pygame.key.get_pressed()#Player Control
    
    if keys[pygame.K_UP]:
        block_y = block_y - 3
    elif keys[pygame.K_DOWN]:
        block_y = block_y + 3
    #endif

    if pos_y+3 > com_y:#Computer Control
        com_y = com_y + 3
    elif pos_y-3 < com_y:
        com_y = com_y - 3
    #endif
        
    screen.fill (WHITE)
    
    pygame.draw.rect(screen,BLUE, (0, block_y, 12, 65))
    pygame.draw.rect(screen,RED, (pos_x, pos_y, 20, 20))
    pygame.draw.rect(screen,YELLOW, (588, com_y, 12, 65))

    pygame.display.flip()

    clock.tick(60)

#End While - End of game loop

pygame.quit()
