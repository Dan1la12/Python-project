import pygame, sys
import classes

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

input_rect = pygame.Rect(300, 750, 200, 30)

color_active = pygame.Color('lightskyblue3') 
color_passive = pygame.Color('gray15')
color = color_passive

active = False

# defining a font 
smallfont = pygame.font.SysFont('Corbel',35) 

text_quit = smallfont.render('Quit', True, WHITE)
text_fire = smallfont.render('Fire', True, WHITE)


def execution():
    screen = pygame.display.set_mode((1080,880))

    user_formula = ''

    while True:
        
        mousepos = pygame.mouse.get_pos() 
        
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #checks if a mouse is clicked 
            if ev.type == pygame.MOUSEBUTTONDOWN:
                classes.Button.Click(ev, mousepos, user_formula)
                if input_rect.collidepoint(ev.pos):
                    global active
                    active = True
            if ev.type == pygame.KEYDOWN:
                if active == True:
                    if ev.key == pygame.K_BACKSPACE:
                        user_formula = user_formula[:-1]
                    else:
                        user_formula += ev.unicode
        screen.fill(GREEN)
        classes.Window.Game_window(screen)
        classes.Window.History_window(screen, None, base_font)
        classes.Window.Input_window(screen, BLACK, input_rect, user_formula, None, base_font)


        classes.Button.Quit_button(screen, mousepos, [500,800,100,50], smallfont)
        classes.Button.Fire_button(screen, mousepos, [300,800,100,50], smallfont)

        pygame.display.flip()
        clock.tick(60)
