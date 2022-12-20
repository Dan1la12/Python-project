import pygame
import sys
import classes
from Objects import Circle, circles, obj_generate
from Players import place_aval_circle, place_aval_soldier, place_aval_zone
from Soldiers import PlaceCircle, soldiers, R, Soldier

pygame.init()
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
DARK = (100, 100, 100)
BLACK = (0, 0, 0)
COLORS = [WHITE, RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN, DARK, BLACK]

clock = pygame.time.Clock()
screen = pygame.display.set_mode((1080, 880))
base_font = pygame.font.Font(None, 32)

soldiers_count = 0
input_rect = pygame.Rect(300, 750, 200, 30)
game_rect = pygame.Rect(20, 20, 1040, 700)
red_place_rect = pygame.Rect(20 + R, 20 + R, 520 - R, 700 - 2*R)
blue_place_rect = pygame.Rect(520 + R, 20 + R, 520 - R, 700 - 2*R)

color_active = pygame.Color('lightskyblue3')
color_passive = pygame.Color('gray15')
color = color_passive

active = False

# defining a font 
smallfont = pygame.font.SysFont('Corbel', 35)

text_quit = smallfont.render('Quit', True, WHITE)
text_fire = smallfont.render('Fire', True, WHITE)
ps = PlaceCircle(screen, 'Red', 0, 0)
o1 = Circle(screen, 300, 300, 50)
circles.append(o1)
# test_dead_body = Soldier(500, 500, 'Red', screen, 2)
# test_dead_body.hit()
is_game = False
turn_number = 0


def execution():
    user_formula = ''
    while True:
        screen = pygame.display.set_mode((1080, 880))
        screen.fill(GREEN)
        game_window = classes.Window(screen, game_rect, base_font, None)
        game_window.Game_window()
        mousepos = pygame.mouse.get_pos()
        global is_game
        for ev in pygame.event.get():
            global soldiers_count
            x, y = mousepos
            if soldiers_count < 10 and soldiers_count % 2 == 1:
                if place_aval_circle(x, y) and place_aval_soldier(x, y) and place_aval_zone(blue_place_rect, x, y):
                    global ps
                    if ev.type == pygame.MOUSEBUTTONDOWN:
                        team = 'Blue'
                        Soldier(x, y, team, screen, soldiers_count // 2 + 1)
                        soldiers_count += 1
                        ps = PlaceCircle(screen, 'Red', x, y)
                    ps.move(x, y)
                    ps.draw()

            elif soldiers_count < 10 and soldiers_count % 2 == 0:
                if place_aval_circle(x, y) and place_aval_soldier(x, y) and place_aval_zone(red_place_rect, x, y):
                    if ev.type == pygame.MOUSEBUTTONDOWN:
                        team = 'Red'
                        Soldier(x, y, team, screen, soldiers_count // 2 + 1)
                        soldiers_count += 1
                        ps = PlaceCircle(screen, 'Blue', x, y)
                    ps.move(x, y)
                    ps.draw()
            else:
                if not is_game:
                    is_game = True

            if ev.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # checks if a mouse is clicked
            global active
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(mousepos[0], mousepos[1]):
                    active = True
                    inputstr = classes.Window(screen, input_rect, base_font, None)
                else:
                    active = False
                    inputstr = classes.Window(screen, input_rect, base_font, None)

                inputstr.Input_window(user_formula)


                quit = classes.Button(screen, [500, 800, 100, 50], smallfont, mousepos, ev)
                quit.Quit_button()
                '''
                if input_rect.collidepoint(ev.pos):
                    global active
                    active = True
                '''
            if ev.type == pygame.KEYDOWN:
                if active:
                    if ev.key == pygame.K_BACKSPACE:
                        user_formula = user_formula[:-1]
                    else:
                        user_formula += ev.unicode

        if is_game:
            global turn_number

        history = classes.Window(screen, None, base_font, None)
        history.History_window()

        inputstr = classes.Window(screen, input_rect, base_font, None)
        inputstr.Input_window(user_formula)
        for s in soldiers:
            s.draw()
        for c in circles:
            c.draw()
        quit = classes.Button(screen, [500, 800, 100, 50], smallfont, mousepos, None)
        quit.Quit_button()
        fire = classes.Button(screen, [300, 800, 100, 50], smallfont, mousepos, None)
        fire.Fire_button()

        pygame.display.flip()
        clock.tick(60)
