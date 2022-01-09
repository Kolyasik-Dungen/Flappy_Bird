import pygame
from Tube import Tube
from Bird import Bird


if __name__ == '__main__':
    pygame.init()

    size = 288, 360
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Flappy bird")
    background_position = [0, 0]
    background_image = pygame.image.load("data/bg1.png").convert()

    running = True
    clock = pygame.time.Clock()
    all_Bird = pygame.sprite.Group()
    all_tubes = pygame.sprite.Group()
    screen.blit(background_image, background_position)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        Tube(all_tubes)
        all_tubes.draw(screen)
        all_tubes.update()
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()