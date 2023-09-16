import pygame


class Snake:
    def __init__(self):
        self.height = 10
        self.width = 10
        self.auto_x = 10
        self.auto_y = 0
        self.speed = 10
        self.body_snake = [
            [140, 50],
            [130, 50],
            [120, 50],
            [110, 50],
            [100, 50],
        ]
        self.rotate = None
        self.player_image = pygame.image.load('image_snake/left.png').convert()
        self.player_image = pygame.transform.scale(self.player_image, (30, 30))
        self.player_rect = self.player_image.get_rect()
        self.player_rect.x = 140
        self.player_rect.y = 50
        self.player_image = pygame.transform.rotate(self.player_image, 90)

    def rotate_image(self, rotate_x, rotate_y):
        if rotate_x < 0 < self.auto_y:
            self.player_image = pygame.transform.rotate(self.player_image, 90)
        if rotate_x > 0 and 0 < self.auto_y:
            self.player_image = pygame.transform.rotate(self.player_image, -90)
        if rotate_x < 0 and 0 > self.auto_y:
            self.player_image = pygame.transform.rotate(self.player_image, -90)
        if rotate_x > 0 > self.auto_y:
            self.player_image = pygame.transform.rotate(self.player_image, 90)
        if rotate_y < 0 < self.auto_x:
            self.player_image = pygame.transform.rotate(self.player_image, -90)
        if rotate_y > 0 and 0 < self.auto_x:
            self.player_image = pygame.transform.rotate(self.player_image, 90)
        if rotate_y < 0 and 0 > self.auto_x:
            self.player_image = pygame.transform.rotate(self.player_image, 90)
        if rotate_y > 0 > self.auto_x:
            self.player_image = pygame.transform.rotate(self.player_image, -90)

    def move_auto(self, key):
        if key[pygame.K_LEFT] and self.auto_x <= 0:
            rotate_x = self.auto_x
            rotate_y = self.auto_y
            self.auto_x = -self.speed
            self.auto_y = 0
            self.rotate_image(rotate_x, rotate_y)
        if key[pygame.K_RIGHT] and self.auto_x >= 0:
            rotate_x = self.auto_x
            rotate_y = self.auto_y
            self.auto_x = self.speed
            self.auto_y = 0
            self.rotate_image(rotate_x, rotate_y)

        if key[pygame.K_UP] and self.auto_y <= 0 and self.rotate != 2:
            rotate_x = self.auto_x
            rotate_y = self.auto_y
            self.auto_x = 0
            self.auto_y = -self.speed
            self.rotate = 2
            self.rotate_image(rotate_x, rotate_y)

        if key[pygame.K_DOWN] and self.auto_y >= 0 and self.rotate != 3:
            rotate_x = self.auto_x
            rotate_y = self.auto_y
            self.auto_x = 0
            self.auto_y = self.speed
            self.rotate = 3
            self.rotate_image(rotate_x, rotate_y)

    def move_snake(self):
        self.player_rect.x += self.auto_x
        self.player_rect.y += self.auto_y
        self.body_snake.insert(0, [self.player_rect.x, self.player_rect.y])
        self.body_snake.pop()

    @property
    def get_body(self):
        return self.body_snake

    def get_position(self):
        return self.player_rect.x, self.player_rect.y

    def make_snake(self, win):
        for x, y in self.body_snake[1:]:
            pygame.draw.rect(win, (160, 196, 50), (x + 10, y + 10, self.height, self.width))

    def add_body(self):
        self.body_snake.append([self.player_rect.x, self.player_rect.y])

