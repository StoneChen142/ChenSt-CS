import pygame, sys
from random import randint
import math
import time
from pygame.locals import *

#Menu
def menu():
    game_start = False
    while game_start == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                #endfunction close everything
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_start = True
                    game()
                #endif
            #End If
        #endfor

        screen.fill (WHITE)

        p1_font = pygame.font.Font('freesansbold.ttf',90)
        p1_text = p1_font.render('Pong Game', True, BLACK, WHITE) 
        p1_textRect = p1_text.get_rect()
        p1_textRect.center = (300,280)
        display_surface.blit(p1_text, p1_textRect)
        
        but_font = pygame.font.Font('freesansbold.ttf',30)
        but_text = but_font.render('Press Space to Start', True, BLACK, WHITE) 
        but_textRect = but_text.get_rect()
        but_textRect.center = (300,380)
        display_surface.blit(but_text, but_textRect)

        h_score_font = pygame.font.Font('freesansbold.ttf',20)
        h_score_text = h_score_font.render('Highest Score: ', True, RED, BLACK) 
        h_score_textRect = h_score_text.get_rect()
        h_score_textRect.center = (500,30)
        display_surface.blit(h_score_text, h_score_textRect)


        pygame.display.flip()

        clock.tick(60)
    #endwhile
#endfunction

#Start the game
def game():
    score = 0
    game_over = False
    block_y = 300
    com_y = 300
    x_offset = 2
    y_offset = 2
    pos_x = 100
    pos_y = 300
    Round = 0
    while game_over == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        font = pygame.font.Font('freesansbold.ttf',20)
        text = font.render('Score '+str(score), True, RED, WHITE) 
        textRect = text.get_rect()
        textRect.center = (300,20)
        display_surface.blit(text, textRect)

        if Round < 99:
            if x_offset < 0:
                x_offset -= 0.0001
            else:
                x_offset += 0.0001
        
        pos_x = pos_x + x_offset
        pos_y = pos_y + y_offset
        
        if pos_y == 582 or pos_y > 582:#Ball Condition
            y_offset = y_offset*-1
        elif pos_y == 0 or pos_y < 0:
            y_offset = y_offset*-1
        elif pos_x > 582 or pos_x < 0:
            game_over = True
            finish(score)
        #Player Paddle
        elif pos_x < 12 and pos_y > block_y-20 and pos_y < block_y + 65:
            x_offset = x_offset*-1
            score += 50
            Round += 1
        #Computer Paddle
        elif pos_x > 568 and pos_y > com_y-20 and pos_y < com_y + 65:
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
        screen.blit(text, textRect)
        
        pygame.draw.rect(screen,BLUE, (0, block_y, 12, 65))
        pygame.draw.rect(screen,RED, (pos_x, pos_y, 20, 20))
        pygame.draw.rect(screen,YELLOW, (588, com_y, 12, 65))

        pygame.display.flip()

        clock.tick(60)
    #endwhile
    Score = score
#endfunction

def finish(Score):
    Continue = False
    while Continue == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    Continue = True
                    menu()
        
        screen.fill (WHITE)
        
        p1_font = pygame.font.Font('freesansbold.ttf',70)
        p1_text = p1_font.render('Your Score: '+str(Score), True, RED, WHITE) 
        p1_textRect = p1_text.get_rect()
        p1_textRect.center = (300,300)
        display_surface.blit(p1_text, p1_textRect)
        
        but_font = pygame.font.Font('freesansbold.ttf',25)
        but_text = but_font.render('Press Space to continue', True, BLACK, WHITE) 
        but_textRect = but_text.get_rect()
        but_textRect.center = (300,380)
        display_surface.blit(but_text, but_textRect)

        h_score_font = pygame.font.Font('freesansbold.ttf',20)
        h_score_text = h_score_font.render('Highest Score: ', True, RED, BLACK) 
        h_score_textRect = h_score_text.get_rect()
        h_score_textRect.center = (500,30)
        display_surface.blit(h_score_text, h_score_textRect)

        pygame.display.flip()

        clock.tick(60)
    #endwhile
#endfunction
     
def scoreboard():
    f = open("text.txt","rt")
    data=f.read()
#endfunction

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

display_surface = pygame.display.set_mode((600,600))

game_close = False

### -- Game Loop
while not game_close:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_close = True
        #End If
            
    # -- Game logic goes after this comment

    menu()
    
#End While - End of game loop

pygame.quit()
