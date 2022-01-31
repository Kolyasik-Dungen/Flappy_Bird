import pygame
from buttons import *


class Menu:
    def __init__(self, screen):
        self.screen = screen
        flappy_logo_position = [200, 20]
        background_image = pygame.image.load('data/bg1.png').convert()
        flappy_logo = pygame.image.load('data/Flappy_Bird_Logo.png')
        flappy_logo = pygame.transform.scale(flappy_logo, (500, 133.5))

        play_button = Button(460, 250, 200, 100, (255, 255, 255), (0, 191, 255), 'Play', 100)

        exit_button = Button(460, 400, 200, 100, (255, 255, 255), (0, 191, 255), 'Exit', 100)
        self.screen.blit(background_image, [0, 0])
        self.screen.blit(flappy_logo, flappy_logo_position)

        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()

        if play_button.is_pressed(mouse_pos, mouse_pressed):
            print('hello is pressed')

        for button in [play_button, exit_button]:
            button.color_change(mouse_pos)
            button.update(screen)