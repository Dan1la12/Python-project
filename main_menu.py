import pygame
import sys
import game_menu as game

pygame.init()

clock = pygame.time.Clock()

# defining a font 
base_font = pygame.font.Font(None, 32)

# defining a font 
smallfont = pygame.font.SysFont('Corbel',35) 

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

# rendering a text written in 
# this font 
text_quit = smallfont.render('Quit', True, WHITE)
text_play = smallfont.render('Play', True, WHITE)

global Exit
Exit = False

if not Exit:
    #screen recolution
    res = (360,480) 

    # opens up a window 
    screen = pygame.display.set_mode(res)


class Buttons():


    def Play_button(mouse):
        # if mouse is hovered on a button it 
        # changes to lighter shade 
        if 150 <= mouse[0] <= 250 and 150 <= mouse[1] <= 200: 
            pygame.draw.rect(screen,BLACK,[150,150,100,50])
        else: 
            pygame.draw.rect(screen,DARK,[150,150,100,50])
        screen.blit(text_play, (175,150))
        

    def Quit_button(mouse):
        # if mouse is hovered on a button it 
        # changes to lighter shade 
        if 150 <= mouse[0] <= 250 and 250 <= mouse[1] <= 300: 
            pygame.draw.rect(screen,BLACK,[150,250,100,50])
        else: 
            pygame.draw.rect(screen,DARK,[150,250,100,50])
        # superimposing the text onto our button 
        screen.blit(text_quit, (175,250))

    def Click(mouse):
        if 150 <= mouse[0] <= 250 and 150 <= mouse[1] <= 200: 
            global Exit 
            Exit = True
            game.execution()
        if 150 <= mouse[0] <= 250 and 250 <= mouse[1] <= 300:
            pygame.quit()
            sys.exit() 
        

def main():        
    while not Exit:
        
        mousepos = pygame.mouse.get_pos() 

        for ev in pygame.event.get(): 
            if ev.type == pygame.QUIT: 
                pygame.quit() 
            #checks if a mouse is clicked 
            if ev.type == pygame.MOUSEBUTTONDOWN:
                Buttons.Click(mousepos)
        
        # fills the screen with a color 
        screen.fill(GREEN) 
        
        Buttons.Quit_button(mousepos)
        Buttons.Play_button(mousepos)
        
        # updates the frames of the game 
        pygame.display.update()
        clock.tick(120)

main()
