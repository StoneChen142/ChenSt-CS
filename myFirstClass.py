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
    def __init__(self, colour):
        self.x = randint(10,590)
        self.y = randint(10,590)
        self.speedx = randint(2,4)
        self.speedy = randint(2,4)
        self.colour = colour

    def move(self):
        if self.y == 590 or self.y > 590:
            self.speedy = self.speedy*-1
        elif self.y == 10 or self.y < 10:
            self.speedy = self.speedy*-1
        elif self.x == 10 or self.x < 10:
            self.speedx = self.speedx*-1
        elif self.x == 590 or self.x > 590:
            self.speedx = self.speedx*-1

        self.x += self.speedx
        self.y += self.speedy

    def draw(self):
        pygame.draw.circle(screen, self.colour, (self.x,self.y),10)

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
ball = Ball(RED)
ball2 = Ball(BLUE)
ball3 = Ball(WHITE)
ball4 = Ball(YELLOW)
ball5 = Ball(WHITE)
ball6 = Ball(GREEN)
ball7 = Ball(ORANGE)
ball8 = Ball(PURPLE)
ball9 = Ball(DGREEN)
ball10 = Ball(PINK)
ball11 = Ball(CYAN)
ball12 = Ball(NICE)

### -- Game Loop
while not game_over:
    # -- User input and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        #End If
    #Next event

    ball.move()
    ball2.move()
    ball3.move()
    ball4.move()
    ball5.move()
    ball6.move()
    ball7.move()
    ball8.move()
    ball9.move()
    ball10.move()
    ball11.move()
    ball12.move()


    screen.fill(BLACK)

    ball.draw()
    ball2.draw()
    ball3.draw()
    ball4.draw()
    ball5.draw()
    ball6.draw()
    ball7.draw()
    ball8.draw()
    ball9.draw()
    ball10.draw()
    ball11.draw()
    ball12.draw()

    
    # -- flip display to reveal new position of objects
    pygame.display.flip()

    # - The clock ticks over
    clock.tick(60)

#End While - End of game loop

pygame.quit()
