import pygame
import game_menu as game

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


class Window:

    def __init__(self, screen, rect, font, event):
        self.screen = screen
        self.rect = rect
        self.font = font
        self.event = None

    def Game_window(self):
        game_window = pygame.draw.rect(self.screen, WHITE, self.rect)
        SCALE = 50
        size = [self.rect[0] + self.rect[2] // SCALE, self.rect[1] + self.rect[3] // SCALE]
        for i in range(0, size[0]):
            pygame.draw.line(self.screen, BLACK, [i * SCALE, 0], [i * SCALE, size[1] * SCALE])
        for i in range(0, size[1]):
            pygame.draw.line(self.screen, BLACK, [0, i * SCALE], [size[0] * SCALE, i * SCALE])
        return game_window


    def Input_window(self, formula):
        pygame.draw.rect(self.screen, BLACK, self.rect, 2)
        maxlen = 14
        if len(formula) < maxlen:
            text_surface = self.font.render(formula, True, BLACK)
            self.screen.blit(text_surface, (self.rect.x + 5, self.rect.y + 5))
        else:
            text_surface = self.font.render(formula[-maxlen:], True, BLACK)
            self.screen.blit(text_surface, (self.rect.x + 5, self.rect.y + 5))
            '''    
            if event == None:
                pass
            elif event == pygame.K_LEFT and x != 0:
                x -= 1
            elif event == pygame.K_RIGHT and x != len(formula):
                x += 1
            '''

        return formula


class Button:

    def __init__(self, screen, rect, font, mouse, event):
        self.screen = screen
        self.rect = rect
        self.font = font
        self.mouse = mouse
        self.event = event


    def Play_button(self):
        # if mouse is hovered on a button it
        # changes to lighter shade
        text_play = self.font.render('Play', True, WHITE)
        if 150 <= self.mouse[0] <= 250 and 150 <= self.mouse[1] <= 200:
            pygame.draw.rect(self.screen, BLACK, self.rect)
            if self.event != None:
                global Exit
                Exit = True
                game.execution()
                return Exit
        else:
            pygame.draw.rect(self.screen, DARK, self.rect)
        self.screen.blit(text_play, (self.rect[0] + 25, self.rect[1]))

    def Fire_button(self):
        # if mouse is hovered on a button it
        # changes to lighter shade
        text_fire = self.font.render('Fire', True, WHITE)
        if 300 <= self.mouse[0] <= 400 and 800 <= self.mouse[1] <= 850:
            pygame.draw.rect(self.screen, BLACK, self.rect)
            global is_fire, active
            if self.event != None:
                is_Fire = True
                active = False
                return is_Fire, active
        else:
            pygame.draw.rect(self.screen, DARK, self.rect)
        self.screen.blit(text_fire, (self.rect[0] + 30, self.rect[1]))

    def Quit_button(self):
        # if mouse is hovered on a button it
        # changes to lighter shade
        if 500 <= self.mouse[0] <= 600 and 800 <= self.mouse[1] <= 850:
            pygame.draw.rect(self.screen, BLACK, self.rect)
            text_quit = self.font.render('Quit', True, WHITE)
            if self.event:
                pygame.quit()
        else:
            pygame.draw.rect(self.screen, DARK, self.rect)
            text_quit = self.font.render('Quit', True, WHITE)
        # superimposing the text onto our button 
        self.screen.blit(text_quit, (self.rect[0] + 25, self.rect[1]))
