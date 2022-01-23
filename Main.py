import pygame
from Tube import Tube
from Bird import Bird


if __name__ == '__main__':
    pygame.init()

    size = 950, 720
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Flappy bird")
    background_position = [0, 0]
    background_image = pygame.image.load("data/bg1.png").convert()

    running = True
    time_of_tube = 0
    clock = pygame.time.Clock()
    all_Bird = pygame.sprite.Group()
    Bird(all_Bird)
    all_tubes = pygame.sprite.Group()
    die_sound = pygame.mixer.Sound("data/die.ogg")
    wing_sound = pygame.mixer.Sound("data/wing.ogg")
    point_sound = pygame.mixer.Sound("data/point.ogg")
    while running:
        time_of_tube += 1
        screen.blit(background_image, background_position)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    all_Bird.update()
                    wing_sound.play()
        all_Bird.draw(screen)
        if time_of_tube % 100 == 0:
            Tube(all_tubes)
        all_tubes.draw(screen)
        all_tubes.update()
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()