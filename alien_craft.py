import pygame
from consts import *


class AlienCraft(pygame.sprite.Sprite):

    i = 0

    def __init__(self):
        super().__init__()

        self.image = pygame.image.load(
            r'Space Invaders\enemy.png')
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 100

    def right(self):
        self.rect.x += 4

    def left(self):
        self.rect.x -= 4

    def changeCd(self, x, y):
        self.rect.x = x
        self.rect.y = y
