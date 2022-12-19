import pygame
from random import randint

Battle_screen = pygame.Surface((1040, 720))


class Circle:
    def __init__(self, screen, x, y, r):
        self.x = x
        self.y = y
        self.r = r
        self.color = BLACK
        self.screen = screen

    def hit_test(self, obj):
        if (obj.x - self.x) ** 2 + (obj.y - self.y) ** 2 <= self.r ** 2:
            boom(obj.x, obj.y)
            return True

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.r)


class WhiteCircle:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.y = y
        self.x = x
        self.r = BOOM_R
        self.color = WHITE

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.r)


def boom(screen, x, y):
    WhiteCircle(screen, x, y)


def obj_generate(screen):
    a = randint(10, 20)
    i = 0
    while i <= a:
        i += 1
        x = randint(40, 1000)
        y = randint(40, 660)
        r = randint(40-a, 300-10*a)
        Circle(screen, x, y, r)


BLACK = (0, 0, 0)
BOOM_R = 15
WHITE = (255, 255, 255)
