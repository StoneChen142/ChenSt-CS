### SRC - This is a very impressive attempt at pong. You have clearly learnt a lot.
### SRC - We will now start looking at how we can use OOP to simplify the code.

import pygame
import random
import math
import time
from pygame.locals import *

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

#Menu
def menu():
    game_start = False
    highestScore = ""
    f = open("Score_Board.txt","r+")
    data=f.read()
    for i in range(3,8):
        highestScore = highestScore + data[i]
    #endfor
    f.close()
    while game_start == False:
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                pygame.quit()
            #endif
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pos>(105,385) and pos<(255,465):
                    game_start = True
                    game()
                if pos>(350,385) and pos<(500,465):
                    game_start = True
                    mgame()
                #endif
            #endif
        #endfor
        
        screen.fill (WHITE)

        p1_font = pygame.font.Font('freesansbold.ttf',90)
        p1_text = p1_font.render('Pong Game', True, BLACK, WHITE) 
        p1_textRect = p1_text.get_rect()
        p1_textRect.center = (300,280)
        display_surface.blit(p1_text, p1_textRect)

        h_score_font = pygame.font.Font('freesansbold.ttf',20)
        h_score_text = h_score_font.render('Highest Score: '+highestScore, True, RED, BLACK) 
        h_score_textRect = h_score_text.get_rect()
        h_score_textRect.center = (480,30)
        display_surface.blit(h_score_text, h_score_textRect)

        #Button Code
        pygame.draw.rect(screen,GREEN, (105, 385, 150, 80))
        buttonText("START", BLACK, 130, 400, 100,  50, size="small")

        pygame.draw.rect(screen,BLUE, (350, 385, 150, 80))
        buttonText("MULTI", BLACK, 375, 400, 100,  50, size="small")

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

        #Change Speed
        if Round < 99:
            if x_offset < 0:
                x_offset -= 0.0001
            elif x_offset > 0:
                x_offset += 0.0001
            elif y_offset < 0:
                y_offset -= 0.00006
            elif y_offset > 0:
                y_offset += 0.00006
        
        pos_x = pos_x + x_offset
        pos_y = pos_y + y_offset
        
        if pos_y == 582 or pos_y > 582:#Ball Condition
            y_offset = y_offset*-1
        elif pos_y == 0 or pos_y < 0:
            y_offset = y_offset*-1
        elif pos_x > 582 or pos_x < 0:
            game_over = True
            entername(score)
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

#Start the Multiplayer game
def mgame():
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
        text = font.render('P1               Last player standing wins               P2', True, RED, WHITE) 
        textRect = text.get_rect()
        textRect.center = (300,20)
        display_surface.blit(text, textRect)

        #Change Speed
        if Round < 99:
            if x_offset < 0:
                x_offset -= 0.0002
            elif x_offset > 0:
                x_offset += 0.0002
            elif y_offset < 0:
                y_offset -= 0.00012
            elif y_offset > 0:
                y_offset += 0.00012
        
        pos_x = pos_x + x_offset
        pos_y = pos_y + y_offset
        
        if pos_y == 582 or pos_y > 582:#Ball Condition
            y_offset = y_offset*-1
        elif pos_y == 0 or pos_y < 0:
            y_offset = y_offset*-1
        elif pos_x > 582:
            game_over = True
            mfinish(1)
        elif pos_x < 0:
            game_over = True
            mfinish(2)
            
        #Player 1 Paddle
        elif pos_x < 12 and pos_y > block_y-20 and pos_y < block_y + 65:
            x_offset = x_offset*-1
            Round += 1
        #Player 2 Paddle
        elif pos_x > 568 and pos_y > com_y-20 and pos_y < com_y + 65:
            x_offset = x_offset*-1
        #endif
        
        keys = pygame.key.get_pressed()#Player Control
        
        #P1 control
        if keys[pygame.K_w]:
            block_y = block_y - 3
        elif keys[pygame.K_s]:
            block_y = block_y + 3
        #endif

        #P2 control
        if keys[pygame.K_UP]:
            com_y = com_y - 3
        elif keys[pygame.K_DOWN]:
            com_y = com_y + 3
        #endif
            
        screen.fill (WHITE)
        screen.blit(text, textRect)
        
        pygame.draw.rect(screen,BLUE, (0, block_y, 12, 65))
        pygame.draw.rect(screen,RED, (pos_x, pos_y, 20, 20))
        pygame.draw.rect(screen,YELLOW, (588, com_y, 12, 65))

        pygame.display.flip()

        clock.tick(60)
    #endwhile
#endfunction

