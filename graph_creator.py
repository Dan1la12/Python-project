import simpleeval as se
import pygame
import numpy as np
from Soldiers import  Soldier

RED = (255, 0, 0)
LIGHT_GRAY = (200, 200, 200)
L_WIGHT = 2


def graph_evaluate(i, graph_string):
    x = i
    try:
        return se.simple_eval(graph_string, function={'cos': lambda t: np.cos(t), 'sin': lambda t: np.sin(t)})
    except:
        return 'err'


'''Функция пытается вычислить относительное значение y при x = i для последующего использования в построении графика.
Или возвращает 'err' что остановит построение графика'''


class Line:

    def __init__(self, x0, y0, x1, y1, screen, color):
        self.screen = screen
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
        self.color = color
        self.active = True
        self.wight = L_WIGHT

    def draw(self):
        pygame.draw.line(self.screen, self.color, (self.x0, self.y0), (self.x1, self.y1), self.wight)

    def deactivate(self):
        self.active = False
        self.color = LIGHT_GRAY


'''Линия соединяющая близкие точки графика с координатами (x0, y0) (x1, y1), deactivate() служит для перевода графика 
в остывшее состояние - изменяет цвет '''


def kill_check(xi, yi):
    for soldier in Soldier:
        soldier.self_kill_check(soldier, xi, yi)
# FIXME проверить работу


'''Проверяет попадание в солдата с координатами self.x и self.y графиком, с текущими координатами xi и yi'''
