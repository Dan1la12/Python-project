import simpleeval
import pygame
from numpy import sin
from numpy import cos


RED = 
LIGHT_GRAY =


def graph_evaluator(i, graph_string):
    x = i
    try:
       return eimpleeval(graph_string)
   except:
       return 'err'
'''Функция пытается вычислить относительное значение y при x = i для последующего использования в построении графика.
Или возвращает 'err' что остановит построение графика'''


class Line:


    def __init__(self, x0, y0, x1, y1):
        pygame.draw.line(self.screen, self.color, (x0, y0), (x1, y1), self.wight)


    def deactivate(self):
        active = False
        color = LIGHT_GRAY


    active = True
    screen = battle_screen
    color = RED
    wight = 3
'''Линия соединяющая близкие точки графика с координатами (x0, y0) (x1, y1), deactivate() служит для перевода графика в остывшее состояние - изменяет цвет'''


def kill_check(xi, yi)
    for soldier in Soldiers:
        if (xi - soldier.x)**2 + (yi - soldier.y)**2 <= soldier.r**2:
            soldier.death()
'''Проверяет попадание в солдата с координатами self.x и self.y графиком, с текущими координатами xi и yi'''


def graph_clean():
    for line in Line:
        if line.active:
            line.deactivate()
'''Переводит график в остывшее состояние'''


