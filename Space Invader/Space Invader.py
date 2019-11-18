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
RemainNum = 25
AddNum=0
# -- Classes
#Sub class #Class - Template/Blueprint with attributes
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

    def reset_pos(self):
        self.rect.y = randint(-300, -20)
        self.rect.x = randint(0, 580)
        block_list.remove(block)
        all_sprites_list.remove(block)     

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
        pos = pygame.mouse.get_pos()

        self.rect.x = pos[0]

#Bullet class
class Bullet(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
 
        self.image = pygame.Surface([4, 10])
        self.image.fill(WHITE)
 
        self.rect = self.image.get_rect()
 
    def update(self):
        
        self.rect.y -= 3

        if self.rect.y <= -10:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)

# -- Initialise PyGame
pygame.init()

# -- Manages how fast screen refreshes

clock = pygame.time.Clock()

# -- Blank Screen
size = (600,600)
screen = pygame.display.set_mode(size)

# -- Title of new window/screen
pygame.display.set_caption("Sprites")

block_list = pygame.sprite.Group()

bullet_list = pygame.sprite.Group()

all_sprites_list = pygame.sprite.Group()

for i in range(25):
    block = Block(CYAN, 20, 15)

    block.rect.x = randint(0,580)
    block.rect.y = randint(-600,-10)

    block_list.add(block)
    all_sprites_list.add(block)
#endfor

#Player
player = Player()
all_sprites_list.add(player)

game_over = False

clock =pygame.time.Clock()

score = 0
    
### -- Game Loop
while not game_over:
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
        #End If
    #Next event

    screen.fill(BLACK)

    ScoreText = Text(20,RED,50,50,'Score '+str(score))
    RoundText = Text(20,RED,50,20,'Round '+str(AddNum))

    player.update()

    block_list.update()
    bullet_list.update()

    for bullet in bullet_list:

        blocks_hit_list = pygame.sprite.spritecollide(bullet, block_list, False)

        for block in blocks_hit_list:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
            score += 1
            RemainNum = RemainNum - 1
            if RemainNum == 0:
                AddNum+=1
                for i in range(25 + AddNum*10):
                    block = Block(CYAN, 20, 15)

                    block.rect.x = randint(0,580)
                    block.rect.y = randint(-1800,-10)

                    block_list.add(block)
                    all_sprites_list.add(block)

                RemainNum = 25 + 10*AddNum

            block.reset_pos()

    all_sprites_list.draw(screen)
    # -- flip display to reveal new position of objects
    pygame.display.flip()

    # - The clock ticks over
    clock.tick(60)

#End While - End of game loop

pygame.quit()
