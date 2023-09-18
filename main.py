import pygame
from game import Game
from snake import Snake
pygame.init()


def setup():
    game_setup = Game(500, 500, 'mari')
    snake_setup = Snake()
    game_setup.snake = snake_setup
    return game_setup


if __name__ == '__main__':
    game = setup()
    run = 2
    while run == 2:
        run = game.play()
        if run == 1:
            game.restart()
            run = 2




