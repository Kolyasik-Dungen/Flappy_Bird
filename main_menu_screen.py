import pygame
from buttons import *

pygame.init()


size = (950, 720)
screen = pygame.display.set_mode(size)
background_position = [0, 0]
flappy_logo_position = [200, 20]
background_image = pygame.image.load('data/bg1.png').convert()
flappy_logo = pygame.image.load('data/Flappy_Bird_Logo.png')
flappy_logo = pygame.transform.scale(flappy_logo, (500, 133.5))


play_button = Button(460, 250, 200, 100, (255, 255, 255), (0, 191, 255), 'Play', 100)

exit_button = Button(460, 400, 200, 100, (255, 255, 255), (0, 191, 255), 'Exit', 100)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background_image, background_position)
    screen.blit(flappy_logo, flappy_logo_position)

    mouse_pos = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()

    if play_button.is_pressed(mouse_pos, mouse_pressed):
        print('hello is pressed')

    if exit_button.is_pressed(mouse_pos, mouse_pressed):
        running = False

    for button in [play_button, exit_button]:
        button.color_change(mouse_pos)
        button.update(screen)

    pygame.display.update()

    pygame.display.flip()
quit()