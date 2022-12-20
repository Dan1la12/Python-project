import simpleeval as se
import pygame
import numpy as np
from Objects import WhiteCircle
from Objects import white_circles

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 225, 0)
GREEN = (0, 0, 255)
LIGHT_GRAY = (200, 200, 200)
"""Цвета"""
L_WIGHT = 1  # Ширина линии
MARKER_R = 2  # Радиус маркера
markers = []  # список маркеров
lines = []  # Список линий


def graph_evaluate(i, graph_string):
    """
    Функция вычисляет значения выражения в строке graph_string при фиксированном i
    выдаёт 'err', если не может вычислить
    Args:
    i - относительная координата, float
    graph_string - строка
    предполагается что в ней сумма, произведение или композиция функций от переменной x:{ '+', '-', '*', '/', '**',
    sin(), cos(), exp()
    """
    graph_string_inside = ''
    for j in graph_string:
        if j == 'x':
            graph_string_inside += str(i)
        else:
            graph_string_inside += str(j)
    try:
        res = se.simple_eval(graph_string_inside, functions={'cos': lambda t: np.cos(t), 'sin': lambda t: np.sin(t),
                                                             'exp': lambda t: np.exp(t)})
        return res
    except:
        return 'err'


class Line:

    def __init__(self, x0, y0, x1, y1, screen, color):
        """
        Конструктор класса Line
        :param x0: x-координата начала
        :param y0: y-координата начала
        :param x1: x-координата конца
        :param y1: y-координата конца
        :param screen: экран для отрисовки
        :param color: цвет
        """
        self.screen = screen
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
        self.color = color
        self.active = True
        self.wight = L_WIGHT
        lines.append(self)

    def draw(self):
        """
        Рисует линию соединяющую (x0,y0), (x1,y1)
        """
        pygame.draw.line(self.screen, self.color, (self.x0, self.y0), (self.x1, self.y1), self.wight)

    def deactivate(self):
        """
        Переводит график в остывшее состояние
        меняет его цвет на LIGHT_GRAY
        """
        self.active = False
        self.color = LIGHT_GRAY


class Marker:
    def __init__(self, x, y, team, screen):
        """
        Конструктор класса Маркер - точки за которой прорисовывается график
        :param x, y: координаты
        :param team: принадлежность команде
        :param screen: экран отрисовки
        """
        self.screen = screen
        self.team = team
        self.x = x
        self.y = y
        self.r = MARKER_R
        markers.append(self)
        self.active = True

    def draw(self):
        """
        отрисовывает маркер
        """
        pygame.draw.circle(self.screen, self.color(), (self.x, self.y), self.r)

    def color(self):
        if self.team == 'Red':
            return YELLOW
        elif self.team == 'Blue':
            return GREEN

    def line_color(self):
        if self.team == 'Red':
            return RED
        elif self.team == 'Blue':
            return BLUE

    def move(self, x, y):
        """
        перемещает маркер на координату (x, y) и возвращает квадрат приращения длинны
        :param x: новая x-координата
        :param y: новая y-координата
        :return: s - квадрат длинны графика
        """
        Line(self.x, self.y, x, y, self.screen, self.line_color())
        self.x = x
        self.y = y
        return (x - self.x) ** 2 + (y - self.y) ** 2

    def remove(self):
        """
        Удаялет маркер
        """
        markers.remove(self)

    def hit_check(self, obj):
        """
        Проверяет столкновение с объектом: препятствием или солдатом
        если сталкивается с солддатом, идет дальше
        если сталкивается с перпятствием и не попадает в уничтоженную область,
            создает уничноженную область и деактивируется
        :param obj: объект, с которым проверяется столкновение
        """
        for circle in white_circles:
            if obj.alive and (self.x - obj.x) ** 2 + (self.y - obj.y) ** 2 <= obj.r ** 2 and (circle.x+self.x)**2 + \
                    (circle.y+self.y)**2 >= circle.r**2:
                """
                Проверяет попадание в объект
                """
                obj.hit()
                if obj.hit():
                    """
                    Проверяет, что попадание в препятствие а не в солдата
                    """
                    white_circle = WhiteCircle(self.screen, self.x, self.y)
                    white_circles.append(white_circle)
                    self.active = False
