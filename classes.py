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
        return game_window

    def History_window(self):
        history_rect = pygame.draw.rect(self.screen, WHITE, [650, 750, 400, 100])
        if self.event != None:
            if self.event.y == 1:
                x += 1
            if self.event.y == -1:
                x -= 1
        else:
            pass
        '''
        if history_rect.collidepoint():
            print('I am  here')
            with open('History.txt', 'w') as History:
                History.write(formula)
            global active
            active = False
            '''
        with open('History.txt', 'r') as History:
            n = 0
            for line in History:
                n += 1
                text_history = self.font.render(line[:-2], True, BLACK)
                self.screen.blit(text_history, (670, 750 + 24 * n))
                if n > 5:
                    break

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
