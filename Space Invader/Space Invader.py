import pygame
import random
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
def shootBullet(x, y):
    
    mbullet = monsterBullet(x,y)

#endprocedure
    
def createEnemy(row, column,block_list,all_sprites_list):
    for j in range(column):
        if j == 0:
            for i in range(row):
                block = Monster2()

                block.rect.x = 158 + 44*i
                block.rect.y = 266

                block_list.add(block)
                all_sprites_list.add(block)
            #endfor
        elif j == 1:
            for i in range(row):
                block = Monster2()

                block.rect.x = 158 + 44*i
                block.rect.y = 234

                block_list.add(block)
                all_sprites_list.add(block)
            #endfor
        #endif
        elif j == 2:
            for i in range(row):
                block = Monster1()

                block.rect.x = 158 + 44*i
                block.rect.y = 202

                block_list.add(block)
                all_sprites_list.add(block)
            #endfor
        #endif
        elif j == 3:
            for i in range(row):
                block = Monster1()

                block.rect.x = 158 + 44*i
                block.rect.y = 170

                block_list.add(block)
                all_sprites_list.add(block)
            #endfor
        #endif
        elif j == 4:
            for i in range(row):
                block = Monster3()

                block.rect.x = 163 + 44*i
                block.rect.y = 138

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
    RemainNum = 55
    AddNum=1
    live = 3
    bulletNum = 7
    moveCount = 1
    moveTime = 1400
    oldTime = 0
    oldpTime = 0
    olduTime = 0
    
    oldbTime1 = 0
    oldbTime2 = 0
    oldbTime3 = 0
    oldbTime4 = 0
    oldbTime5 = 0

    oldb1Time1 = 0
    oldb1Time2 = 0
    oldb1Time3 = 0
    oldb1Time4 = 0
    oldb1Time5 = 0
    
    p_posx = 0
    p_posy = 0
    i = 0
    pause = False
    UFOSpawned = False

    shoot = 50
    
    oldtime=pygame.time.get_ticks()
    
    explosion_list = pygame.sprite.Group()

    ufoExplosion_list = pygame.sprite.Group()

    barExplosion_list1 = pygame.sprite.Group()
    barExplosion_list2 = pygame.sprite.Group()
    barExplosion_list3 = pygame.sprite.Group()
    barExplosion_list4 = pygame.sprite.Group()
    barExplosion_list5 = pygame.sprite.Group()

    barExplosion1_list1 = pygame.sprite.Group()
    barExplosion1_list2 = pygame.sprite.Group()
    barExplosion1_list3 = pygame.sprite.Group()
    barExplosion1_list4 = pygame.sprite.Group()
    barExplosion1_list5 = pygame.sprite.Group()

    block_list = pygame.sprite.Group()

    bullet_list = pygame.sprite.Group()

    mbullet_list = pygame.sprite.Group()

    all_sprites_list = pygame.sprite.Group()

    player_list = pygame.sprite.Group()

    ufo_list = pygame.sprite.Group()

    barricade1_list = pygame.sprite.Group()
    barricade2_list = pygame.sprite.Group()
    barricade3_list = pygame.sprite.Group()
    barricade4_list = pygame.sprite.Group()
    barricade5_list = pygame.sprite.Group()

    #Player
    THEEND = Block(600, 10)
    THEEND.rect.x = 0
    THEEND.rect.y = 600

    player = Player()
    player.rect.x = 381
    all_sprites_list.add(player)
    player_list.add(player)

    live1 = PlayerLive()
    live1.rect.y = 14
    live1.rect.x = 640
    all_sprites_list.add(live1)

    live2 = PlayerLive()
    live2.rect.y = 14
    live2.rect.x = 689
    all_sprites_list.add(live2)

    live3 = PlayerLive()
    live3.rect.y = 14
    live3.rect.x = 738
    all_sprites_list.add(live3)

    ufo = UFO()
    
    all_sprites_list.add(ufo)
    ufo_list.add(ufo)
    
    createEnemy(11,5,block_list, all_sprites_list)

    barricade1 = Barricade()
    barricade1.rect.x = 115
    barricade1.rect.y = 450
    all_sprites_list.add(barricade1)
    barricade1_list.add(barricade1)
    bar1HP = 10

    barricade2 = Barricade()
    barricade2.rect.x = 237
    barricade2.rect.y = 450
    all_sprites_list.add(barricade2)
    barricade2_list.add(barricade2)
    bar2HP = 10

    barricade3 = Barricade()
    barricade3.rect.x = 359
    barricade3.rect.y = 450
    all_sprites_list.add(barricade3)
    barricade3_list.add(barricade3)
    bar3HP = 10

    barricade4 = Barricade()
    barricade4.rect.x = 481
    barricade4.rect.y = 450
    all_sprites_list.add(barricade4)
    barricade4_list.add(barricade4)
    bar4HP = 10

    barricade5 = Barricade()
    barricade5.rect.x = 603
    barricade5.rect.y = 450
    all_sprites_list.add(barricade5)
    barricade5_list.add(barricade5)
    bar5HP = 10
        
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
                        bullet.rect.x = player.rect.x + 18.8
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
        BulletText = Text(20,RED,51,80,'Bullet: '+str(bulletNum))

        if pause == False:

            if UFOSpawned == True:
                ufo.update()
                if ufo.rect.x < -100:
                    UFOSpawned = False
                    ufo.rect.x = 900
            else:
                Surprise = random.randint(0,750)
                if Surprise == 0:
                    UFOSpawned = True
            
            player.update()

            newtime=pygame.time.get_ticks()

            #Update Enemies
            if newtime - oldtime > moveTime: #in milliseconds 

                block_list.update(moveCount)
                moveCount += 1
                moveTime -= 7
                oldtime=newtime

                selected_enemy = random.choice(block_list.sprites())
                Class = str(selected_enemy.__class__.__name__)
                if Class == "Monster1" or Class == "Monster2":
                    mbullet = monsterBullet(selected_enemy.rect.x + 12, selected_enemy.rect.y - 24)
                elif Class == "Monster3":
                    mbullet = monsterBullet(selected_enemy.rect.x + 7, selected_enemy.rect.y - 24)
                #endif
                mbullet_list.add(mbullet)
                all_sprites_list.add(mbullet)
                      
            #endif
            
            bullet_list.update()

            mbullet_list.update()

        #endif

        if bar1HP == 0:
            all_sprites_list.remove(barricade1)
            barricade1_list.remove(barricade1)
        elif bar2HP == 0:
            all_sprites_list.remove(barricade2)
            barricade2_list.remove(barricade2)
        elif bar3HP == 0:
            all_sprites_list.remove(barricade3)
            barricade3_list.remove(barricade3)
        elif bar4HP == 0:
            all_sprites_list.remove(barricade4)
            barricade4_list.remove(barricade4)
        elif bar5HP == 0:
            all_sprites_list.remove(barricade5)
            barricade5_list.remove(barricade5)
            
        EndList_list = pygame.sprite.spritecollide(THEEND, block_list, False)

        live_list = pygame.sprite.spritecollide(player, block_list, False)

        for block in live_list:
            game_over = True
            finish(score)
            #endif
        #endfor    

        for block in EndList_list:
            game_over = True
            finish(score)
        #endfor

        #Update Bullet
        for bullet in bullet_list:

            if bullet.rect.y <= -1000:
                bullet_list.remove(bullet)
                all_sprites_list.remove(bullet)
                bulletNum += 1
            #endif

            blocks_hit_list = pygame.sprite.spritecollide(bullet, block_list, False)

            #Erase Block
            for block in blocks_hit_list:
                
                bullet_list.remove(bullet) 
                all_sprites_list.remove(bullet)
                
                block_list.remove(block)
                all_sprites_list.remove(block)

                shoot -= 1
 
                Class = str(block.__class__.__name__)
                if Class == "Monster1" or Class == "Monster2":
                    explosionExample = Explosion(1, block.rect.x, block.rect.y)
                elif Class == "Monster3":
                    explosionExample = Explosion(2, block.rect.x, block.rect.y)
                oldTime=pygame.time.get_ticks()
                explosion_list.add(explosionExample)
                all_sprites_list.add(explosionExample)
                score = block.addScore(score)
                bulletNum += 1
                RemainNum -= 1         
                if RemainNum == 0:
                    AddNum+=1
                    bulletNum += 1
                    RemainNum = 55
                    createEnemy(11,5,block_list, all_sprites_list)
                    moveTime = 3000 - (AddNum - 1)*100
                    moveCount = 1
                #endif
            #endfor

            #Bullet hit UFO
            ufo_hit_list = pygame.sprite.spritecollide(bullet, ufo_list, False)

            #Reset UFO
            for ufo in ufo_hit_list:
                
                bullet_list.remove(bullet) 
                all_sprites_list.remove(bullet)

                UFOSpawned = False

                score += (300 + (random.randint(0,10))*10)
 
                ufoExplosionExample = ufoExplosion(ufo.rect.x, ufo.rect.y)
                ufo.rect.x = 900
                olduTime = pygame.time.get_ticks()
                ufoExplosion_list.add(ufoExplosionExample)
                all_sprites_list.add(ufoExplosionExample)
                bulletNum += 1
                
            #endfor

            #Bullet hit Barricade
            bar_hit_list1 = pygame.sprite.spritecollide(bullet, barricade1_list, False)
            bar_hit_list2 = pygame.sprite.spritecollide(bullet, barricade2_list, False)
            bar_hit_list3 = pygame.sprite.spritecollide(bullet, barricade3_list, False)
            bar_hit_list4 = pygame.sprite.spritecollide(bullet, barricade4_list, False)
            bar_hit_list5 = pygame.sprite.spritecollide(bullet, barricade5_list, False)
            #Barriacde reduce hp
            for barricade1 in bar_hit_list1:
                
                bullet_list.remove(bullet) 
                all_sprites_list.remove(bullet)

                bar1HP -= 1
 
                explosionExample = Explosion(3, bullet.rect.x, bullet.rect.y)
                oldbTime1 = pygame.time.get_ticks()
                barExplosion_list1.add(explosionExample)
                all_sprites_list.add(explosionExample)
                bulletNum += 1
                
            #endfor

            for barricade2 in bar_hit_list2:
                
                bullet_list.remove(bullet) 
                all_sprites_list.remove(bullet)

                bar2HP -= 1
 
                explosionExample = Explosion(3, bullet.rect.x, bullet.rect.y)
                oldbTime2 = pygame.time.get_ticks()
                barExplosion_list2.add(explosionExample)
                all_sprites_list.add(explosionExample)
                bulletNum += 1
                
            #endfor

            for barricade3 in bar_hit_list3:
                
                bullet_list.remove(bullet) 
                all_sprites_list.remove(bullet)

                bar3HP -= 1
 
                explosionExample = Explosion(3, bullet.rect.x, bullet.rect.y)
                oldbTime3 = pygame.time.get_ticks()
                barExplosion_list3.add(explosionExample)
                all_sprites_list.add(explosionExample)
                bulletNum += 1

            #endfor

            for barricade4 in bar_hit_list4:
                
                bullet_list.remove(bullet) 
                all_sprites_list.remove(bullet)

                bar4HP -= 1
 
                explosionExample = Explosion(3, bullet.rect.x, bullet.rect.y)
                oldbTime4 = pygame.time.get_ticks()
                barExplosion_list4.add(explosionExample)
                all_sprites_list.add(explosionExample)
                bulletNum += 1
                
            #endfor

            for barricade5 in bar_hit_list5:
                
                bullet_list.remove(bullet) 
                all_sprites_list.remove(bullet)

                bar5HP -= 1
 
                explosionExample = Explosion(3, bullet.rect.x, bullet.rect.y)
                oldbTime5 = pygame.time.get_ticks()
                barExplosion_list5.add(explosionExample)
                all_sprites_list.add(explosionExample)
                bulletNum += 1
                
            #endfor

        #endfor

        #Update Monster Bullet
        for mbullet in mbullet_list:

            if mbullet.rect.y > 650:
                mbullet_list.remove(mbullet)
                all_sprites_list.remove(mbullet)
            #endif
        #endfor

            #Bullet hit Barricade
            bar1_hit_list1 = pygame.sprite.spritecollide(mbullet, barricade1_list, False)
            bar1_hit_list2 = pygame.sprite.spritecollide(mbullet, barricade2_list, False)
            bar1_hit_list3 = pygame.sprite.spritecollide(mbullet, barricade3_list, False)
            bar1_hit_list4 = pygame.sprite.spritecollide(mbullet, barricade4_list, False)
            bar1_hit_list5 = pygame.sprite.spritecollide(mbullet, barricade5_list, False)
            #Barriacde reduce hp
            for barricade1 in bar1_hit_list1:
                
                mbullet_list.remove(mbullet) 
                all_sprites_list.remove(mbullet)

                bar1HP -= 1
 
                explosionExample = Explosion(3, mbullet.rect.x, mbullet.rect.y)
                oldb1Time1 = pygame.time.get_ticks()
                barExplosion1_list1.add(explosionExample)
                all_sprites_list.add(explosionExample)
                
            #endfor

            for barricade2 in bar1_hit_list2:
                
                mbullet_list.remove(mbullet) 
                all_sprites_list.remove(mbullet)

                bar2HP -= 1
 
                explosionExample = Explosion(3, mbullet.rect.x, mbullet.rect.y)
                oldb1Time2 = pygame.time.get_ticks()
                barExplosion1_list2.add(explosionExample)
                all_sprites_list.add(explosionExample)
                
            #endfor

            for barricade3 in bar1_hit_list3:
                
                mbullet_list.remove(mbullet) 
                all_sprites_list.remove(mbullet)

                bar3HP -= 1
 
                explosionExample = Explosion(3, mbullet.rect.x, mbullet.rect.y)
                oldb1Time3 = pygame.time.get_ticks()
                barExplosion1_list3.add(explosionExample)
                all_sprites_list.add(explosionExample)

            #endfor

            for barricade4 in bar1_hit_list4:
                
                mbullet_list.remove(mbullet) 
                all_sprites_list.remove(mbullet)

                bar4HP -= 1
 
                explosionExample = Explosion(3, mbullet.rect.x, mbullet.rect.y)
                oldb1Time4 = pygame.time.get_ticks()
                barExplosion1_list4.add(explosionExample)
                all_sprites_list.add(explosionExample)
                
            #endfor

            for barricade5 in bar1_hit_list5:
                
                mbullet_list.remove(mbullet) 
                all_sprites_list.remove(mbullet)

                bar5HP -= 1
 
                explosionExample = Explosion(3, mbullet.rect.x, mbullet.rect.y)
                oldb1Time5 = pygame.time.get_ticks()
                barExplosion1_list5.add(explosionExample)
                all_sprites_list.add(explosionExample)
                
            #endfor

        player_gethit_list = pygame.sprite.spritecollide(player, mbullet_list, False)

        #Reduce player hp
        for mbullet in player_gethit_list:
                
            mbullet_list.remove(mbullet) 
            all_sprites_list.remove(mbullet)
                
            live -= 1

            if live == 2:
                all_sprites_list.remove(live3)
            elif live == 1:
                all_sprites_list.remove(live2)
            elif live == 0:
                all_sprites_list.remove(live1)

            #player explosion
            oldpTime = pygame.time.get_ticks()
            i = 0
            player.toggle(0,0)
            pause = True
            p_posx = player.rect.x
            p_posy = player.rect.y
            player.rect.x -= 4.5
            player.rect.y -= 1.5
            player.explosion1()
        #endfor

        #Explosion
        for explosionExample in explosion_list:
            newTime=pygame.time.get_ticks()
            if newTime - oldTime > 160:
                all_sprites_list.remove(explosionExample)
                explosion_list.remove(explosionExample)
            #endif
        #endfor
        
        for ufoExplosionExample in ufoExplosion_list:
            newuTime=pygame.time.get_ticks()
            if newuTime - olduTime > 500:
                all_sprites_list.remove(ufoExplosionExample)
                ufoExplosion_list.remove(ufoExplosionExample)
            #endif
        #endfor


        #Barricade Explosion
        for explosionExample in barExplosion_list1:
            newbTime1=pygame.time.get_ticks()
            if newbTime1 - oldbTime1 > 170:
                all_sprites_list.remove(explosionExample)
                barExplosion_list1.remove(explosionExample)
            #endif
        #endfor

        for explosionExample in barExplosion_list2:
            newbTime2=pygame.time.get_ticks()
            if newbTime2 - oldbTime2 > 170:
                all_sprites_list.remove(explosionExample)
                barExplosion_list2.remove(explosionExample)
            #endif
        #endfor

        for explosionExample in barExplosion_list3:
            newbTime3=pygame.time.get_ticks()
            if newbTime3 - oldbTime3 > 170:
                all_sprites_list.remove(explosionExample)
                barExplosion_list3.remove(explosionExample)
            #endif
        #endfor

        for explosionExample in barExplosion_list4:
            newbTime4=pygame.time.get_ticks()
            if newbTime4 - oldbTime4 > 170:
                all_sprites_list.remove(explosionExample)
                barExplosion_list4.remove(explosionExample)
            #endif
        #endfor

        for explosionExample in barExplosion_list5:
            newbTime5=pygame.time.get_ticks()
            if newbTime5 - oldbTime5 > 170:
                all_sprites_list.remove(explosionExample)
                barExplosion_list5.remove(explosionExample)
            #endif
        #endfor

        #Mbullet
        for explosionExample in barExplosion1_list1:
            newb1Time1=pygame.time.get_ticks()
            if newb1Time1 - oldb1Time1 > 170:
                all_sprites_list.remove(explosionExample)
                barExplosion1_list1.remove(explosionExample)
            #endif
        #endfor

        for explosionExample in barExplosion1_list2:
            newb1Time2=pygame.time.get_ticks()
            if newb1Time2 - oldb1Time2 > 170:
                all_sprites_list.remove(explosionExample)
                barExplosion1_list2.remove(explosionExample)
            #endif
        #endfor

        for explosionExample in barExplosion1_list3:
            newb1Time3=pygame.time.get_ticks()
            if newb1Time3 - oldb1Time3 > 170:
                all_sprites_list.remove(explosionExample)
                barExplosion1_list3.remove(explosionExample)
            #endif
        #endfor

        for explosionExample in barExplosion1_list4:
            newb1Time4=pygame.time.get_ticks()
            if newb1Time4 - oldb1Time4 > 170:
                all_sprites_list.remove(explosionExample)
                barExplosion1_list4.remove(explosionExample)
            #endif
        #endfor

        for explosionExample in barExplosion1_list5:
            newb1Time5=pygame.time.get_ticks()
            if newb1Time5 - oldb1Time5 > 170:
                all_sprites_list.remove(explosionExample)
                barExplosion1_list5.remove(explosionExample)
            #endif
        #endfor

        #Player Explosion
        if pause == True:
            newpTime = pygame.time.get_ticks()
            if newpTime - oldpTime > 600 and i == 0:
                oldpTime = newpTime
                player.explosion2()
                i += 1
            elif newpTime - oldpTime > 600 and i == 1:
                oldpTime = newpTime
                player.explosion1()
                i += 1
            elif newpTime - oldpTime > 600 and i == 2:
                oldpTime = newpTime
                player.explosion2()
                i += 1
            elif newpTime - oldpTime > 600 and i == 3:
                oldpTime = newpTime
                player.explosion1()
                i += 1
            elif i == 4:    
                explosion_list.remove(player)
                pause = False
                player.toggle(p_posx, p_posy)
                if live == 0:
                    game_over = True
                    finish(score)
            #endif
        #endif

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
    def __init__(self):
        super().__init__()
        
    #endprocedure
