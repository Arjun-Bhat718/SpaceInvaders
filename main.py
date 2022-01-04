import math
import random
from space_craft import SpaceCraft
import pygame
from pygame import mixer
from alien_craft import AlienCraft
from bullet import Bullet
from consts import *
import random
from bomb import Bomb
import sys


pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invader")
icon = pygame.image.load(
    r"Space Invaders\ufo.png")
pygame.display.set_icon(icon)
mainMenu = True

while mainMenu:
    mousePos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            if mousePos[0] >= 250 and mousePos[0] <= 500 and mousePos[1] >= 260 and mousePos[1] <= 320:
                mainMenu = False
            elif mousePos[0] >= 250 and mousePos[0] <= 500 and mousePos[1] >= 375 and mousePos[1] <= 435:
                print('options')
            elif mousePos[0] >= 250 and mousePos[0] <= 500 and mousePos[1] >= 495 and mousePos[1] <= 555:
                pygame.quit()
                sys.exit()

    menu = pygame.image.load(
        r'Space Invaders\mainMenu.png')
    screen.blit(menu, (0, 0))
    pygame.display.update()


alienBombList = [1, 2, 3, 4, 5, 6]

background = pygame.image.load(
    r'Space Invaders\background.png')
lifeLeft = 50


backgroundSound = mixer.Sound(
    r'Space Invaders\background.wav')
backgroundSound.play(-1)

bomb = Bomb()
bomb_sprite = pygame.sprite.Group()
bomb_sprite.add(bomb)
playerImg = SpaceCraft()
player_sprite = pygame.sprite.Group()
player_sprite.add(playerImg)
alienImg1 = AlienCraft()
alienImg2 = AlienCraft()
alienImg3 = AlienCraft()
alienImg4 = AlienCraft()
alienImg5 = AlienCraft()
alienImg6 = AlienCraft()
bullet = Bullet()
alienImg2.changeCd(200, 100)
alienImg3.changeCd(300, 100)
alienImg4.changeCd(100, 200)
alienImg5.changeCd(200, 200)
alienImg6.changeCd(300, 200)
alien_sprites = pygame.sprite.Group()
alien_sprites.add(alienImg3)
alien_sprites.add(alienImg2)
alien_sprites.add(alienImg1)
alien_sprites.add(alienImg4)
alien_sprites.add(alienImg5)
alien_sprites.add(alienImg6)
bullet_sprite = pygame.sprite.Group()
bullet_sprite.add(bullet)
all_sprites = pygame.sprite.Group()
all_sprites.add(bullet)
all_sprites.add(playerImg)
all_sprites.add(alienImg1)
all_sprites.add(alienImg2)
all_sprites.add(alienImg3)
all_sprites.add(alienImg4)
all_sprites.add(alienImg5)
all_sprites.add(alienImg6)
all_sprites.add(bomb)
playerX = 370
playerY = 480
playerX_change = 0


score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
testY = 10


over_font = pygame.font.Font('freesansbold.ttf', 64)


def pause():
    mixer.stop()
    pause = True
    screen.fill(WHITE)
    pauseMenu = pygame.image.load(
        r'Space Invaders\pauseMenu.png')
    screen.blit(pauseMenu, (0, 0))

    while pause:
        mousePos = pygame.mouse.get_pos()
        print(mousePos)
        mousePos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pause = False
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                if mousePos[0] >= 250 and mousePos[0] <= 500 and mousePos[1] >= 290 and mousePos[1] <= 355:
                    pause = False
                elif mousePos[0] >= 250 and mousePos[0] <= 500 and mousePos[1] >= 420 and mousePos[1] <= 490:
                    sys.exit()

        pygame.display.update()
    backgroundSound.play(-1)


def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def game_over_text():
    over_text = over_font.render("GAME OVER", True, RED)
    screen.blit(over_text, (200, 250))


def game_win_text():
    over_text = over_font.render("YOU WON!!!", True, GREEN)
    screen.blit(over_text, (200, 250))


alienRight = False
alienLeft = False

