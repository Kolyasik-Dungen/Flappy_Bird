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
    image.set_colorkey('White')

    def __init__(self, *group):
        super().__init__(*group)
        self.y = randint(-285, -75)
        self.image = Tube.image
        self.rect = self.image.get_rect()
        self.rect.x = 1000
        self.rect.y = self.y

    def update(self):
        self.rect = self.rect.move(-3, 0)