#endclass

class Monster1(Monster):
    def __init__(self):
        super().__init__()
        
        self.image = pygame.Surface([34,24])
        self.image = pygame.image.load("SpaceMonster1-1.png").convert()
        self.image = pygame.transform.scale(self.image, (34, 24))
        self.rect = self.image.get_rect()
        self.numImage = 1

    #endprocedure

    def update(self,move):

        if move < 4 or move > 11 and move < 18 or move > 25 and move < 32 or move > 39 and move < 46 or move > 53 and move < 60 or move > 67 and move < 74 or move > 81 and move < 88:
            self.rect.x += 44
        elif (move - 4)%7 == 0 or move == 4:
            self.rect.y += 32
        elif move > 4 and move < 11 or move > 18 and move < 25 or move > 32 and move < 39 or move > 46 and move < 53 or move > 60 and move < 67 or move > 74 and move < 81 or move > 88 and move < 95:
            self.rect.x -= 44
        #endif
            
        if self.numImage == 1:
            self.image = pygame.image.load("SpaceMonster1-2.png").convert()
            self.image = pygame.transform.scale(self.image, (34, 24))
            self.numImage = 2
        elif self.numImage == 2:
            self.image = pygame.image.load("SpaceMonster1-1.png").convert()
            self.image = pygame.transform.scale(self.image, (34, 24))
            self.numImage = 1

        #endif
            
    #endprocedure

    def addScore(self,score):

        score += 20

        return score

    #endfunction
        
