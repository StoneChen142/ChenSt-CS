import pygame
import random
# -- Global Constants

f = open("RouteSheet.txt","r+")
lines = f.readlines()
length = len(lines)
print(length)
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
nextMove[0] = 0

size_x = 34
size_y = 34

#Animations

moveDown = [pygame.transform.scale(pygame.image.load('PacManRight1.png'), (size_x, size_y)), pygame.transform.scale(pygame.image.load('PacManRight2.png'), (size_x, size_y)),pygame.transform.scale(pygame.image.load('PacManFull.png'), (size_x, size_y)),pygame.transform.scale(pygame.image.load('PacManRight2.png'), (size_x, size_y))]
moveUp = [pygame.transform.scale(pygame.image.load('PacManLeft1.png'), (size_x, size_y)), pygame.transform.scale(pygame.image.load('PacManLeft2.png'), (size_x, size_y)),pygame.transform.scale(pygame.image.load('PacManFull.png'), (size_x, size_y)),pygame.transform.scale(pygame.image.load('PacManLeft2.png'), (size_x, size_y))]
moveRight = [pygame.transform.scale(pygame.image.load('PacManDown1.png'), (size_x, size_y)), pygame.transform.scale(pygame.image.load('PacManDown2.png'), (size_x, size_y)),pygame.transform.scale(pygame.image.load('PacManFull.png'), (size_x, size_y)),pygame.transform.scale(pygame.image.load('PacManDown2.png'), (size_x, size_y))]
moveLeft = [pygame.transform.scale(pygame.image.load('PacManUp1.png'), (size_x, size_y)), pygame.transform.scale(pygame.image.load('PacManUp2.png'), (size_x, size_y)),pygame.transform.scale(pygame.image.load('PacManFull.png'), (size_x, size_y)),pygame.transform.scale(pygame.image.load('PacManUp2.png'), (size_x, size_y))]

notMovingDown = pygame.transform.scale(pygame.image.load('PacManDown2.png'), (size_x, size_y))
notMovingUp = pygame.transform.scale(pygame.image.load('PacManUp2.png'), (size_x, size_y))
notMovingLeft = pygame.transform.scale(pygame.image.load('PacManLeft2.png'), (size_x, size_y))
notMovingRight = pygame.transform.scale(pygame.image.load('PacManRight2.png'), (size_x, size_y))

ShadowRight = [pygame.transform.scale(pygame.image.load('ShadowDown1.png'), (size_x, size_y)), pygame.transform.scale(pygame.image.load('ShadowDown2.png'), (size_x, size_y))]
ShadowLeft = [pygame.transform.scale(pygame.image.load('ShadowUp1.png'), (size_x, size_y)), pygame.transform.scale(pygame.image.load('ShadowUp2.png'), (size_x, size_y))]
ShadowUp = [pygame.transform.scale(pygame.image.load('ShadowLeft1.png'), (size_x, size_y)), pygame.transform.scale(pygame.image.load('ShadowLeft2.png'), (size_x, size_y))]
ShadowDown = [pygame.transform.scale(pygame.image.load('ShadowRight1.png'), (size_x, size_y)), pygame.transform.scale(pygame.image.load('ShadowRight2.png'), (size_x, size_y))]

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

