from random import randint
import pygame
import os
import sys


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class Tube(pygame.sprite.Sprite):
    image = load_image("spr_block.png")
    image.set_colorkey("WHITE")
    last = []

    def __init__(self, *group):
        super().__init__(*group)
        self.y = randint(-285, -75)
        self.image = Tube.image
        self.rect = self.image.get_rect()
        self.rect.x = 1050
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.y = self.y
        self.last = self

    def update(self):
        self.rect = self.rect.move(-5, 0)
