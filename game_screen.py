import pygame
from random import randint

Battle_screen = pygame.Surface((1040, 720))
circles = []
white_circles = []


class Circle:
    def __init__(self, screen, x, y, r):
        self.x = x
        self.y = y
        self.r = r
        self.color = BLACK
        self.screen = screen

    def hit(self):
        white_circle = WhiteCircle()
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
        circle = Circle(screen, x, y, r)
        circles.apend(circle)


BLACK = (0, 0, 0)
BOOM_R = 15
WHITE = (255, 255, 255)
