import pygame.draw

from Objects import circles
from Soldiers import Soldier, soldiers, R, R_I

LAMP_COORDS = (100, 800)
LAMP_R = 30
LAMP_R_I = 25
RED = (255, 0, 0)
BLUE = (0, 0, 255)
LIGHT_RED = (255, 70, 70)
LIGHT_BLUE = (70, 70, 255)
YELLOW = (255, 255, 0)
LIGHT_YELLOW = (255, 255, 70)
GREEN = (0, 255, 0)
LIGHT_GREEN = (70, 255, 70)


def place_aval_circle(x, y):
    """
    Проверяет находится ли (x, y) на расстоянии R от любого препятствия
    Args:
        x: x-координата
        y: y-координата

    Returns: False, если находится хоть в каком-то, иначе True

    """
    for c in circles:
        if (c.x - x) ** 2 + (c.y - y) ** 2 <= (c.r + R) ** 2:
            return False
    return True


def place_aval_soldier(x, y):
    """
    Проверяет находится ли (x, y) на расстоянии R от любого солдата
    Args:
        x: x-координата
        y: y-координата

    Returns: False, если находится хоть в каком-то, иначе True

    """
    if not soldiers == []:
        for s in soldiers:
            if (s.x - x) ** 2 + (s.y - y) ** 2 <= 4 * R ** 2:
                return False
    return True


def place_aval_zone(zone, x, y):
    """
    Проверяет находится ли (x, y) в допустимой зоне
    Args:
        zone: - зона проверки
        x: x-координата
        y: y-координата

    Returns: True, если допистимая зона, False, иначе

    """
    return zone.collidepoint(x, y)


def place_soldier(x, y, screen, n):
    if n % 2 == 1:
        s = Soldier(x, y, 'Blue', screen, n // 2 + 1)
        soldiers.append(s)
    elif n % 2 == 0:
        s = Soldier(x, y, 'Red', screen, n // 2 + 1)
        soldiers.append(s)


def blue_team_alive():
    """
    Проверяет победу красных
    Returns:  False - синие мертвы, победа красных, True - иначе

    """
    for s in soldiers:
        if s.team == 'Blue' and s.alive:
            return True
        else:
            return False


def red_team_alive():
    """
    Проверяет победу синих
    Returns:  False - красные мертвы, победа синих, True - иначе

    """
    for s in soldiers:
        if s.team == 'Red' and s.alive:
            return True
        else:
            return False


def lamp(screen, team):
    """
    Создаёт лампу, котороя светится цветом ходящей комаеды
    Args:
        screen: экран отрисовки
        team: команда, которая ходит

    """
    if team == 'Red':
        pygame.draw.circle(screen, RED, LAMP_COORDS, LAMP_R)
        pygame.draw.circle(screen, LIGHT_RED, LAMP_COORDS, LAMP_R_I)
    elif team == 'Blue':
        pygame.draw.circle(screen, BLUE, LAMP_COORDS, LAMP_R)
        pygame.draw.circle(screen, LIGHT_BLUE, LAMP_COORDS, LAMP_R_I)


def lamp_soldier(screen, x, y, team):
    """
    Подсвечивает стреляющего солдата
    Args:
        screen: экран отрисовки
        x: x-координата лампы
        y: y-координата лампы
        team: команда лампы, определяет цвет

    """
    if team == 'Red':
        pygame.draw.circle(screen, YELLOW, (x, y), R)
        pygame.draw.circle(screen, LIGHT_YELLOW, (x, y), R_I)
    elif team == 'Blue':
        pygame.draw.circle(screen, GREEN, (x, y), R)
        pygame.draw.circle(screen, LIGHT_GREEN, (x, y), R_I)

def draw_screen_border(screen):
    pass
    pygame.draw.rect(screen, GREEN, (0))
