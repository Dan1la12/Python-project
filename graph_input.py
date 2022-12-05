import simpleeval
import pygame
from numpy import sin
from numpy import cos
battle_screen = pygame.display.set_mode((500, 500))
BLACK = (0, 0, 0)
FPS = 120
dt = 1/FPS

class Line:
    def __init__(self, x0, y0, x1, y1):
        pygame.draw.line(self.screen, self.color, (x0, y0), (x1, y1), self.wight)
    screen = battle_screen
    color = BLACK
    wight = 1


def function_calc(x_player, y_player):
    s = 0
    i = 0
    x0 = x_player
    y0 = y_player
    while s <= 700:
        func_ins = ''
        for j in func:
            if j == 'x':
                func_ins += str(i)
            else:
                func_ins += j
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
'''Починить'''




func = str(input())