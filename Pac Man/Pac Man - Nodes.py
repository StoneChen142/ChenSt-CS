import pygame
import random
# -- Global Constants

f = open("RouteSheet.txt","r+")
lines = f.readlines()
length = len(lines)
print(length)
f.close()

graph = {'a0':{'a1':89,'a6':70},'a1':{'a0':89,'a2':110, 'a7':70},'a2':{'a1':110,'a9':70},'a3':{'a4':110,'b0':70}, 'a4':{'a3':110,'a5':88, 'b2':70},'a5':{'a4':88,'b3':70}, 'a6':{'a0':70,'a7':89, 'b4':51}, 'a7':{'a6':89,'a1':70, 'a8':55, 'b5':51}, 'a8':{'a7':55,'a9':55, 'b6':51}, 'a9':{'a8':55,'a2':70, 'b0':54}, 'b0':{'a9':54,'a3':70, 'b1':53}, 'b1':{'b0':53,'b2':57, 'b9':51}, 'b2':{'b1':57,'a4':70, 'b3':88, 'c0':51},'b3':{'b2':88,'a5':70, 'c1': 51},'b4':{'a6':51,'b5':89},'b5':{'b4':89,'c6':107, 'a7': 51},'b6':{'a8':51,'b7':54},'b7':{'b6':54,'c3':54},'b8':{'b9':53,'c4':54},'b9':{'b1':51,'b8':53},'c0':{'b2':51,'c1':88, 'c9': 107},'c1':{'c0':88,'b3':51},'c2':{'c3':54,'c7':53},'c3':{'c2':54,'c4':55, 'b7': 54}, 'c4':{'c3':55,'c5':54, 'b8': 54},'c5':{'c4':54,'c8':53},'c6':{'c7':55,'b5':107, 'd3': 104}, 'c7':{'c2':53,'c6':55, 'd0': 52}, 'c8':{'c5':53,'c9':56, 'd1': 52},'c9':{'c8':56,'c0':107, 'd8': 104},'d0':{'c7':52,'d4':52, 'd1': 163},'d1':{'c8':52,'d7':52, 'd0': 163},'d2':{'d3':89,'e0':52},'d3':{'d2':89,'c6':104, 'd4': 55, 'e2':52}, 'd4':{'d3':55,'d0':52, 'd5': 54}, 'd5':{'d4':54,'e4':52},'d6':{'e5':52,'d7':53},'d7':{'d6':53,'d1':52, 'd8': 56}, 'd8':{'d7':56,'c9':104, 'd9': 88,'e7':52}, 'd9':{'d8':88,'e9':52}, 'e0':{'d2':52,'e1':35}, 'e1':{'e0':35,'f1':53}, 'e2':{'d3':52,'e3':55, 'f2': 53},'e3':{'e2':55,'f3':53, 'e4': 54},'e4':{'e3':54,'d5':52, 'e5': 56}, 'e5':{'e4':56,'d6':52, 'e6': 52},'e6':{'e5':52,'f6':53, 'e7': 57},'e7':{'e6':57,'d8':52, 'f7': 53}, 'e8':{'e9':35,'f8':53},'e9':{'e8':35,'d9':52}, 'f0':{'f1':35,'g0':53}, 'f1':{'f0':35,'e1':53, 'f2': 54}, 'f2':{'f1':54,'e2':53}, 'f3':{'f4':53,'e3':53}, 'f4':{'f3':53,'g1':53}, 'f5':{'f6':52,'g2':53}, 'f6':{'f5':52,'e6':53}, 'f7':{'e7':53,'f8':53}, 'f8':{'f7':53,'e8':53, 'f9': 35}, 'f9':{'f8':35,'g3':53}, 'g0':{'f0':53,'g1':197}, 'g1':{'g0':197,'g2':57, 'f4':53}, 'g2':{'g1':57,'g3':197, 'f5':53},'g3':{'g2':197,'f9':53}}

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
 
        self.image = pygame.Surface([34, 34])
        self.image = pygame.transform.scale(pygame.image.load('ShadowDown2.png'), (34, 34))
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
        self.image = pygame.image.load("Brick.png").convert()
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        
    #endprocedure

#endclass

class DownRightNode(pygame.sprite.Sprite):
    def __init__(self,width,height):
        super().__init__()
        
        self.image = pygame.Surface([width,height])
        self.image = pygame.image.load("Brick.png").convert()
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        
    #endprocedure

#endclass

class DownVertNode(pygame.sprite.Sprite):
    def __init__(self,width,height):
        super().__init__()
        
        self.image = pygame.Surface([width,height])
        self.image = pygame.image.load("Brick.png").convert()
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        
    #endprocedure

#endclass

class UpVertNode(pygame.sprite.Sprite):
    def __init__(self,width,height):
        super().__init__()
        
        self.image = pygame.Surface([width,height])
        self.image = pygame.image.load("Brick.png").convert()
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        
    #endprocedure

#endclass

class DownLeftNode(pygame.sprite.Sprite):
    def __init__(self,width,height):
        super().__init__()
        
        self.image = pygame.Surface([width,height])
        self.image = pygame.image.load("Brick.png").convert()
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        
    #endprocedure

#endclass

class LeftVertNode(pygame.sprite.Sprite):
    def __init__(self,width,height):
        super().__init__()
        
        self.image = pygame.Surface([width,height])
        self.image = pygame.image.load("Brick.png").convert()
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        
    #endprocedure

#endclass

class RightVertNode(pygame.sprite.Sprite):
    def __init__(self,width,height):
        super().__init__()
        
        self.image = pygame.Surface([width,height])
        self.image = pygame.image.load("Brick.png").convert()
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        
    #endprocedure

#endclass

class UpRightNode(pygame.sprite.Sprite):
    def __init__(self,width,height):
        super().__init__()
        
        self.image = pygame.Surface([width,height])
        self.image = pygame.image.load("Brick.png").convert()
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        
    #endprocedure

#endclass

class UpLeftNode(pygame.sprite.Sprite):
    def __init__(self,width,height):
        super().__init__()
        
        self.image = pygame.Surface([width,height])
        self.image = pygame.image.load("Brick.png").convert()
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        
    #endprocedure

#endclass

class DownHoriNode(pygame.sprite.Sprite):
    def __init__(self,width,height):
        super().__init__()
        
        self.image = pygame.Surface([width,height])
        self.image = pygame.image.load("Brick.png").convert()
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        
    #endprocedure

#endclass

class UpHoriNode(pygame.sprite.Sprite):
    def __init__(self,width,height):
        super().__init__()
        
        self.image = pygame.Surface([width,height])
        self.image = pygame.image.load("Brick.png").convert()
        self.image = pygame.transform.scale(self.image, (width, height))
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
    player.rect.y = 320
    all_sprites_list.add(player)
    player_list.add(player)

    shadow = Shadow()
    shadow.rect.x = 238
    shadow.rect.y = 215
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
            pos = pygame.mouse.get_pos()
            print(pos)
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
