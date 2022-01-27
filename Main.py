import pygame
from Tube import Tube
from Bird import Bird

if __name__ == '__main__':
    pygame.init()

    size = 1024, 360
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Flappy bird")
    background_position = [0, 0]
    background_image = pygame.image.load("data/bg1.png").convert()

    running = True
    clock = pygame.time.Clock()
    all_Bird = pygame.sprite.Group()
    bird = Bird(all_Bird)
    all_tubes = pygame.sprite.Group()
    SPAWNEVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(SPAWNEVENT, 2000)
    die_sound = pygame.mixer.Sound("data/die.ogg")
    wing_sound = pygame.mixer.Sound("data/wing.ogg")
    point_sound = pygame.mixer.Sound("data/point.ogg")

    while running:
        screen.blit(background_image, background_position)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == SPAWNEVENT:
                Tube(all_tubes)
                pygame.time.set_timer(SPAWNEVENT, 2000)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.set_jump()
                    wing_sound.play()
        all_Bird.update()
        all_Bird.draw(screen)
        all_tubes.update()
        all_tubes.draw(screen)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
