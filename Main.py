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
    speed = 5
    height_free = 220
    width = 60
    x = 1250
    clock = pygame.time.Clock()
    while running:
        screen.blit(background_image, background_position)
        level = randint(0, 2)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        test_tube = Tube(width, height_free, level, x, speed)
        test_tube.render(screen)
        x -= speed
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()