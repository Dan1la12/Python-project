from Objects import circles
from Soldiers import Soldier, soldiers, R


def place_aval(x, y):
    objects = circles + soldiers

    for o in objects:
        if (o.x - x) ** 2 + (o.y - y) ** 2 <= (o.r + R) ** 2:
            return False
        else:
            return True


def place_soldier(x, y, screen, n):
    if n%2 == 1:
        s = Soldier(x, y, 'Blue', screen, n//2+1)
        soldiers.append(s)
    elif n%2 ==0:
        s = Soldier(x, y, 'Red', screen, n//2+1)
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
