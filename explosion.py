import pygame
from consts import *
from app import is_running


class Bird(pygame.sprite.Sprite):

    i = 0

    def __init__(self):
        super().__init__()
        self.birds = [BIRD1_IMAGE, BIRD2_IMAGE, BIRD3_IMAGE]
        self.image = pygame.image.load(BIRD1_IMAGE)
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = SCREEN_SIZE[1]//2

    def fly(self):
        if Bird.i > 2:
            Bird.i = 0
        self.image = pygame.image.load(self.birds[Bird.i])

        Bird.i += 1
        self.rect.y += 2

    def flyUp(self):
        self.rect.y -= 5

    def flyDown(self):
        self.rect.y += 3

    def fallDown(self):
        if self.rect.y == SCREEN_SIZE[1]-168:
            is_running = False
