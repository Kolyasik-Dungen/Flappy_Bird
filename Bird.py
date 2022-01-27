from typing import List

import pygame
import os
import sys

from pygame.sprite import Sprite

from Tube import Tube


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class Bird(pygame.sprite.Sprite):
    image = load_image("brd.png")
    image.set_colorkey("WHITE")

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Bird.image
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 100

        self.gravity = 1

    def update(self):
        self.rect = self.rect.move(0, self.gravity)
        self.gravity += 1

    def set_jump(self):
        self.gravity = -10

    def intersect(self, tubes: List[Sprite]):
        for tube in tubes:
            if tube.rect.colliderect(self.rect):
                return True
        return False