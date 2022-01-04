import pygame
from consts import *


class Bomb(pygame.sprite.Sprite):
    global not_hit
    not_hit = True

    def __init__(self):
        super().__init__()
        bombImg = pygame.image.load(
            r'Space Invaders\alienBomb.png')
        bombImg = pygame.transform.scale(bombImg, (40, 40))
        self.image = bombImg
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
