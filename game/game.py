import os

import pygame
import random


class Game:
    def __init__(self, height, width, caption):
        self.win = pygame.display.set_mode((height, width))
        self.background = pygame.image.load(os.path.join(os.path.dirname(__file__), 'background/background.jpg'))
        pygame.transform.scale(self.background, (width, height))
        self.height_blit = 0
        self.width_blit = 0
        self.win.blit(self.background, (self.width_blit, self.height_blit))
        self.width = width
        self.height = height
        self.snake = None
        self.caption = caption
        pygame.display.set_caption(self.caption)
        self.y_food = random.randrange(50, 450, 10)
        self.x_food = random.randrange(50, 450, 10)
        self.pause = False
        self.add_food()

    def restart(self):
        self.snake.restart()
        self.height_blit = 0
        self.width_blit = 0
        self.background = pygame.image.load(os.path.join(os.path.dirname(__file__), 'background/background.jpg'))
        self.win.blit(self.background, (self.width_blit, self.height_blit))
        self.pause = False
        self.add_food()

    def eat_food(self):
        position = self.snake.get_position()
        if self.x_food - 20 < position[0] < self.x_food and self.y_food - 20 < position[1] < self.y_food:
            self.y_food = random.randrange(50, 450, 10)
            self.x_food = random.randrange(50, 450, 10)
            self.snake.add_body()
            return True

    def add_food(self):
        pygame.draw.rect(self.win, (255, 255, 255), (self.x_food, self.y_food, 10, 10))

    def clear_window(self):
        self.win.blit(self.background, (self.width_blit, self.height_blit))
        if not self.pause:
            self.win.blit(self.snake.player_image, self.snake.player_rect)

    def play(self):
        pygame.time.delay(100)
        for even in pygame.event.get():
            if even.type == pygame.QUIT:
                return 0
        key = pygame.key.get_pressed()
        self.snake.move_auto(key)
        self.snake.move_snake()
        if self.game_over():
            self.height_blit = 200
            self.width_blit = 75
            self.play_again()
            self.pause = True
        if self.pause and key[pygame.K_SPACE]:
            return 1

        self.eat_food()
        self.clear_window()
        self.add_food()
        if not self.pause:
            self.snake.make_snake(self.win)
        pygame.display.update()
        return 2

    def play_again(self):
        font = pygame.font.SysFont("None", 45)
        self.background = font.render('press space to play again', True, 'red')

    def game_over(self):
        if (self.snake.player_rect.x == 0 or self.snake.player_rect.x == (self.width - self.snake.width) or
                self.snake.player_rect.y == 0 or self.snake.player_rect.y == (self.height - self.snake.height)):
            font = pygame.font.SysFont("None", 45)
            text = font.render('game over', True, 'blue', 'white')
            self.win.blit(text, (170, 100))
            return True
        if [self.snake.player_rect.x, self.snake.player_rect.y] in self.snake.get_body[1:]:
            return True
