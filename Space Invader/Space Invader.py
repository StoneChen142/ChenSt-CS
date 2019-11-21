import pygame
from random import randint
import time
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
#Class - Template/Blueprint with attributes
def createEnemy(row, column,block_list,all_sprites_list):
    for j in range(column):
        if j == 0:
            for i in range(row):
                block = Monster1(1)

                block.rect.x = 158 + 44*i
                block.rect.y = 170

                block_list.add(block)
                all_sprites_list.add(block)
            #endfor
        elif j == 1:
            for i in range(row):
                block = Monster1(1)

                block.rect.x = 158 + 44*i
                block.rect.y = 138

                block_list.add(block)
                all_sprites_list.add(block)
            #endfor
        #endif
        elif j == 2:
            for i in range(row):
                block = Monster2(1)

                block.rect.x = 158 + 44*i
                block.rect.y = 106

                block_list.add(block)
                all_sprites_list.add(block)
            #endfor
        #endif
        elif j == 3:
            for i in range(row):
                block = Monster2(1)

                block.rect.x = 158 + 44*i
                block.rect.y = 74

                block_list.add(block)
                all_sprites_list.add(block)
            #endfor
        #endif
        elif j == 4:
            for i in range(row):
                block = Monster3(1)

                block.rect.x = 163 + 44*i
                block.rect.y = 42

                block_list.add(block)
                all_sprites_list.add(block)
            #endfor 
        #endif
#endprocedure
        
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
                if pos>(325,385) and pos<(475,465):
                    game_start = True
                    game()
                #endif
            #endif
        #endfor
        
        screen.fill (BLACK)

        MainText = Text(80,RED,400,280,'Space Invader')

        #Button Code
        pygame.draw.rect(screen,PURPLE, (325, 385, 150, 80))
        buttonText("START", CYAN, 350, 400, 100,  50, size="small")

        pygame.display.flip()

        clock.tick(60)
    #endwhile
#endprocedure

def game():
    game_over = False
    score = 0
    RemainNum = 40
    AddNum=1
    live = 3
    bulletNum = 8
    direction = 1

    block_list = pygame.sprite.Group()

    bullet_list = pygame.sprite.Group()

    all_sprites_list = pygame.sprite.Group()

    #Player
    THEEND = Block(600, 10)
    THEEND.rect.x = 0
    THEEND.rect.y = 600

    player = Player()
    player.rect.x = 387
    all_sprites_list.add(player)
    
    createEnemy(11,5,block_list, all_sprites_list)
        
    while game_over == False:
    # -- User input and controls
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if bulletNum > 0:
                        bulletNum -= 1
                        bullet = Bullet()
                        bullet.rect.x = player.rect.x + 11
                        bullet.rect.y = player.rect.y

                        bullet_list.add(bullet)

                        all_sprites_list.add(bullet)
                    #endif
                #endif
            #End If
        #Next event

        screen.fill(BLACK)

        ScoreText = Text(20,RED,52,50,'Score: '+str(score))
        RoundText = Text(20,RED,52,20,'Round: '+str(AddNum))
        RemainText = Text(20,RED,55,80,'Enemy: '+str(RemainNum))
        BulletText = Text(20,RED,55,140,'Bullet: '+str(bulletNum))
        if live > 1:
            LivesText = Text(20,RED,50,110,'Lives: '+str(live))
        else:
            LivesText = Text(20,RED,50,110,'Live: '+str(live))
        #endif

        player.update()

        
        block_list.update(direction)
        
        bullet_list.update()

        EndList_list = pygame.sprite.spritecollide(THEEND, block_list, False)

        live_list = pygame.sprite.spritecollide(player, block_list, False)

        for block in live_list:
            live -= 1
            score += 1
            RemainNum -= 1
            block_list.remove(block)
            all_sprites_list.remove(block)

            if live < 0:
                game_over = True
                finish(score)
            elif RemainNum == 0:
                    print("New wave created")
                    AddNum+=1
                    bulletNum += 1
                    RemainNum = 40
                    createEnemy(11,5,block_list, all_sprites_list)
            #endif
        #endfor
                

        for block in EndList_list:
            live -= 1
            score += 1
            RemainNum -= 1
            block_list.remove(block)
            all_sprites_list.remove(block)

            if live < 0:
                game_over = True
                finish(score)
            elif RemainNum == 0:
                    print("New wave created")
                    AddNum+=1
                    bulletNum += 1
                    RemainNum = 40
                    createEnemy(11,5,block_list, all_sprites_list)
            #endif
        #endfor

        for bullet in bullet_list:

            if bullet.rect.y <= -1000:
                bullet_list.remove(bullet)
                all_sprites_list.remove(bullet)
                bulletNum += 1
            #endif

            blocks_hit_list = pygame.sprite.spritecollide(bullet, block_list, False)

            for block in blocks_hit_list:
                bullet_list.remove(bullet) 
                all_sprites_list.remove(bullet)
                block_list.remove(block)
                all_sprites_list.remove(block)
                score += 1
                bulletNum += 1
                RemainNum -= 1
                if RemainNum == 0:
                    print("New wave created")
                    AddNum+=1
                    bulletNum += 1
                    RemainNum = 40
                    createEnemy(11,5,block_list, all_sprites_list)
                #endif
            #endfor
        #endfor

        all_sprites_list.draw(screen)
        # -- flip display to reveal new position of objects
        pygame.display.flip()

        # - The clock ticks over
        clock.tick(60)
