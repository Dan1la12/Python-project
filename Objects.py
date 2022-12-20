import pygame
from random import randint

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
"""Цвета"""
BOOM_R = 15 # радиус взрыва
circles = []  # список препятствий
white_circles = []  # список дырок в препятствиях


class Circle:

    def __init__(self, screen, x, y, r):
        """
        Конструктор класса Circle - игровых препятствий
        :param screen: экран отрисовки
        :param x: x-координата
        :param y: y-координата
        :param r: радиус препятствия
        """
        self.x = x
        self.y = y
        self.r = r
        self.color = BLACK  # цвет
        self.screen = screen
        self.alive = True  # для hit_check, препятствие всегда alive = True

    def draw(self):
        """
        Отрисовывает препятствие
        """
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.r)


class WhiteCircle:
    def __init__(self, screen, x, y):
        """
        Конструктор класса WhiteCircle - дырок в препятствиях
        :param screen: экран отрисовки
        :param x: x-координата
        :param y: y-координата
        """
        self.screen = screen
        self.y = y
        self.x = x
        self.r = BOOM_R  # радиус
        self.color = WHITE  # цвет
        white_circles.append(self)

    def draw(self):
        """
        Отрисовывает дырку в препятствии
        """
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.r)


def obj_generate(screen):
    """
    Создает препятствия в начале игры
    :param screen: экран отрисовки
    Условия генерации писались по-приколу, тестер пока не балансил
    """
    a = randint(10, 20)
    i = 0
    while i <= a:
        i += 1
        x = randint(40, 1000)
        y = randint(40, 660)
        r = randint(40 - a, 300 - 10 * a)
        circle = Circle(screen, x, y, r)
        circles.append(circle)