#endclass

class Monster2(Monster):
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface([34,24])
        self.image = pygame.image.load("SpaceMonster3-1.png").convert()
        self.image = pygame.transform.scale(self.image, (34, 24))
        self.rect = self.image.get_rect()
        self.numImage = 1
        
    #endprocedure

    def update(self,move):

        if move < 4 or move > 11 and move < 18 or move > 25 and move < 32 or move > 39 and move < 46 or move > 53 and move < 60 or move > 67 and move < 74 or move > 81 and move < 88:
            self.rect.x += 44
        elif (move - 4)%7 == 0 or move == 4:
            self.rect.y += 32
        elif move > 4 and move < 11 or move > 18 and move < 25 or move > 32 and move < 39 or move > 46 and move < 53 or move > 60 and move < 67 or move > 74 and move < 81 or move > 88 and move < 95:
            self.rect.x -= 44
        #endif
            
        if self.numImage == 1:
            self.image = pygame.image.load("SpaceMonster3-2.png").convert()
            self.image = pygame.transform.scale(self.image, (34, 24))
            self.numImage = 2
        elif self.numImage == 2:
            self.image = pygame.image.load("SpaceMonster3-1.png").convert()
            self.image = pygame.transform.scale(self.image, (34, 24))
            self.numImage = 1
        #endif

    #endprocedure

    def addScore(self,score):

        score += 10

        return score

    #endfunction

