import simpleeval
import pygame
from numpy import sin
from numpy import cos
battle_screen = pygame.display.set_mode((500, 500))
BLACK = (0, 0, 0)
FPS = 120#возможно, должно быть не здесь
dt = 1/FPS
max_lenght = 700
class Line:
    def __init__(self, x0, y0, x1, y1):
        pygame.draw.line(self.screen, self.color, (x0, y0), (x1, y1), self.wight)
    screen = battle_screen
    color = BLACK
    wight = 3


def function_calc(x_player, y_player, func):
    s = 0
    i = 0
    x0 = x_player
    y0 = y_player
    func_ins = '' #внутркнняя функция, где x заменён на i
    for j in func:
        if j == 'x':
            func_ins += str(i)
        else:
            func_ins += j
    while s<= max_lenght:
        i += dt
        x1 = x0 + i
        while True:
            try:
                y1 = simpleeval(func_ins)
                break
            except:
                print('Произошла ошибка, проверьте ввод функции')
                func = str(input())
        s += ((x1-x0)**2 +(y1-y0)**2)**0.5
        Line(x0, y0, x1, y1)
        for soldier in Soldiers: #проверка смерти, можно убить своего
            if soldier != active: #чтобы не убить себя
                if (soldier.x - x1)**2 + (soldier.y - y1)** <= soldier.R**2:
                    soldier.death()
'''Функция принимает значения координаты солдата x_player, y_player и введеный график func() и отрисовывает график начиная из него. Допустимый ввод предполагает использование стандартного скрипта python и функций sin() и cos().
Если програма не может посчитать значение функции в какой-то точке, пишет 'Произошла ошибка...' FIXME: переделать, возможен абуз механики
Должна проверять попадание в другого солдата FIXME: пока не работает'''




func = str(input())


def soldier_deat():
    pass #пока нет такой функции
