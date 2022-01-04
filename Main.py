import pygame
from random import randint
from Tube import Tube
import time

if __name__ == '__main__':
    pygame.init()

    size = 1220, 720
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Flappy bird")
    background_position = [0, 0]
    background_image = pygame.image.load("images/city_day.jpg").convert()

    running = True
    speed = 20
    height_free = 100
    width = 50
    clock = pygame.time.Clock()
    while running:
        screen.blit(background_image, background_position)
        level = randint(0, 3)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        test_tube = Tube(width, height_free, level)
        test_tube.render(screen)
        pygame.display.flip()
    pygame.quit()