#Multiplayer finish screen
def mfinish(num):
    Continue = False
    while Continue == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    Continue = True
                    menu()
                #endif
            #endif
        #endfor
        
        screen.fill (WHITE)
        
        p1_font = pygame.font.Font('freesansbold.ttf',80)
        p1_text = p1_font.render('Player '+str(num) + " Won!", True, RED, WHITE) 
        p1_textRect = p1_text.get_rect()
        p1_textRect.center = (300,200)
        display_surface.blit(p1_text, p1_textRect)

        but1_font = pygame.font.Font('freesansbold.ttf',30)
        but1_text = but1_font.render('Press Space to continue', True, BLACK, WHITE) 
        but1_textRect = but1_text.get_rect()
        but1_textRect.center = (300,430)
        display_surface.blit(but1_text, but1_textRect)

        pygame.display.flip()

        clock.tick(60)
    #endwhile
#endfunction

#Restart screen
def finish(Score):
    Continue = False
    highestScore=""
    f = open("Score_Board.txt","r+")
    data=f.read()
    for i in range(3,8):
        highestScore = highestScore + data[i]
    #endfor
    f.close()
    while Continue == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    Continue = True
                    menu()
                #endif
            #endif
        #endfor
        
        screen.fill (WHITE)
        
        p1_font = pygame.font.Font('freesansbold.ttf',30)
        p1_text = p1_font.render('Your Score: '+str(Score), True, RED, WHITE) 
        p1_textRect = p1_text.get_rect()
        p1_textRect.center = (300,320)
        display_surface.blit(p1_text, p1_textRect)

        p2_font = pygame.font.Font('freesansbold.ttf',45)
        p2_text = p2_font.render('the Highest Score?', True, BLACK, WHITE) 
        p2_textRect = p2_text.get_rect()
        p2_textRect.center = (300,260)
        display_surface.blit(p2_text, p2_textRect)
        
        but_font = pygame.font.Font('freesansbold.ttf',45)
        but_text = but_font.render('Think You Can Beat', True, BLACK, WHITE) 
        but_textRect = but_text.get_rect()
        but_textRect.center = (300,215)
        display_surface.blit(but_text, but_textRect)

        but1_font = pygame.font.Font('freesansbold.ttf',30)
        but1_text = but1_font.render('Press Space to continue', True, BLACK, WHITE) 
        but1_textRect = but1_text.get_rect()
        but1_textRect.center = (300,450)
        display_surface.blit(but1_text, but1_textRect)

        h_score_font = pygame.font.Font('freesansbold.ttf',30)
        h_score_text = h_score_font.render('Highest Score: '+str(highestScore), True, RED, BLACK) 
        h_score_textRect = h_score_text.get_rect()
        h_score_textRect.center = (300,345)
        display_surface.blit(h_score_text, h_score_textRect)

        pygame.display.flip()

        clock.tick(60)
    #endwhile
#endfunction

#Entername
def entername(Score):
    name=""
    done=False
    highestScore=""
    highName=""
    #Get Highest Score
    f = open("Score_Board.txt","r+")
    data=f.read()
    for i in range(3,8):
        highestScore = highestScore + data[i]
    #endfor
    j=8
    while data[j] != "\n":
        highName = highName + data[j]
        j+=1
    #endwhile
    f.close()
    
    while done == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    done = True
                    nextpage(Score)
                #endif
            #endif
        #endfor

        screen.fill(WHITE)
        
        p1_font = pygame.font.Font('freesansbold.ttf',30)
        p1_text = p1_font.render('Enter your name in the next page', True, RED, WHITE) 
        p1_textRect = p1_text.get_rect()
        p1_textRect.center = (300,210)
        screen.blit(p1_text, p1_textRect)

        p2_font = pygame.font.Font('freesansbold.ttf',30)
        p2_text = p2_font.render('Press "Space" to continue', True, RED, WHITE) 
        p2_textRect = p2_text.get_rect()
        p2_textRect.center = (300,245)
        screen.blit(p2_text, p2_textRect)

        y_score_font = pygame.font.Font('freesansbold.ttf',40)
        y_score_text = y_score_font.render('Your Score: '+str(Score), True, RED, BLACK) 
        y_score_textRect = y_score_text.get_rect()
        y_score_textRect.center = (300,320)
        screen.blit(y_score_text, y_score_textRect)

        h_score_font = pygame.font.Font('freesansbold.ttf',40)
        h_score_text = h_score_font.render('Highest Score: '+str(highestScore)+str(highName), True, RED, BLACK) 
        h_score_textRect = h_score_text.get_rect()
        h_score_textRect.center = (300,360)
        screen.blit(h_score_text, h_score_textRect)

        pygame.display.flip()

        clock.tick(60)
    #endwhile
    pygame.display.flip()

    clock.tick(60)
#endfunction
        
