import pygame, sys
import classes
from Players import place_aval, place_soldier
from Soldiers import PlaceCircle, soldiers, R, Soldier
from Objects import Circle, circles
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
screen = pygame.display.set_mode((1080,880))
base_font = pygame.font.Font(None, 32)

soldiers_count = 0
input_rect = pygame.Rect(300, 750, 200, 30)
game_rect = pygame.Rect(20, 20, 1040, 700)
plays_rect = pygame.Rect(20 + R, 20 + R, 1040 - 2 * R, 700 - 2 * R)


color_active = pygame.Color('lightskyblue3') 
color_passive = pygame.Color('gray15')
color = color_passive

active = False

# defining a font 
smallfont = pygame.font.SysFont('Corbel',35) 

text_quit = smallfont.render('Quit', True, WHITE)
text_fire = smallfont.render('Fire', True, WHITE)

ps = PlaceCircle(screen, 'Red', 0, 0)
o1 = Circle(screen,300, 300, 50)
circles.append(o1)
def execution():

    user_formula = ''

    while True:
        screen = pygame.display.set_mode((1080,880))
        screen.fill(GREEN)
        classes.Window.Game_window(screen, game_rect)
        mousepos = pygame.mouse.get_pos() 
        o1.draw()
        '''
        if place_aval(mousepos[0], mousepos[1]) and plays_rect.collidepoint(mousepos[0], mousepos[1]):
            if ev == pygame.MOUSEBUTTONDOWN:

            #and classes.Window.Game_window(screen).collidepoint(ev.pos)
            ps.draw()
            ps.move(mousepos[0], mousepos[1])
            #soldiers_count += 1
            '''



        for ev in pygame.event.get():
            
            if place_aval(mousepos[0], mousepos[1]) and plays_rect.collidepoint(mousepos[0], mousepos[1]):
                if ev.type == pygame.MOUSEBUTTONDOWN:
                    print('Click')
                    if soldiers_count % 2 == 1:
                        team = 'Blue'
                    else:
                        team = 'Red'
                    s = Soldier(mousepos[0], mousepos[1], team, screen, soldiers_count//2 + 1)
                    soldiers.append(s)
                    soldiers_count += 1
                    
                #and classes.Window.Game_window(screen).collidepoint(ev.pos)
                ps.draw()
                ps.move(mousepos[0], mousepos[1])
            for s in soldiers:
                s.draw()
                #soldiers_count += 1
            if ev.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #checks if a mouse is clicked 
            if ev.type == pygame.MOUSEBUTTONDOWN:
                classes.Button.Click(ev, mousepos, user_formula)
                '''
                if input_rect.collidepoint(ev.pos):
                    global active
                    active = True
                '''
            if ev.type == pygame.KEYDOWN:
                if active == True:
                    if ev.key == pygame.K_BACKSPACE:
                        user_formula = user_formula[:-1]
                    else:
                        user_formula += ev.unicode
        
        classes.Window.History_window(screen, None, base_font)
        classes.Window.Input_window(screen, BLACK, input_rect, user_formula, None, base_font)


        classes.Button.Quit_button(screen, mousepos, [500,800,100,50], smallfont)
        classes.Button.Fire_button(screen, mousepos, [300,800,100,50], smallfont)

        pygame.display.flip()
        clock.tick(60)
