from Objects import circles
from Soldiers import Soldier, soldiers, R


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
        elif (c.x - x) ** 2 + (c.y - y) ** 2 <= (c.r + R) ** 2:
            pass  # без этого не работает
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
            elif (s.x - x) ** 2 + (s.y - y) ** 2 >= 4 * R ** 2:
                pass  # без этого не работает
    return True


def place_aval_zone(zone, x, y):
    return zone.collidepoint(x, y)


def place_soldier(x, y, screen, n):
    if n % 2 == 1:
        s = Soldier(x, y, 'Blue', screen, n // 2 + 1)
        soldiers.append(s)
    elif n % 2 == 0:
        s = Soldier(x, y, 'Red', screen, n // 2 + 1)
        soldiers.append(s)


def blue_alive():
    for s in soldiers:
        if s.team == 'Blue' and s.alive:
            return True
        else:
            return False


def red_alive():
    for s in soldiers:
        if s.team == 'Red' and s.alive:
            return True
        else:
            return False