#endclass

class Monster3(Monster):
    def __init__(self):
        super().__init__()
        
        self.image = pygame.Surface([24,24])
        self.image = pygame.image.load("SpaceMonster2-1.png").convert()
        self.image = pygame.transform.scale(self.image, (24, 24))
        self.rect = self.image.get_rect()
        self.numImage = 1

    #endprocedure

    def update(self,move):

        if move < 4 or move > 11 and move < 18 or move > 25 and move < 32 or move > 39 and move < 46 or move > 53 and move < 60 or move > 67 and move < 74 or move > 81 and move < 88:
            self.rect.x += 44
        elif (move - 4)%7 == 0 or move == 4:
            self.rect.y += 32
        elif move > 4 and move < 11 or move > 18 and move < 25 or move > 32 and move < 39 or move > 46 and move < 53 or move > 60 and move < 67 or move > 74 and move < 81 or move > 88 and move < 95:
            self.rect.x -= 44
        #endif
            
        if self.numImage == 1:
            self.image = pygame.image.load("SpaceMonster2-2.png").convert()
            self.image = pygame.transform.scale(self.image, (24, 24))
            self.numImage = 2
        elif self.numImage == 2:
            self.image = pygame.image.load("SpaceMonster2-1.png").convert()
            self.image = pygame.transform.scale(self.image, (24, 24))
            self.numImage = 1

        #endif
        
    #endprocedure

    def addScore(self,score):

        score += 40

        return score

    #endfunction
        
