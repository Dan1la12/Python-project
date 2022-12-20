import pygame
import sys
import classes
import game_menu as game

pygame.init()

clock = pygame.time.Clock()

# defining a font 
base_font = pygame.font.Font(None, 32)

# defining a font 
smallfont = pygame.font.SysFont('Corbel', 35)

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

global Exit
Exit = False

if not Exit:
    # screen recolution
    res = (360, 480)

    # opens up a window 
    screen = pygame.display.set_mode(res)


def main():
    while not Exit:

        mousepos = pygame.mouse.get_pos()

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                # checks if a mouse is clicked
            if ev.type == pygame.MOUSEBUTTONDOWN:
                classes.Button.Play_button(screen, ev, mousepos, [150, 150, 100, 50], smallfont)

        # fills the screen with a color 
        screen.fill(GREEN)

        classes.Button.Quit_button(screen, mousepos, [150, 250, 100, 50], smallfont)
        classes.Button.Play_button(screen, None, mousepos, [150, 150, 100, 50], smallfont)

        # updates the frames of the game 
        pygame.display.update()
        clock.tick(120)


main()