#Next page
def nextpage(Score):
    size = (600,600)
    screen = pygame.display.set_mode(size)
    font = pygame.font.Font(None, 32)
    input_box = pygame.Rect(200, 280, 140, 32)
    color_inactive = (0,0,0)
    color_active = (235,52,52)
    color = color_inactive
    active = False
    text = ''
    done = False

    while done == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False
                # Change the current color of the input box.
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        scoreboard(Score,text)
                        done = True
                        leaderboard()
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        p_font = pygame.font.Font('freesansbold.ttf',30)
        p_text = p_font.render('Press "Space" to continue', True, RED, BLACK) 
        p_textRect = p_text.get_rect()
        p_textRect.center = (300,480)
        screen.blit(p_text, p_textRect)

        screen.fill(WHITE)
        # Render the current text.
        txt_surface = font.render(text, True, color)
        # Resize the box if the text is too long.
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        # Blit the text.
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        # Blit the input_box rect.
        pygame.draw.rect(screen, color, input_box, 2)

        pygame.display.flip()
        
        clock.tick(60)
    #endwhile
#endfunction

def leaderboard():
    f = open("Score_Board.txt","r+")
    #Reading data
    lines = f.readlines()
    f.close()
    output = ["","","","",""]
    for i in range(0,5):
        j=0
        while str((lines[i])[j]) != "\n":
            output[i] = output[i] + (lines[i])[j]
            j+=1
        #endwhile
    #endfor
    done = False
    while done == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    done = True
                    menu()

        screen.fill(WHITE)
        
        p_font = pygame.font.Font('freesansbold.ttf',30)
        p_text = p_font.render('Press "Space" to continue', True, RED, WHITE) 
        p_textRect = p_text.get_rect()
        p_textRect.center = (300,480)
        screen.blit(p_text, p_textRect)

        h_score_font = pygame.font.Font('freesansbold.ttf',80)
        h_score_text = h_score_font.render('Leader Board', True, RED, BLACK) 
        h_score_textRect = h_score_text.get_rect()
        h_score_textRect.center = (300,100)
        screen.blit(h_score_text, h_score_textRect)

        p1_font = pygame.font.Font('freesansbold.ttf',30)
        p1_text = p1_font.render(str(output[0]), True, RED, WHITE) 
        p1_textRect = p1_text.get_rect()
        p1_textRect.center = (300,240)
        screen.blit(p1_text, p1_textRect)

        p2_font = pygame.font.Font('freesansbold.ttf',30)
        p2_text = p2_font.render(str(output[1]), True, RED, WHITE) 
        p2_textRect = p2_text.get_rect()
        p2_textRect.center = (300,280)
        screen.blit(p2_text, p2_textRect)

        p3_font = pygame.font.Font('freesansbold.ttf',30)
        p3_text = p3_font.render(str(output[2]), True, RED, WHITE) 
        p3_textRect = p3_text.get_rect()
        p3_textRect.center = (300,320)
        screen.blit(p3_text, p3_textRect)

        p4_font = pygame.font.Font('freesansbold.ttf',30)
        p4_text = p4_font.render(str(output[3]), True, RED, WHITE) 
        p4_textRect = p4_text.get_rect()
        p4_textRect.center = (300,360)
        screen.blit(p4_text, p4_textRect)

        p5_font = pygame.font.Font('freesansbold.ttf',30)
        p5_text = p5_font.render(str(output[4]), True, RED, WHITE) 
        p5_textRect = p5_text.get_rect()
        p5_textRect.center = (300,400)
        screen.blit(p5_text, p5_textRect)

        pygame.display.flip()
        
        clock.tick(60)
    #endwhile
#endfunction
        
#Score
def scoreboard(score,name):
    f = open("Score_Board.txt","r+")
    #Reading data
    name = str(name)
    score = str(score)
    score_length=len(score)
    lines = f.readlines()
    maximum = 5
    data = ""
    f.close()
    #Formatting the score
    if score_length < 5:
        while score_length != 5:
            score = "0"+score
            score_length += 1
    addLine = ") "+score+"   "+name+"\n"
    #Evaluating the score
    rank = 0
    num = 0
    added = False
    while num < maximum:
        big = False
        same = False
        TF = ""
        line=str(lines[rank])
        print(line)
        for j in range(3,7):
            if int(score[j-3]) > int(line[j]):
                TF = TF + "T"
            elif int(score[j-3]) == int(line[j]):
                TF = TF + "S"
            else:
                TF = TF + "F"
            #endif
        #endfor
        #Evaluating
        if added == False:
            if TF[1] == "T" or TF[:2] == "ST" or TF[:3] == "SST" or TF[:4] == "SSST":
                big = True
            elif TF == "SSSS":
                same = True
            else:
                big = False
                same = False
            #endif
        #endif
            
        if same == True:
            data = data + str(num+1) + line[1:]
            rank += 1
            num += 1
        elif big == True and added == False:
            data = data + str(num+1) + addLine
            big = False
            rank += 1
            num += 1
            added = True
            same=False
            if num < 4:
                data = data + str(num+1) + line[1:]
                num += 1
            #endif
        else:
            data = data + str(num+1) + line[1:]
            rank += 1
            num += 1
        #endif
        print(rank)
    #endwhile
    f = open("Score_Board.txt","w+")
    f.write(data)  
    f.close()
#endfunction

# -- Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)
RED = (255,0,0)
GREEN = (0,255,0)
DGREEN = (15,186,35)

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
