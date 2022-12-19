import pygame

soldiers = []  # возможно придется убрать


class Soldier:

    def __init__(self, x, y, team, screen, number):
        """
        Конструктор класса Soldier
        :param x: x-координата
        :param y: y-координата
        :param team: команда ('Blue', или 'Red')
        :param screen: экран отрисовки
        :param number: порядковый номер
        """
        self.number = number
        self.alive = True
        self.x = x
        self.y = y
        self.team = team
        self.screen = screen
        self.r = R
        self.r_i = R_I
        soldiers.append(self)

    def color1(self):
        """
        сопоставляет живым солдатам из команд и мертвым солдатам основной цвет отрисовки
        'Red' - RED
        'Blue' - BLUE
        alive == FALSE - GRAY

        """
        if self.alive and self.team == 'Blue':
            return BLUE
        elif self.alive and self.team == 'Red':
            return RED
        else:
            return GRAY

    def color2(self):
        """
        сопоставляет живым солдатам из команд и мертвым солдатам вторичный цвет отрисовки
        'Red' - LIGHT_RED
        'Blue' - LIGHT_BLUE
        alive == FALSE - LIGHT_GRAY
        """
        if self.alive and self.team == 'Blue':
            return LIGHT_BLUE
        elif self.alive and self.team == 'Red':
            return LIGHT_RED
        else:
            return LIGHT_GRAY

    def draw(self):
        """
        Отрисовывает солдат в 2 цвета
        """
        pygame.draw.circle(self.screen, self.color1, (self.x, self.y), self.r)
        pygame.draw.circle(self.screen, self.color2, (self.x, self.y), self.r_i)

    def hit(self):
        """
        Убивает солдата при попадании
        :return: False - для hit_test
        """
        self.alive = False
        return False
        # возможно добавлю звук


GRAY = (100, 100, 100)
LIGHT_GRAY = (200, 200, 200)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
LIGHT_RED = (200, 0, 0)
LIGHT_BLUE = (0, 0, 200)
R = 10
R_I = 8
