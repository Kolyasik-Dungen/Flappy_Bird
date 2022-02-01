import pygame
from buttons import *
from Tube import Tube
from Bird import Bird

pygame.init()


class Main_Menu:
    def __init__(self):
        self.size = (950, 720)
        self.screen = pygame.display.set_mode(self.size)
        self.background_position = [0, 0]
        self.flappy_logo_position = [200, 20]
        self.background_image = pygame.image.load('data/bg1.png').convert()
        self.flappy_logo = pygame.image.load('data/Flappy_Bird_Logo.png')
        self.flappy_logo = pygame.transform.scale(self.flappy_logo, (500, 133.5))

    def run(self):
        running = True

        self.play_button = Button(460, 250, 200, 100, (255, 255, 255), (0, 191, 255), 'Play', 100)

        self.exit_button = Button(460, 400, 200, 100, (255, 255, 255), (0, 191, 255), 'Exit', 100)

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    quit()

            self.screen.blit(self.background_image, self.background_position)
            self.screen.blit(self.flappy_logo, self.flappy_logo_position)

            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            if self.play_button.is_pressed(mouse_pos, mouse_pressed):
                running = False

            if self.exit_button.is_pressed(mouse_pos, mouse_pressed):
                quit()

            for button in [self.play_button, self.exit_button]:
                button.color_change(mouse_pos)
                button.update(self.screen)

            pygame.display.update()

            pygame.display.flip()


class End_Menu:
    def __init__(self):
        self.size = (950, 720)
        self.screen = pygame.display.set_mode(self.size)
        self.background_position = [0, 0]
        self.flappy_logo_position = [200, 20]
        self.background_image = pygame.image.load('data/bg1.png').convert()

        # self.score - переменная с количеством очков. Может конфликтовать со шрифтом, так как у него нет шрифтовых цифр
        self.score = 1

    def run_end(self):
        self.running = True

        self.best_score_export = Button(460, 90, 300, 100, (255, 255, 255), (0, 191, 255),
                                        f"Best {round(int(score_best))}", 100)

        self.score_export = Button(460, 220, 600, 100, (255, 255, 255), (0, 191, 255), f"Youre score is {round(score)}",
                                   100)

        self.exit_button = Button(460, 350, 200, 100, (255, 255, 255), (0, 191, 255), 'Exit', 100)

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.blit(self.background_image, self.background_position)

            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            if self.exit_button.is_pressed(mouse_pos, mouse_pressed):
                self.running = False
                # go1.run()

            for button in [self.score_export, self.exit_button, self.best_score_export]:
                button.color_change(mouse_pos)
                button.update(self.screen)

            pygame.display.update()

            pygame.display.flip()
        quit()


go = End_Menu()

go1 = Main_Menu()
f = open("score.txt", encoding="utf8")
score_best = f.readline()
f.close()
go1.run()
pygame.init()
size = 950, 720
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Flappy bird")
background_position = [0, 0]
background_image = pygame.image.load("data/bg1.png").convert()
running = True
pix = 0
score = 0
text_x = 475
text_y = 70
font = pygame.font.Font('data/Flappy-Bird.ttf', 100)
time_of_tube = 0
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
    text = font.render(str(round(score)), True, (255, 255, 255))

    if bird.intersect(all_tubes.sprites()):
        score += 0.055555
        pix += 1
        if pix // 18:
            pix = 0
            point_sound.play()

    for tube in all_tubes.sprites():
        if pygame.sprite.collide_mask(bird, tube):
            running = False
            f = open("score.txt", 'w')
            if int(score_best) <= round(score):
                score_best = score
            print(round(int(score_best)), file=f)
            f.close()
    screen.blit(background_image, background_position)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            quit()
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
    screen.blit(text, (text_x, text_y))
    pygame.display.flip()
    clock.tick(60)
go.run_end()
