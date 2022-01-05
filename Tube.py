import pygame


class Tube:
    def __init__(self, width, height, level, x, speed):
        self.speed = speed
        self.width = width
        self.height_free = height
        self.level = level
        self.x = x
        if self.level == 0:
            self.height_down = 110
            self.height_up = 720 - self.height_free - self.height_down
        elif self.level == 1:
            self.height_down = 310
            self.height_up = 720 - self.height_free - self.height_down
        elif self.level == 2:
            self.height_down = 410
            self.height_up = 720 - self.height_free - self.height_down

    def render(self, screen):
        pygame.draw.rect(screen, pygame.Color("Green"), (self.x, 0, self.width, self.height_up))
        pygame.draw.rect(screen, pygame.Color("Green"), (self.x, 720 - self.height_down, self.width, 658))
