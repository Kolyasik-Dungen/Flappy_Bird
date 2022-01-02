import pygame

if __name__ == '__main__':
    pygame.init()

    size = 1220, 720
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Flappy bird")
    background_position = [0, 0]
    background_image = pygame.image.load("images/city_day.jpg").convert()

    running = True
    r = 0
    b = 1
    clock = pygame.time.Clock()
    while running:
        screen.blit(background_image, background_position)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()
    pygame.quit()