running = True
fired = False
i = 0
win = False
bombFire = False
n = 0
gameOver = False
while running:

    i += 1
    mousePos = pygame.mouse.get_pos()

    if n == 4:
        gameOver = True
        break
    if i % 150 == 0:
        bomber = random.choice(alienBombList)

        if bomber == 1:
            bomb.rect.y = alienImg6.rect.y
            bomb.rect.x = alienImg1.rect.x
            bombFire = True
            bombSound = mixer.Sound(
                r'Space Invaders\Shotgun_Blast-Jim_Rogers-1914772763.wav')
            bombSound.play()
            print('fire')
        elif bomber == 2:
            bomb.rect.y = alienImg6.rect.y
            bomb.rect.x = alienImg2.rect.x
            bombFire = True
            bombSound = mixer.Sound(
                r'Space Invaders\Shotgun_Blast-Jim_Rogers-1914772763.wav')
            bombSound.play()
            print('fire')
        elif bomber == 3:
            bomb.rect.y = alienImg6.rect.y
            bomb.rect.x = alienImg3.rect.x
            bombFire = True
            bombSound = mixer.Sound(
                r'Space Invaders\Shotgun_Blast-Jim_Rogers-1914772763.wav')
            bombSound.play()
            print('fire')
        elif bomber == 4:
            bomb.rect.y = alienImg6.rect.y
            bomb.rect.x = alienImg4.rect.x
            bombFire = True
            bombSound = mixer.Sound(
                r'Space Invaders\Shotgun_Blast-Jim_Rogers-1914772763.wav')
            bombSound.play()
            print('fire')
        elif bomber == 5:
            bomb.rect.y = alienImg6.rect.y
            bomb.rect.x = alienImg5.rect.x
            bombFire = True
            bombSound = mixer.Sound(
                r'Space Invaders\Shotgun_Blast-Jim_Rogers-1914772763.wav')
            bombSound.play()
            print('fire')
        elif bomber == 6:
            bomb.rect.y = alienImg6.rect.y
            bomb.rect.x = alienImg6.rect.x
            bombFire = True
            bombSound = mixer.Sound(
                r'Space Invaders\Shotgun_Blast-Jim_Rogers-1914772763.wav')
            bombSound.play()
            print('fire')
    if bombFire == True:
        bomb.rect.y += 7
    if len(alien_sprites) == 0:
        win = True
        backgroundSound.fadeout(500)
        break
    if pygame.sprite.spritecollide(bullet, alien_sprites, True):
        score_value += 1
    if pygame.sprite.spritecollide(alienImg1, bullet_sprite, True):
        bullet.rect.x = -100
        bullet.rect.y = 700
        all_sprites.add(bullet)

    if pygame.sprite.spritecollide(alienImg2, bullet_sprite, True):
        bullet.rect.x = -100
        bullet.rect.y = 700
        all_sprites.add(bullet)

    if pygame.sprite.spritecollide(alienImg3, bullet_sprite, True):
        bullet.rect.x = -100
        bullet.rect.y = 700
        all_sprites.add(bullet)

    if pygame.sprite.spritecollide(alienImg4, bullet_sprite, True):
        bullet.rect.x = -100
        bullet.rect.y = 700
        all_sprites.add(bullet)

    if pygame.sprite.spritecollide(alienImg5, bullet_sprite, True):
        bullet.rect.x = -100
        bullet.rect.y = 700
        all_sprites.add(bullet)

    if pygame.sprite.spritecollide(alienImg6, bullet_sprite, True):
        bullet.rect.x = -100
        bullet.rect.y = 700
        all_sprites.add(bullet)

    if pygame.sprite.spritecollide(bomb, player_sprite, False):
        print('Lost a life')
        n += 2
    if pygame.sprite.spritecollide(playerImg, bomb_sprite, True):
        bomb.rect.y = 0
        bomb.rect.x = -100
        all_sprites.add(bomb)

    if alienImg1.rect.x == 0:
        alienLeft = False
    if alienImg3.rect.x == 776:
        alienRight = False
    if alienImg1.rect.x > 0 and alienRight == False:
        alienLeft = True
        alienImg1.left()
        alienImg2.left()
        alienImg3.left()
    elif alienImg3.rect.x < 776 and alienLeft == False:
        alienRight = True
        alienImg1.right()
        alienImg2.right()
        alienImg3.right()
    if i >= 30:
        if alienImg4.rect.x == 0:
            alienLeft = False
        if alienImg6.rect.x == 776:
            alienRight = False
        if alienImg4.rect.x > 0 and alienRight == False:
            alienLeft = True
            alienImg4.left()
            alienImg5.left()
            alienImg6.left()
        elif alienImg6.rect.x < 776 and alienLeft == False:
            alienRight = True
            alienImg4.right()
            alienImg5.right()
            alienImg6.right()

    screen.fill((0, 0, 0))

    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:

                playerImg.left()
                playerImg.left()
                playerImg.left()
            if event.key == pygame.K_RIGHT:
                playerImg.right()
                playerImg.right()
                playerImg.right()
            if event.key == pygame.K_SPACE:
                if bullet.rect.y >= 0:
                    bullet.rect.x = playerImg.rect.x - 5
                    bullet.rect.y = 500
                    fired = True
                    bulletSound = mixer.Sound(
                        r'Space Invaders\laser.wav')
                    bulletSound.play()
                else:
                    bullet.rect.y = 700
                    fired = False
        if event.type == pygame.MOUSEBUTTONUP:
            print('me')
            if mousePos[0] >= 720 and mousePos[0] <= 770 and mousePos[1] >= 10 and mousePos[1] <= 45:
                print('paused')
                pause()

    if fired == True:
        bullet.rect.y -= 10

    pauseButton = pygame.image.load(
        r'Space Invaders\pause.png')
    screen.blit(pauseButton, (390, -280))
    all_sprites.draw(screen)
    pygame.draw.rect(screen, RED, (playerImg.rect.x-17,
                                   playerImg.rect.y+70, 100, 10))
    pygame.draw.rect(screen, LT_GREEN,
                     (playerImg.rect.x-17, playerImg.rect.y+70, 100-(n*25), 10))
    show_score(textX, testY)
    pygame.display.update()
n = 0
while win:
    backgroundSound.fadeout(500)
    n += 1
    if n == 1:
        winSound = mixer.Sound(
            r'Space Invaders\Short_triumphal_fanfare-John_Stracke-815794903.wav')
        winSound.play()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            win = False
    game_win_text()
    pygame.display.update()


while gameOver:
    backgroundSound.fadeout(500)
    n += 1
    if n == 1:
        powerSound = mixer.Sound(
            r'Space Invaders\Power Failure-SoundBible.com-1821346166.wav')
        powerSound.play()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = False
    game_over_text()
    pygame.display.update()
