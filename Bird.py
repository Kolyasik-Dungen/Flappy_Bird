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


class Bird(pygame.sprite.Sprite):
    image = load_image("bird_stand.jpg")

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Bird.image
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 150