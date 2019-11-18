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
#Sub class #Class - Template/Blueprint with attributes

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
                if pos>(225,385) and pos<(375,465):
                    game_start = True
                    game()
                #endif
            #endif
        #endfor
        
        screen.fill (BLACK)

        MainText = Text(80,RED,300,280,'Space Invader')

        #Button Code
        pygame.draw.rect(screen,PURPLE, (225, 385, 150, 80))
        buttonText("START", CYAN, 250, 400, 100,  50, size="small")

        pygame.display.flip()

        clock.tick(60)
    #endwhile
#endfunction

def game():
    game_over = False
    score = 0
    RemainNum = 10
    AddNum=1
    live = 3

    block_list = pygame.sprite.Group()

    bullet_list = pygame.sprite.Group()

    all_sprites_list = pygame.sprite.Group()

    #Player
    THEEND = Block(CYAN, 600, 10)
    THEEND.rect.x = 0
    THEEND.rect.y = 600

    player = Player()
    player.rect.x = 290
    all_sprites_list.add(player)
    
    for i in range(10):
        block = Block(CYAN, 20, 15)

        block.rect.x = randint(0,580)
        block.rect.y = randint(-600,-10)

        block_list.add(block)
        all_sprites_list.add(block)
    #endfor
        
    while game_over == False:
    # -- User input and controls
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullet = Bullet()
                    bullet.rect.x = player.rect.x + 10
                    bullet.rect.y = player.rect.y

                    bullet_list.add(bullet)

                    all_sprites_list.add(bullet)
                #endif
            #End If
        #Next event

        screen.fill(BLACK)

        ScoreText = Text(20,RED,52,50,'Score: '+str(score))
        RoundText = Text(20,RED,52,20,'Round: '+str(AddNum))
        RemainText = Text(20,RED,55,80,'Remain: '+str(RemainNum))
        if live > 1:
            LivesText = Text(20,RED,50,110,'Lives: '+str(live))
        else:
            LivesText = Text(20,RED,50,110,'Live: '+str(live))

        player.update()

        block_list.update()
        bullet_list.update()

        EndList_list = pygame.sprite.spritecollide(THEEND, block_list, False)

        live_list = pygame.sprite.spritecollide(player, block_list, False)

        for block in live_list:
            live -= 1
            score += 1
            remain -= 1
            block_list.remove(block)
            all_sprites_list.remove(block)

            if live < 0:
                game_over = True
                finish(score)
                

        for block in EndList_list:
            game_over = True
            finish(score)

        for bullet in bullet_list:

            if bullet.rect.y <= -10:
                bullet_list.remove(bullet)
                all_sprites_list.remove(bullet)

            blocks_hit_list = pygame.sprite.spritecollide(bullet, block_list, False)

            for block in blocks_hit_list:
                bullet_list.remove(bullet)
                block_list.remove(block)
                all_sprites_list.remove(block)  
                all_sprites_list.remove(bullet)
                score += 1
                RemainNum = RemainNum - 1
                if RemainNum == 0:
                    print("New enemy created")
                    AddNum+=1
                    for i in range(10 + AddNum*2):
                        block = Block(CYAN, 20, 15)

                        block.rect.x = randint(0,580)
                        block.rect.y = randint(-900,-10)

                        block_list.add(block)
                        all_sprites_list.add(block)

                    RemainNum = 10 + 2*AddNum

        all_sprites_list.draw(screen)
        # -- flip display to reveal new position of objects
        pygame.display.flip()

        # - The clock ticks over
        clock.tick(60)
#endprocedure

#Menu
def finish(Score):
    Continue = False
    while Continue == False:
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                pygame.quit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if pos>(175,385) and pos<(425,465):
                    Continue = True
                    menu()
            #endif
        #endfor
        
        screen.fill (BLACK)

        MainText = Text(70,RED,300,280,'Congratulations!')
        ScoreText = Text(40,RED,300,340,'Your Score: '+str(Score))

        pygame.draw.rect(screen,PURPLE, (175, 385, 250, 80))
        buttonText("CONTINUE", CYAN, 249, 400, 100,  50, size="small")

        pygame.display.flip()

        clock.tick(60)
    #endwhile
#endfunction
        
def Text(Size,Colour,x,y,text):
    font = pygame.font.Font('freesansbold.ttf',Size)
    text = font.render(text, True, Colour, BLACK) 
    textRect = text.get_rect()
    textRect.center = (x,y)
    screen.blit(text, textRect)
    
class Block(pygame.sprite.Sprite):
    def __init__(self, colour, width, height):
        super().__init__()
        
        self.image = pygame.Surface([width,height])
        self.image.fill(colour)
        self.rect = self.image.get_rect()

        pygame.draw.rect(self.image, colour, [0,0,width,height])     

    def update(self):
 
        self.rect.y += 1

        if self.rect.y > 600:
            self.rect.y = randint(-100, -10)
            self.rect.x = randint(0, 580)

#Player class
class Player(pygame.sprite.Sprite):
 
    def __init__(self):
        super().__init__()
 
        self.image = pygame.Surface([20, 20])
        self.image.fill(NICE)
 
        self.rect = self.image.get_rect()

        self.rect.y = 570
 
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

#Bullet class
class Bullet(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
 
        self.image = pygame.Surface([4, 10])
        self.image.fill(WHITE)
 
        self.rect = self.image.get_rect()
 
    def update(self):
        
        self.rect.y -= 3

# -- Initialise PyGame
pygame.init()

# -- Manages how fast screen refreshes

clock = pygame.time.Clock()

# -- Blank Screen
size = (600,600)
screen = pygame.display.set_mode(size)

# -- Title of new window/screen
pygame.display.set_caption("Sprites")

clock =pygame.time.Clock()
    
### -- Game Loop

menu()

#End While - End of game loop

pygame.quit()
