import pygame
from consts import *


class SpaceCraft(pygame.sprite.Sprite):

    i = 0

    def __init__(self):
        super().__init__()

        self.image = pygame.image.load(
            r'Space Invaders\player.png')
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 500

    def right(self):
        self.rect.x += 10

    def left(self):
        self.rect.x -= 10
