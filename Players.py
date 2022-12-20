from Objects import circles
from Soldiers import Soldier, soldiers


def place_aval(x, y, h_min, h_max, w_min, w_max):
    objects = circles + soldiers

    for o in objects:
        if (o.x - x) ** 2 + (o.y - y) ** 2 <= o.r ** 2 or x < w_min or x > w_max or y < h_min or y > h_max:
            return False
        else:
            return True


def place_soldier(x, y, team, screen, n):
    if team == 'Blue':
        s = Soldier(x, y, 'Blue', screen, n)
        soldiers.append(s)
    elif team == 'Red':
        s = Soldier(x, y, 'Blue', screen, n)
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