#Player class
class Player(pygame.sprite.Sprite):
 
    def __init__(self):
        super().__init__()
 
        self.image = pygame.Surface([34, 34])
        self.image = pygame.transform.scale(pygame.image.load('PacManFull.png'), (34, 34))
        self.rect = self.image.get_rect()
        self.num = 0
        
    #endfunction
 
    def update(self,n,PlayerMoving):
        global left
        global right
        global up
        global down

        if PlayerMoving == True:
            
            if n == 1:

                self.rect.x -= 1
                if self.rect.x < -36:

                    self.rect.x = 540

            elif n == 2:
                
                self.rect.x += 1
                if self.rect.x > 540:

                    self.rect.x = -36

                #endif
                    
            elif n == 3:

                self.rect.y -= 1
                if self.rect.y < -36:

                    self.rect.y = 540

                #endif

            elif n == 4:

                self.rect.y += 1
                if self.rect.y > 540:

                    self.rect.y = -36

                #endif

            #endif
        #endif
    #endprocedure

    def animation(self,num,PlayerMoving):
        global left
        global right
        global up
        global down
        global PlayerMove

        if PlayerMoving == True:         
            
            if num == 1:
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

        else:

            if PlayerMove == 1:
                
                self.image = notMovingLeft

            elif PlayerMove == 2:

                self.image = notMovingRight

            elif PlayerMove == 3:

                self.image = notMovingUp

            elif PlayerMove == 4:

                self.image = notMovingDown

            elif PlayerMove == 0:

                self.image = notMovingRight

            #endif
               
    #endprocedure   
                
#EndClass

#Ghost Class
class Shadow(pygame.sprite.Sprite):
 
    def __init__(self):
        super().__init__()
 
        self.image = pygame.Surface([36, 36])
        self.image = pygame.transform.scale(pygame.image.load('ShadowDown2.png'), (36, 36))
        self.rect = self.image.get_rect()
        self.num = 0
        
    #endfunction
 
    def update(self,n):

        if n == 1:

            self.rect.x -= 1
            if self.rect.x < -36:

                self.rect.x = 540

        elif n == 2:
            
            self.rect.x += 1
            if self.rect.x > 540:

                self.rect.x = -36

            #endif
                
        elif n == 3:

            self.rect.y -= 1
            if self.rect.y < -36:

                self.rect.y = 540

            #endif

        elif n == 4:

            self.rect.y += 1
            if self.rect.y > 540:

                self.rect.y = -36

            #endif

        #endif

    #endprocedure

    def animation(self,num):
            
        if num == 1:
            if self.num == 0:
                self.image = ShadowUp[self.num]
                self.num += 1
            elif self.num == 1:
                self.image = ShadowUp[self.num]
                self.num = 0
            #endif
        elif num == 2:
            if self.num == 0:
                self.image = ShadowDown[self.num]
                self.num += 1
            elif self.num == 1:
                self.image = ShadowDown[self.num]
                self.num = 0
            #endif
        elif num == 3:
            if self.num == 0:
                self.image = ShadowLeft[self.num]
                self.num += 1
            elif self.num == 1:
                self.image = ShadowLeft[self.num]
                self.num = 0
            #endif
        elif num == 4:
            if self.num == 0:
                self.image = ShadowRight[self.num]
                self.num += 1
            elif self.num == 1:
                self.image = ShadowRight[self.num]
                self.num = 0
            #endif
        #endif
               
    #endprocedure   
                
#EndClass

