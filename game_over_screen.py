import pygame
from buttons import *

pygame.init()


size = (950, 720)
screen = pygame.display.set_mode(size)
background_position = [0, 0]
flappy_logo_position = [200, 20]
background_image = pygame.image.load('data/bg1.png').convert()


play_button = Button(460, 250, 300, 100, (255, 255, 255), (0, 191, 255), 'Play Again', 100)

#score - переменная с количеством очков. Может конфликтовать со шрифтом, так как у него нет шрифтовых цифр
score = 1
score_export = Button(460, 100, 600, 100, (255, 255, 255), (0, 191, 255), f"Youre score is {score}", 100)

exit_button = Button(460, 400, 200, 100, (255, 255, 255), (0, 191, 255), 'Exit', 100)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background_image, background_position)

    mouse_pos = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()

    #if play_button.is_pressed(mouse_pos, mouse_pressed):
        #print('hello is pressed')

    #if exit_button.is_pressed(mouse_pos, mouse_pressed):
        #running = False

    for button in [play_button, score_export, exit_button]:
        button.color_change(mouse_pos)
        button.update(screen)

    pygame.display.update()

    pygame.display.flip()
quit()