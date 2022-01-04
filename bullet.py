import pygame
from consts import *


class Bullet(pygame.sprite.Sprite):
    # global not_hit
    # not_hit = True

    def __init__(self):
        super().__init__()

        self.image = pygame.image.load(
            r'Space Invaders\bullet.png')
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 700
