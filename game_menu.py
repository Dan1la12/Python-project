import pygame
import sys
import classes
from Objects import Circle, circles, obj_generate, white_circles
from Players import place_aval_circle, place_aval_soldier, place_aval_zone, lamp, lamp_soldier, blue_team_alive, red_team_alive
from Soldiers import PlaceCircle, soldiers, R, Soldier
from graph_creator import Marker, markers, lines, graph_evaluate

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
L_MAX_SQ = 200000
current_length_sq = 0
current_x = 0

clock = pygame.time.Clock()
screen = pygame.display.set_mode((1080, 880))
base_font = pygame.font.Font(None, 32)

soldiers_count = 0
input_rect = pygame.Rect(300, 750, 200, 30)
game_rect = pygame.Rect(20, 20, 1040, 700)
red_place_rect = pygame.Rect(20 + R, 20 + R, 520 - R, 700 - 2 * R)
blue_place_rect = pygame.Rect(520 + R, 20 + R, 520 - R, 700 - 2 * R)
marker_rect = pygame.Rect(20, 20, 1040, 700)

color_active = pygame.Color('lightskyblue3')
color_passive = pygame.Color('gray15')
color = color_passive

active = False

# defining a font
smallfont = pygame.font.SysFont('Corbel', 35)

text_quit = smallfont.render('Quit', True, WHITE)
text_fire = smallfont.render('Fire', True, WHITE)
ps = PlaceCircle(screen, 'Red', 0, 0)
obj_generated = False
is_game = False
find_red_soldier = True
find_blue_soldier = False
red_turn_number = 0
blue_turn_number = 0
x_fire = 0
y_fire = 0
n_fire = 100
team_fire = ''
is_Fire = False
dx = 2

