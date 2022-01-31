import pygame


class Button():
    def __init__(self, x_coord, y_coord, button_w, button_h, font_color, background_color, button_text, font_size):
        self.x_coord = x_coord
        self.y_coord = y_coord

        self.button_w = button_w
        self.button_h = button_h

        self.font_color = font_color
        self.background_color = background_color

        self.button_text = button_text

        self.font = pygame.font.Font('data/FlappyBirdy.ttf', font_size)

        self.image = pygame.Surface((self.button_w, self.button_h))
        self.image.fill(self.background_color)
        self.rect = self.image.get_rect(center=(self.x_coord, self.y_coord))

        self.rect.x = self.x_coord
        self.rect.y = self.y_coord

        self.text = self.font.render(self.button_text, True, self.font_color)
        self.text_rect = self.text.get_rect(center=(self.button_w / 2, self.button_h / 2))
        self.rect = self.image.get_rect(center=(self.x_coord, self.y_coord))
        self.image.blit(self.text, self.text_rect)

    def is_pressed(self, pos, pressed):
        if self.rect.collidepoint(pos):
            if pressed[0]:
                return True
            return False
        return False

    def update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)
        self.image.blit(self.text, self.text_rect)

    def color_change(self, mouse_pos):
        if (mouse_pos[0] > self.rect.left) and (mouse_pos[0] < self.rect.right) and (mouse_pos[1] > self.rect.top) and (mouse_pos[1] < self.rect.bottom):
            self.text = self.font.render(self.button_text, True, (0, 255, 0))
            #Если хочешь добавить звук, то убери комменты вначале
            #pygame.mixer.music.load('data/click.mp3')
            #pygame.mixer.music.play(0)
        else:
            self.text = self.font.render(self.button_text, True, (255, 255, 255))