#endprocedure

#Finish Screen
def finish(Score):
    Continue = False
    while Continue == False:
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                pygame.quit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if pos>(275,385) and pos<(525,465):
                    Continue = True
                    menu()
                #endif
            #endif
        #endfor
        
        screen.fill (BLACK)

        MainText = Text(70,RED,400,280,'Congratulations!')
        ScoreText = Text(40,RED,400,340,'Your Score: '+str(Score))

        pygame.draw.rect(screen,PURPLE, (275, 385, 250, 80))
        buttonText("CONTINUE", CYAN, 349, 400, 100,  50, size="small")

        pygame.display.flip()

        clock.tick(60)
    #endwhile
#endprocedure
        
def Text(Size,Colour,x,y,text):
    font = pygame.font.Font('freesansbold.ttf',Size)
    text = font.render(text, True, Colour, BLACK) 
    textRect = text.get_rect()
    textRect.center = (x,y)
    screen.blit(text, textRect)
#endprocedure
    
class Block(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()
        
        self.image = pygame.Surface([width,height])
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
    #endprocedure

    def update(self,d):
        self.rect.y += 0.2  

        #endif
    #endprocedure
#endclass

class Monster(pygame.sprite.Sprite):
    def __init__(self,MLives):
        super().__init__()
        
        self.live = MLives
    #endprocedure

    def update(self):
        self.rect.y += 1

        #endif
    #endprocedure
#endclass

class Monster1(Monster):
    def __init__(self,MLives):
        super().__init__(MLives)
        
        self.image = pygame.Surface([34,24])
        self.image = pygame.image.load("SpaceMonster1-1.png").convert()
        self.image = pygame.transform.scale(self.image, (34, 24))
        self.rect = self.image.get_rect()
    #endprocedure

    def update(self,move):
        
        self.rect.y += 1

        #endif
    #endprocedure
#endclass

class Monster2(Monster):
    def __init__(self,MLives):
        super().__init__(MLives)
        
        self.image = pygame.Surface([34,24])
        self.image = pygame.image.load("SpaceMonster3-1.png").convert()
        self.image = pygame.transform.scale(self.image, (34, 24))
        self.rect = self.image.get_rect()
        self.lives = MLives
        
        image1 = pygame.image.load("SpaceMonster3-1.png").convert()
        image1 = pygame.transform.scale(self.image, (34, 24))

        image2 = pygame.image.load("SpaceMonster3-2.png").convert()
        image2 = pygame.transform.scale(self.image, (34, 24))
    #endprocedure

    def update(self,move):

        self.rect.y += 1

        #endif
    #endprocedure

    def lives():
        if self.lives = 0:
            return True
        else:
            self.lives -= 1
#endclass

class Monster3(Monster):
    def __init__(self,MLives):
        super().__init__(MLives)
        
        self.image = pygame.Surface([24,24])
        self.image = pygame.image.load("SpaceMonster2-1.png").convert()
        self.image = pygame.transform.scale(self.image, (24, 24))
        self.rect = self.image.get_rect()
    #endprocedure

    def update(self,move):

        self.rect.y += 1 

        #endif
    #endprocedure
#endclass

#Player class
class Player(pygame.sprite.Sprite):
 
    def __init__(self):
        super().__init__()
 
        self.image = pygame.Surface([26, 16])
        self.image = pygame.image.load("Player.png").convert()
        self.image = pygame.transform.scale(self.image, (26, 16))
        PlayerExplode1 = pygame.image.load("PlayerExplode1.png").convert()
        PlayerExplode2 = pygame.image.load("PlayerExplode2.png").convert()
 
        self.rect = self.image.get_rect()

        self.rect.y = 570
    #endprocedure
 
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rect.x -= 3
        elif keys[pygame.K_d]:
            self.rect.x += 3
        elif keys[pygame.K_LEFT]:
            self.rect.x -= 3
        elif keys[pygame.K_RIGHT]:
            self.rect.x += 3
        #endif
    #endprocedure
#endclass

#Bullet class
class Bullet(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
 
        self.image = pygame.Surface([4, 10])
        self.image.fill(WHITE)
 
        self.rect = self.image.get_rect()
    #endprocedure
 
    def update(self):
        
        self.rect.y -= 3
    #endprocedure
#endclass

# -- Initialise PyGame
pygame.init()

# -- Manages how fast screen refreshes

clock = pygame.time.Clock()

# -- Blank Screen
size = (800,600)
screen = pygame.display.set_mode(size)

# -- Title of new window/screen
pygame.display.set_caption("Space Invader")

clock =pygame.time.Clock()
    
### -- Game Loop

menu()

#End While - End of game loop

pygame.quit()