def execution():
    user_formula = ''
    while True:
        screen = pygame.display.set_mode((1080, 880))
        screen.fill(GREEN)
        game_window = classes.Window(screen, game_rect, base_font, None)
        game_window.Game_window()
        mousepos = pygame.mouse.get_pos()
        for c in circles:  # отрисовка препятствий
            c.draw()
        global obj_generated
        if not obj_generated:
            obj_generate(screen)
            obj_generated = True
        global is_game  # показывает началась игра, или нет
        for ev in pygame.event.get():
            global soldiers_count
            x, y = mousepos
            if soldiers_count < 10 and soldiers_count % 2 == 1:
                """
                Проверяет сколько солдат поставлено и при нажатии мыши ставит синего солдата, 
                если их нечетное количество, показывает, куда можно поставить солдата
                """
                if place_aval_circle(x, y) and place_aval_soldier(x, y) and place_aval_zone(blue_place_rect, x, y):
                    global ps
                    if ev.type == pygame.MOUSEBUTTONDOWN:
                        team = 'Blue'
                        Soldier(x, y, team, screen, soldiers_count // 2)
                        soldiers_count += 1
                        ps = PlaceCircle(screen, 'Red', x, y)
                    ps.move(x, y)
                    ps.draw()

            elif soldiers_count < 10 and soldiers_count % 2 == 0:
                """
                Проверяет сколько солдат поставлено и при нажатии мыши ставит красного солдата, 
                если их четное количество, показывает, куда можно поставить солдата
                """
                if place_aval_circle(x, y) and place_aval_soldier(x, y) and place_aval_zone(red_place_rect, x, y):
                    if ev.type == pygame.MOUSEBUTTONDOWN:
                        team = 'Red'
                        Soldier(x, y, team, screen, soldiers_count // 2)
                        soldiers_count += 1
                        ps = PlaceCircle(screen, 'Blue', x, y)
                    ps.move(x, y)
                    ps.draw()
            else:
                """
                если солдат 10, начинает игру
                """
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
                fire = classes.Button(screen, [300, 800, 100, 50], smallfont, mousepos, ev)
                if fire.Fire_button():
                    global is_Fire
                    is_Fire = fire.Fire_button()[0]
                    active = fire.Fire_button()[1]

                quit = classes.Button(screen, [500, 800, 100, 50], smallfont, mousepos, ev)
                quit.Quit_button()

            if ev.type == pygame.KEYDOWN:
                if active:
                    if ev.key == pygame.K_BACKSPACE:
                        user_formula = user_formula[:-1]
                    else:
                        user_formula += ev.unicode

        global find_red_soldier, find_blue_soldier, blue_turn_number, red_turn_number, x_fire, y_fire, n_fire, \
            team_fire, current_length_sq, current_x
        """
        Глобальные переменные для запуска игры
        find_red_soldier - выбирается ли красный солдат для стрельбы ()
        find_blue_soldier - выбирается ли синий солдат для стрельбы
        blue_turn_number - номер "хода" синих, если солдат с таким номером мертв, сдвигается
        red_turn_number - номер "хода" красных, если солдат с таким номером мертв, сдвигается
        x_fire - x-координата стреляющего солдата
        y_fire - y-координата стреляющего солдата
        n_fire - номер стреляющего солдата 
        team_fire - команда, которая стреляет
        current_length_sq - текущий квардра длины графика (не превосходит L_MAX_SQ)
        current_x - текущая x - координата отрисовки, задает через graph_evaluate current_y
        is_Fire - ведется ли отрисовка графика
        """
        if is_game:
            if find_red_soldier:  # выбирает красного солдата, который будет стрелять
                if not active:
                    active = True
                for s in soldiers:
                    if s.number == red_turn_number and s.team == 'Red' and s.alive:
                        x_fire = s.x
                        y_fire = s.y
                        n_fire = s.number
                        team_fire = 'Red'
                        find_red_soldier = False
                red_turn_number += 1
                red_turn_number %= 5
            if find_blue_soldier:
                if not active:  # выбирает синего солдата, который будет стрелять
                    active = True
                for s in soldiers:
                    if s.number == red_turn_number and s.team == 'Blue' and s.alive:
                        x_fire = s.x
                        y_fire = s.y
                        n_fire = s.number
                        team_fire = 'Blue'
                        find_blue_soldier = False
                blue_turn_number += 1
                blue_turn_number %= 5
            if team_fire == 'Red' and is_Fire:
                active = False  # не даёт менять ввод функции во время отрисовки
                if not markers:  # создает маркер, если его нет
                    Marker(x_fire, y_fire, team_fire, screen)
                for m in markers:  # вызывает функции маркера
                    m.soldier_hit_check(n_fire, team_fire)
                    if current_length_sq < L_MAX_SQ:
                        current_x += dx
                        if graph_evaluate(current_x, user_formula) != 'err':
                            current_y = graph_evaluate(current_x, user_formula) * -1
                            current_length_sq += float(m.move(x_fire + current_x, y_fire + current_y))
                        else:
                            current_length_sq = L_MAX_SQ  # для прекращения действия
                        if m.circle_check_hit(screen):
                            m.circle_check_hit(screen)
                            current_length_sq = L_MAX_SQ  # для прекращения действия
                        if not place_aval_zone(marker_rect, m.x, m.y):
                            current_length_sq = L_MAX_SQ
                    elif current_length_sq >= L_MAX_SQ:  # прекращает действие маркера
                        markers.remove(m)
                        is_Fire = False
                        find_blue_soldier = True
                        current_length_sq = 0
                        current_x = 0
                        for l in lines:
                            if l.active:
                                l.deactivate()
            if team_fire == 'Blue' and is_Fire:
                active = False
                if not markers:
                    Marker(x_fire, y_fire, team_fire, screen)
                for m in markers:
                    m.soldier_hit_check(n_fire, team_fire)
                    if current_length_sq < L_MAX_SQ:
                        current_x -= dx
                        if graph_evaluate(current_x, user_formula) != 'err':
                            current_y = graph_evaluate(current_x, user_formula) * -1
                            current_length_sq += float(m.move(x_fire + current_x, y_fire + current_y))
                        else:
                            current_length_sq = L_MAX_SQ
                        if m.circle_check_hit(screen):
                            m.circle_check_hit(screen)
                            current_length_sq = L_MAX_SQ
                        if not place_aval_zone(marker_rect, m.x, m.y):
                            current_length_sq = L_MAX_SQ
                    elif current_length_sq >= L_MAX_SQ:
                        markers.remove(m)
                        is_Fire = False
                        find_red_soldier = True
                        current_length_sq = 0
                        current_x = 0
                        for l in lines:
                            if l.active:
                                l.deactivate()

        for wc in white_circles:
            wc.draw()
        for l in lines:
            l.draw()
        for s in soldiers:  # отрисовка солдат
            s.draw()
        lamp(screen, team_fire)  # отрисовка ламп
        lamp_soldier(screen, x_fire, y_fire, team_fire)
        for m in markers:
            m.draw()

        pygame.draw.rect(screen, GREEN, [0, 0, 1080, 20])
        pygame.draw.rect(screen, GREEN, [0, 0, 20, 720])
        pygame.draw.rect(screen, GREEN, [1060, 20, 20, 700])
        pygame.draw.rect(screen, GREEN, [0, 720, 1080, 400])

        inputstr = classes.Window(screen, input_rect, base_font, None)
        inputstr.Input_window(user_formula)


        quit = classes.Button(screen, [500, 800, 100, 50], smallfont, mousepos, None)
        quit.Quit_button()
        fire = classes.Button(screen, [300, 800, 100, 50], smallfont, mousepos, None)
        fire.Fire_button()

        pygame.display.flip()
        clock.tick(60)