#endclass

class PlayerLive(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = pygame.Surface([39, 21])
        self.image = pygame.image.load("Player.png").convert()
        self.image = pygame.transform.scale(self.image, (39, 21))
        self.rect = self.image.get_rect()

    #endprocedure

#endclass

class Explosion(pygame.sprite.Sprite):

    def __init__(self, ExType, x, y):
        super().__init__()

        self.image = pygame.Surface([39, 24])
        self.image = pygame.image.load("MonsterExplode.png").convert()
        self.image = pygame.transform.scale(self.image, (39, 24))
        self.rect = self.image.get_rect()

        if ExType == 1:
            self.rect.x = x - 2
            self.rect.y = y

        elif ExType == 2:
            
            self.rect.x = x - 7
            self.rect.y = y

        elif ExType == 3:

            self.rect.x = x - 17
            self.rect.y = y - 9

    #endprocedure

class ufoExplosion(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.Surface([63, 24])
        self.image = pygame.image.load("UFOExplode.png").convert()
        self.image = pygame.transform.scale(self.image, (63, 24))
        self.rect = self.image.get_rect()

        self.rect.x = x - 12
        self.rect.y = y - 3

    #endprocedure
#endclass

#Player class
class Player(pygame.sprite.Sprite):
 
    def __init__(self):
        super().__init__()
 
        self.image = pygame.Surface([39, 21])
        self.image = pygame.image.load("Player.png").convert()
        self.image = pygame.transform.scale(self.image, (39, 21))
         
        self.rect = self.image.get_rect()

        self.rect.y = 565

        self.activated = True
    #endprocedure
 
    def update(self):

        if self.activated == True:
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

    def explosion1(self):

        self.image = pygame.image.load("PlayerExplode1.png").convert()
        self.image = pygame.transform.scale(self.image, (48, 24))

    #endprocedure

    def explosion2(self):

        self.image = pygame.image.load("PlayerExplode2.png").convert()
        self.image = pygame.transform.scale(self.image, (48, 24))

    #endprocedure

    def toggle(self, x, y):

        if self.activated == True:
            self.activated = False
        else:
            self.activated = True
            self.image = pygame.image.load("Player.png").convert()
            self.image = pygame.transform.scale(self.image, (39, 21))
            self.rect.x = x
            self.rect.y = y

    #endprocedure
    
#endclass

#UFO class
class UFO(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
 
        self.image = pygame.Surface([48, 21])
        self.image = pygame.image.load("UFO.png").convert()
        self.image = pygame.transform.scale(self.image, (48, 21))
        self.rect = self.image.get_rect()

        self.rect.x = 900
        self.rect.y = 102
        
    #endprocedure
 
    def update(self):
        
        self.rect.x -= 3
        
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
        
        self.rect.y -= 5
    #endprocedure
#endclass

class monsterBullet(pygame.sprite.Sprite):

    def __init__(self,x,y):
        super().__init__()
 
        self.image = pygame.Surface([9, 21])
        self.image = pygame.image.load("MonsterBullet.png").convert()
        self.image = pygame.transform.scale(self.image, (9, 21))
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y
        
    #endprocedure
 
    def update(self):
        
        self.rect.y += 5
        
    #endprocedure
        
#endclass

#Barricader
class Barricade(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
 
        self.image = pygame.Surface([72, 48])
        self.image = pygame.image.load("Barricade.png").convert()
        self.image = pygame.transform.scale(self.image, (72, 48))
        self.rect = self.image.get_rect()
        
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
