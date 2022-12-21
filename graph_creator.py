import simpleeval as se
import pygame
import numpy as np
from Objects import WhiteCircle
from Objects import white_circles, circles
from Soldiers import soldiers, R
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 225, 0)
GREEN = (0, 0, 255)
LIGHT_GRAY = (200, 200, 200)
"""Цвета"""
L_WIGHT = 1  # Ширина линии
MARKER_R = 4  # Радиус маркера
markers = []  # список маркеров
lines = []  # Список линий


def graph_evaluate(i, graph_string):
    """
    Функция вычисляет значения выражения в строке graph_string при фиксированном i
    выдаёт 'err', если не может вычислить, или f(0) != 0
    Args:
    i - относительная координата, float
    graph_string - строка
    предполагается что в ней сумма, произведение или композиция функций от переменной x:{ '+', '-', '*', '/', '**',
    sin(), cos(), exp()
    """
    graph_string_inside = ''
    graph_string_zero = ''
    for j in graph_string:
        if j == 'x':
            graph_string_inside += str(i)
            graph_string_zero += '0'
        else:
            graph_string_inside += str(j)
            graph_string_zero += str(j)

    try:
        res = se.simple_eval(graph_string_inside, functions={'cos': lambda t: np.cos(t), 'sin': lambda t: np.sin(t),
                                                             'exp': lambda t: np.exp(t)})
        res1 = se.simple_eval(graph_string_zero, functions={'cos': lambda t: np.cos(t), 'sin': lambda t: np.sin(t),
                                                             'exp': lambda t: np.exp(t)})
        if res1 == 0:
            return res
        else:
            return 'err'
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

    def color(self):
        if self.team == 'Red':
            return YELLOW
        elif self.team == 'Blue':
            return GREEN

    def draw(self):
        """
        отрисовывает маркер
        """
        pygame.draw.circle(self.screen, self.color(), (self.x, self.y), self.r)

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
        s = (x - self.x) ** 2 + (y - self.y) ** 2
        self.x = x
        self.y = y
        print(s)
        return s

    def remove(self):
        """
        Удаялет маркер
        """
        markers.remove(self)

    def soldier_hit_check(self, number, team):
        """
        порверяет на столкновение маркера с солдатами, кроме того, кто делает ход (определяется командой и номером)
        Args:
            number: номер стреляющего солдата
            team: команда, которой принадлежит солдат
        Returns:
        """
        for s in soldiers:
            if (s.x - self.x) ** 2 + (s.y - self.y) ** 2 <= R ** 2 and not (s.number == number and s.team == team):
                s.hit()

    def circle_check_hit(self, screen):
        """
        Проверяет столкновение маркера с препятствиями, при столкновении создаёт дырку, при попадании в дырку ничего
        не происходит
        Args: screen: экран отрисовки дырки
        Returns: True, при столкновении
        """
        for c in circles:
            if (c.x - self.x) ** 2 + (c.y - self.y) ** 2 <= c.r ** 2:
                for wc in white_circles:
                    if (wc.x - self.x) ** 2 + (wc.y - self.y) ** 2 <= wc.r:
                        break
                WhiteCircle(screen, self.x, self.y)
                return True

