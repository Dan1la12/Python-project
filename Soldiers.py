import pygame

soldiers = []  # возможно придется убрать
GRAY = (100, 100, 100)
LIGHT_GRAY = (200, 200, 200)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
LIGHT_RED = (255, 70, 70)
LIGHT_BLUE = (70, 70, 255)
TRANSPARENT_RED = (255, 200, 200, 0.4)
TRANSPARENT_BLUE = (200, 200, 255, 0.4)
R = 20
R_I = 16


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
        pygame.draw.circle(self.screen, self.color1(), (self.x, self.y), self.r)
        pygame.draw.circle(self.screen, self.color2(), (self.x, self.y), self.r_i)

    def hit(self):
        """
        Убивает солдата при попадании
        :return: False - для hit_test
        """
        self.alive = False
        # возможно добавлю звук


class PlaceCircle:
    def __init__(self, screen, team, x, y):
        """
        Конструктор класса PlaceCircle - вспомогательного кружка при размещении солдат игроками
        :param screen: экран отрисовки
        :param team: команда, к которой он принадлежит
        :param x: x-координата
        :param y: y-координата
        """
        self.screen = screen
        self.y = y
        self.x = x
        self.team = team
        self.r = R

    def color(self):
        """
        сопоставляет цвет своей комагде
        """
        if self.team == 'Blue':
            return TRANSPARENT_BLUE
        elif self.team == 'Red':
            return TRANSPARENT_RED

    def draw(self):
        """
        Отрисовывает вспомогательный кружок
        """
        pygame.draw.circle(self.screen, self.color(), (self.x, self.y), self.r)

    def move(self, x, y):
        """
        Перемещает его (вслед за мышкой)
        :param x: новая x-координата
        :param y: новая y-координата
        """
        self.x = x
        self.y = y