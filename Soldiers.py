class Soldier:


    def __init__(self, x, y, team):
        self.x = x
        self.y = y
        self.team = team
        self.screen = pygame.battle_screen
        if team == 'RED':
            pygame.draw.circle(screen, RED, (x, y), r)

        elif team == 'BLUE':
            pygame.draw.circle(screen, BLUE, (x, y), r)

    alive = True
    his_turn = False
    team = ''
    x = 0
    y = 0
    r = 10


BLUE = (0, 0, 255)
RED = (255, 0, 0)
