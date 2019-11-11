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

class Ball():
    def __init__(self, colour, n):
        self.n = n
        for i in range(0,self.n-1):
            self.x[i] = randint(10,590)
            self.y[i] = randint(10,590)
            self.speedx[i] = randint(2,4)
            self.speedy[i] = randint(2,4)
            self.colour[i] = colour

    def move(self):
        for i in range(0,self.n-1):
            if self.y[i] == 590 or self.y[i] > 590:
                self.speedy[i] = self.speedy[i]*-1
            elif self.y[i] == 10 or self.y[i] < 10:
                self.speedy[i] = self.speedy[i]*-1
            elif self.x[i] == 10 or self.x[i] < 10:
                self.speedx[i] = self.speedx[i]*-1
            elif self.x[i] == 590 or self.x[i] > 590:
                self.speedx[i] = self.speedx[i]*-1

            self.x[i] += self.speedx[i]
            self.y[i] += self.speedy[i]

    def draw(self):
        for i in range(0,self.n-1):
            pygame.draw.circle(screen, self.colour[i], (self.x[i],self.y[i]),10)

# -- Initialise PyGame
pygame.init()

# -- Manages how fast screen refreshes

clock = pygame.time.Clock()

# -- Blank Screen
size = (600,600)
screen = pygame.display.set_mode(size)

# -- Title of new window/screen
pygame.display.set_caption("My First Flipbook")

game_over = False
ball = Ball(NICE,10)

### -- Game Loop
while not game_over:
    # -- User input and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        #End If
    #Next event

    ball.move()

    screen.fill(BLACK)

    ball.draw()
    
    # -- flip display to reveal new position of objects
    pygame.display.flip()

    # - The clock ticks over
    clock.tick(60)

#End While - End of game loop

pygame.quit()
