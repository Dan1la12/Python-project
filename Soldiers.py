import pygame


class Soldier:

    def __init__(self, x, y, team, screen, number):
        self.number = number
        self.alive = True
        self.x = x
        self.y = y
        self.team = team
        self.screen = screen
        self.r = R
        self.r_i = R_I

    def draw_red(self):
        pygame.draw.circle(self.screen, RED, (self.x, self.y), self.r)
        pygame.draw.circle(self.screen, LIGHT_RED, (self.x, self.y), self.r_i)

    def draw_blue(self):
        pygame.draw.circle(self.screen, BLUE, (self.x, self.y), self.r)
        pygame.draw.circle(self.screen, LIGHT_BLUE, (self.x, self.y), self.r_i)

    def draw_dead(self):
        pygame.draw.circle(self.screen, GRAY, (self.x, self.y), self.r)
        pygame.draw.circle(self.screen, LIGHT_GRAY, (self.x, self.y), R_I)

    def alive(self):
        return self.alive

    def team(self):
        return self.team

    def self_kill_check(self, x, y):
        if (x - self.x) ** 2 + (y - self.y) ** 2 <= self.r ** 2:
            self.death()

    def death(self):
        self.alive = False
        # возможно добавлю взрыв


GRAY = (100, 100, 100)
LIGHT_GRAY = (200, 200, 200)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
LIGHT_RED = (200, 0, 0)
LIGHT_BLUE = (0, 0, 200)
R = 10
R_I = 8
