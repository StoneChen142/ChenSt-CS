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
        self.image.fill(BLACK)
 
        self.rect = self.image.get_rect()
 
    def update(self):
        
        self.rect.y -= 3
#Sub class #Class - Template/Blueprint with attributes
# -- Initialise PyGame
pygame.init()

# -- Manages how fast screen refreshes

clock = pygame.time.Clock()

# -- Blank Screen
size = (600,600)
screen = pygame.display.set_mode(size)

# -- Title of new window/screen
pygame.display.set_caption("Space Invader")

clock =pygame.time.Clock()

game_over = False

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
            #endif
        #End If
    #Next event

    screen.fill(WHITE)

    player.update()

    block_list.update()
    bullet_list.update()

    EndList_list = pygame.sprite.spritecollide(THEEND, block_list, False)             

    for block in EndList_list:
        game_over = True
        pygame.quit()

    for bullet in bullet_list:

        if bullet.rect.y <= -1000:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)

        blocks_hit_list = pygame.sprite.spritecollide(bullet, block_list, False)

        for block in blocks_hit_list:
            bullet_list.remove(bullet)
            block_list.remove(block)
            all_sprites_list.remove(block)  
            all_sprites_list.remove(bullet)
    
    all_sprites_list.draw(screen)
    # -- flip display to reveal new position of objects
    pygame.display.flip()

    # - The clock ticks over
    clock.tick(60)
#endprocedure

    
### -- Game Loop

#End While - End of game loop

pygame.quit()
