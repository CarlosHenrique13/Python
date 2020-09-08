import pygame
import  math
import random

class Shot(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("data/shot.png")  # 32x32
        self.image = pygame.transform.scale(self.image, [10, 10])
        self.rect = self.image.get_rect()



        self.speed = 7

    def update(self, *args):
        # LOGICA!
        self.rect.x += self.speed

        if self.rect.left > 840:
            self.kill()