class Maze(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        self.image = pygame.Surface([508,540])
        self.image = pygame.image.load("maze.png").convert()
        self.image = pygame.transform.scale(self.image, (508, 540))
        self.rect = self.image.get_rect()
        
    #endprocedure

#endclass

class Node(pygame.sprite.Sprite):
    def __init__(self,width,height):
        super().__init__()
        
        self.image = pygame.Surface([width,height])
        self.rect = self.image.get_rect()
        
    #endprocedure

#endclass

class DownRightNode(pygame.sprite.Sprite):
    def __init__(self,width,height):
        super().__init__()
        
        self.image = pygame.Surface([width,height])
        self.rect = self.image.get_rect()
        
    #endprocedure

#endclass

class DownVertNode(pygame.sprite.Sprite):
    def __init__(self,width,height):
        super().__init__()
        
        self.image = pygame.Surface([width,height])
        self.rect = self.image.get_rect()
        
    #endprocedure

#endclass

class UpVertNode(pygame.sprite.Sprite):
    def __init__(self,width,height):
        super().__init__()
        
        self.image = pygame.Surface([width,height])
        self.rect = self.image.get_rect()
        
    #endprocedure

#endclass

class DownLeftNode(pygame.sprite.Sprite):
    def __init__(self,width,height):
        super().__init__()
        
        self.image = pygame.Surface([width,height])
        self.rect = self.image.get_rect()
        
    #endprocedure

#endclass

class LeftVertNode(pygame.sprite.Sprite):
    def __init__(self,width,height):
        super().__init__()
        
        self.image = pygame.Surface([width,height])
        self.rect = self.image.get_rect()
        
    #endprocedure

#endclass

class RightVertNode(pygame.sprite.Sprite):
    def __init__(self,width,height):
        super().__init__()
        
        self.image = pygame.Surface([width,height])
        self.rect = self.image.get_rect()
        
    #endprocedure

#endclass

class UpRightNode(pygame.sprite.Sprite):
    def __init__(self,width,height):
        super().__init__()
        
        self.image = pygame.Surface([width,height])
        self.rect = self.image.get_rect()
        
    #endprocedure

#endclass

class UpLeftNode(pygame.sprite.Sprite):
    def __init__(self,width,height):
        super().__init__()
        
        self.image = pygame.Surface([width,height])
        self.rect = self.image.get_rect()
        
    #endprocedure

#endclass

class DownHoriNode(pygame.sprite.Sprite):
    def __init__(self,width,height):
        super().__init__()
        
        self.image = pygame.Surface([width,height])
        self.rect = self.image.get_rect()
        
    #endprocedure

#endclass

class UpHoriNode(pygame.sprite.Sprite):
    def __init__(self,width,height):
        super().__init__()
        
        self.image = pygame.Surface([width,height])
        self.rect = self.image.get_rect()
        
    #endprocedure

#endclass

class vertical(pygame.sprite.Sprite):
    def __init__(self,width,height):
        super().__init__()
        
        self.image = pygame.Surface([width,height])
        self.rect = self.image.get_rect()
        
    #endprocedure

#endclass

class horizontal(pygame.sprite.Sprite):
    def __init__(self,width,height):
        super().__init__()
        
        self.image = pygame.Surface([width,height])
        self.rect = self.image.get_rect()
        
    #endprocedure

def createMaze(length, node_list, block_list, all_sprites_list, downRight_list, downLeft_list, hori_list, vert_list, downHori_list, upHori_list, upRight_list, upLeft_list, leftVert_list, rightVert_list):

    maze = Maze()
    maze.rect.x = 0
    maze.rect.y = 30
    all_sprites_list.add(maze)

    #Nodes
    for i in range(length):
        
        line = lines[i-2]
        
        #x position
        if line[1] == "0":
            xpos = int(str(line[2])+str(line[3]))
        elif line[3] == str(0) and line[2] == str(0) and line[1] == str(0) :
            xpos = 0
        else:
            xpos = int(str(line[1])+str(line[2])+str(line[3]))
        #endif

        #y position
        if line[4] == str(0):
            ypos = int(str(line[5])+str(line[6]))
        else:
            ypos = int(str(line[4])+str(line[5])+str(line[6]))
        #endif

        #width
        if line[7] == str(0):
            width = int(str(line[8])+str(line[9]))
        else:
            width = int(str(line[7])+str(line[8])+str(line[9]))
        #endif

        #height
        if line[10] == str(0):
            height = int(str(line[11])+str(line[12]))
        else:
            height = int(str(line[10])+str(line[11])+str(line[12]))
        #endif
                
        if line[0] == str(1):

            node = Node(width,height)
            node.rect.x = xpos
            node.rect.y = ypos
            node_list.add(node)
            all_sprites_list.add(node)

        elif line[0] == str(2):

            node = DownRightNode(width,height)
            node.rect.x = xpos
            node.rect.y = ypos
            downRight_list.add(node)
            all_sprites_list.add(node)

        elif line[0] == str(3):

            node = DownLeftNode(width,height)
            node.rect.x = xpos
            node.rect.y = ypos
            downLeft_list.add(node)
            all_sprites_list.add(node)

        elif line[0] == str(4):

            node = horizontal(width,height)
            node.rect.x = xpos
            node.rect.y = ypos
            hori_list.add(node)
            all_sprites_list.add(node)

        elif line[0] == str(5):

            node = vertical(width,height)
            node.rect.x = xpos
            node.rect.y = ypos
            vert_list.add(node)
            all_sprites_list.add(node)

        elif line[0] == str(6):

            node = DownHoriNode(width,height)
            node.rect.x = xpos
            node.rect.y = ypos
            downHori_list.add(node)
            all_sprites_list.add(node)

        elif line[0] == str(7):

            node = UpHoriNode(width,height)
            node.rect.x = xpos
            node.rect.y = ypos
            upHori_list.add(node)
            all_sprites_list.add(node)

        elif line[0] == str(8):

            node = UpRightNode(width,height)
            node.rect.x = xpos
            node.rect.y = ypos
            upRight_list.add(node)
            all_sprites_list.add(node)

        elif line[0] == str(9):

            node = UpLeftNode(width,height)
            node.rect.x = xpos
            node.rect.y = ypos
            upLeft_list.add(node)
            all_sprites_list.add(node)

        elif line[0] == str(0):

            node = LeftVertNode(width,height)
            node.rect.x = xpos
            node.rect.y = ypos
            leftVert_list.add(node)
            all_sprites_list.add(node)

        elif line[0] == "a":

            node = RightVertNode(width,height)
            node.rect.x = xpos
            node.rect.y = ypos
            rightVert_list.add(node)
            all_sprites_list.add(node)

        #endif
            

            
#endprocedure

#Menu
def menu():
    game_start = False
    while game_start == False:
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                pygame.quit()
            #endif
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pos>(180,385) and pos<(330,465):
                    game_start = True
                    game()
                #endif
            #endif
        #endfor
        
        screen.fill (BLACK)

        MainText = Text(80,YELLOW,255,280,'PACMAN')

        #Button Code
        pygame.draw.rect(screen,YELLOW, (180, 385, 150, 80))
        buttonText("START", BLACK, 205, 400, 100,  50, size="small")

        pygame.display.flip()

        clock.tick(60)
    #endwhile
#endprocedure

def game():
    game_over = False

    #Variables

    currentX = 252
    currentY = 432

    oldtime = 0
    Soldtime = 0

    all_sprites_list = pygame.sprite.Group()

    block_list = pygame.sprite.Group()

    node_list = pygame.sprite.Group()

    downLeft_list = pygame.sprite.Group()

    downRight_list = pygame.sprite.Group()

    downHori_list = pygame.sprite.Group()

    upHori_list = pygame.sprite.Group()

    upRight_list = pygame.sprite.Group()

    upLeft_list = pygame.sprite.Group()

    leftVert_list = pygame.sprite.Group()

    rightVert_list = pygame.sprite.Group()

    vert_list = pygame.sprite.Group()

    hori_list = pygame.sprite.Group()

    player_list = pygame.sprite.Group()

    ghost_list = pygame.sprite.Group()

    createMaze(length, node_list, block_list, all_sprites_list, downRight_list, downLeft_list, hori_list, vert_list, downHori_list, upHori_list, upRight_list, upLeft_list, leftVert_list, rightVert_list)

    player = Player()
    player.rect.x = 238
    player.rect.y = 424
    all_sprites_list.add(player)
    player_list.add(player)

    shadow = Shadow()
    shadow.rect.x = 252
    shadow.rect.y = 180
    all_sprites_list.add(shadow)
    ghost_list.add(shadow)

    PlayerMove = 0
    ShadowMove = 0
    PlayerMoving = False

    score = 0
    AddNum = 0
        
    while game_over == False:
    # -- User input and controls
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    nextMove[0] = 1
                    left = True
                elif event.key == pygame.K_d:
                    nextMove[0] = 2
                    right = True
                elif event.key == pygame.K_w:
                    nextMove[0] = 3
                    up = True
                elif event.key == pygame.K_s:
                    nextMove[0] = 4
                    down = True
                    #endif
                #endif
            #End If
        #Next event

        screen.fill(BLACK)

        ScoreText = Text(20,RED,255,20,'Score: '+str(score))
        RoundText = Text(20,RED,52,20,'Round: '+str(AddNum))

        player.update(PlayerMove,PlayerMoving)

        #Shadow Chasing Algorithm


        shadow.update(ShadowMove)

        #Update PacMan&Ghosts
        newtime = pygame.time.get_ticks()
        Snewtime = pygame.time.get_ticks()

        if newtime - oldtime > 50 and PlayerMoving == True: 

            player.animation(PlayerMove,PlayerMoving)
            oldtime=newtime
                
        #endif

        if Snewtime - Soldtime > 60:

            shadow.animation(ShadowMove)
            Soldtime=Snewtime

        #endif

        for node in downRight_list:
            
            DRmove_list = pygame.sprite.spritecollide(node, player_list, False)

            for player in DRmove_list:

                if node.rect.x == player.rect.x and node.rect.y == player.rect.y:

                    if nextMove != [] and PlayerMove != 1 and PlayerMove != 3:

                        if nextMove[0] == 4 or nextMove[0] == 2:

                            PlayerMove = nextMove[0]
                            PlayerMoving = True

                        #endif

                    elif PlayerMove == 1 or PlayerMove == 3:

                        PlayerMoving = False
                        PlayerMove = 0
                            
                    #endif

                #endif
                    
            #endfor

        #endfor

        for node in upRight_list:
            
            URmove_list = pygame.sprite.spritecollide(node, player_list, False)

            for player in URmove_list:

                if node.rect.x == player.rect.x and node.rect.y == player.rect.y:

                    if nextMove != [] and PlayerMove != 1 and PlayerMove != 4:

                        if nextMove[0] == 3 or nextMove[0] == 2:

                            PlayerMove = nextMove[0]
                            PlayerMoving = True

                        #endif

                    elif PlayerMove == 1 or PlayerMove == 4:

                        PlayerMoving = False
                        PlayerMove = 0
                        print("Stopped Moving")
                            
                    #endif

                #endif
                    
            #endfor

        #endfor

        for node in downLeft_list:
            
            DLmove_list = pygame.sprite.spritecollide(node, player_list, False)

            for player in DLmove_list:

                if node.rect.x == player.rect.x and node.rect.y == player.rect.y:

                    if nextMove != [] and PlayerMove != 2 and PlayerMove != 3:

                        if nextMove[0] == 4 or nextMove[0] == 1:

                            PlayerMove = nextMove[0]
                            PlayerMoving = True

                        #endif

                    elif PlayerMove == 2 or PlayerMove == 3:

                        PlayerMoving = False
                        PlayerMove = 0
                            
                    #endif

                #endif
                    
            #endfor

        #endfor

        for node in upLeft_list:
            
            ULmove_list = pygame.sprite.spritecollide(node, player_list, False)

            for player in ULmove_list:

                if node.rect.x == player.rect.x and node.rect.y == player.rect.y:

                    if nextMove != [] and PlayerMove != 2 and PlayerMove != 4:

                        if nextMove[0] == 3 or nextMove[0] == 1:

                            PlayerMove = nextMove[0]
                            PlayerMoving = True

                        #endif

                    elif PlayerMove == 2 or PlayerMove == 4:

                        PlayerMoving = False
                        PlayerMove = 0
                            
                    #endif

                #endif
                    
            #endfor

        #endfor

        for node in node_list:
            
            move_list = pygame.sprite.spritecollide(node, player_list, False)

            for player in move_list:

                if node.rect.x == player.rect.x and node.rect.y == player.rect.y:

                    if nextMove != []:
                        
                        PlayerMove = nextMove[0]

                    #endif

                #endif
                    
            #endfor

        #endfor

        for node in vert_list:
            
            vertMove_list = pygame.sprite.spritecollide(node, player_list, False)

            for player in vertMove_list:

                if nextMove[0] == 3 or nextMove[0] == 4:

                    PlayerMove = nextMove[0]
                    PlayerMoving = True

                #endif
                    
            #endfor

        #endfor

        for node in hori_list:
            
            horiMove_list = pygame.sprite.spritecollide(node, player_list, False)

            for player in horiMove_list:

                if nextMove[0] == 1 or nextMove[0] == 2:

                    PlayerMove = nextMove[0]
                    PlayerMoving = True

                #endif
                    
            #endfor

        #endfor

        for node in downHori_list:
            
            DHMove_list = pygame.sprite.spritecollide(node, player_list, False)

            for player in DHMove_list:

                if node.rect.x == player.rect.x and node.rect.y == player.rect.y:

                    if nextMove != [] and PlayerMove != 3:

                        if nextMove[0] == 4 or nextMove[0] == 1 or nextMove[0] == 2:

                            PlayerMove = nextMove[0]
                            PlayerMoving = True

                        #endif

                    elif PlayerMove == 3:

                        PlayerMoving = False
                        PlayerMove = 0
                            
                    #endif

                #endif
                    
            #endfor

        #endfor

        for node in upHori_list:
            
            UHMove_list = pygame.sprite.spritecollide(node, player_list, False)

            for player in UHMove_list:

                if node.rect.x == player.rect.x and node.rect.y == player.rect.y:

                    if nextMove != [] and PlayerMove != 4:

                        if nextMove[0] == 3 or nextMove[0] == 1 or nextMove[0] == 2:

                            PlayerMove = nextMove[0]
                            PlayerMoving = True

                        #endif

                    elif PlayerMove == 4:

                        PlayerMoving = False
                        PlayerMove = 0
                            
                    #endif

                #endif
                    
            #endfor

        #endfor

        for node in leftVert_list:
            
            LVMove_list = pygame.sprite.spritecollide(node, player_list, False)

            for player in LVMove_list:

                if node.rect.x == player.rect.x and node.rect.y == player.rect.y:

                    if nextMove != [] and PlayerMove != 2:

                        if nextMove[0] == 4 or nextMove[0] == 1 or nextMove[0] == 3:

                            PlayerMove = nextMove[0]
                            PlayerMoving = True

                        #endif

                    elif PlayerMove == 2:

                        PlayerMoving = False
                        PlayerMove = 0
                            
                    #endif

                #endif
                    
            #endfor

        #endfor

        for node in rightVert_list:
            
            RVMove_list = pygame.sprite.spritecollide(node, player_list, False)

            for player in RVMove_list:

                if node.rect.x == player.rect.x and node.rect.y == player.rect.y:

                    if nextMove != [] and PlayerMove != 1:

                        if nextMove[0] == 4 or nextMove[0] == 2 or nextMove[0] == 3:

                            PlayerMove = nextMove[0]
                            PlayerMoving = True

                        #endif

                    else:

                        PlayerMoving = False
                        PlayerMove = 0
                            
                    #endif

                #endif
                    
            #endfor

        #endfor
                
        all_sprites_list.draw(screen)
        # -- flip display to reveal new position of objects
        pygame.display.flip()

        # - The clock ticks over
        clock.tick(180)
#endprocedure

# -- Initialise PyGame
pygame.init()

# -- Manages how fast screen refreshes

clock = pygame.time.Clock()

# -- Blank Screen
size = (510,570)
screen = pygame.display.set_mode(size)

# -- Title of new window/screen
pygame.display.set_caption("Pac Man")
    
### -- Game Loop

menu()

#End While - End of game loop

pygame.quit()
