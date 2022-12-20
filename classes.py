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

    def Game_window(screen, rect):
        game_window = pygame.draw.rect(screen,WHITE,rect)
        return game_window

 
    def History_window(screen, event, font):
        history_rect =  pygame.draw.rect(screen,WHITE,[650,750,400,100])
        if event != None:
            if event.y == 1:
                x += 1
            if event.y == -1:
                x -= 1
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
                text_history = font.render(line[:-2], True, BLACK)
                screen.blit(text_history, (670,750 + 24*n))
                if n > 5:
                    break



                

    def Input_window(screen, color, input_rect, formula, event, font):
        pygame.draw.rect(screen, color, input_rect, 2)
        if len(formula) == 0:
            x = 0
        else:
            maxlen = 14
            if len(formula) < maxlen:
                text_surface = font.render(formula, True, BLACK)
                screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
            else:
                text_surface = font.render(formula[-maxlen-x:x], True, BLACK)
                screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
            if event == None:
                pass
            elif event == pygame.K_LEFT and x != 0:
                x -= 1
            elif event == pygame.K_RIGHT and x != len(formula):
                x += 1


        return formula 



class Button:
    def Play_button(screen, event, mouse, rect, font):
        # if mouse is hovered on a button it 
        # changes to lighter shade 
        text_play = font.render('Play', True, WHITE)
        if 150 <= mouse[0] <= 250 and 150 <= mouse[1] <= 200: 
            pygame.draw.rect(screen,BLACK,rect)
            if event != None:
                global Exit 
                Exit = True
                game.execution()
                return Exit
        else: 
            pygame.draw.rect(screen,DARK,rect)
        screen.blit(text_play, (rect[0] + 25,rect[1]))


    def Fire_button(screen, mouse, rect, font):
        # if mouse is hovered on a button it 
        # changes to lighter shade 
        text_fire = font.render('Fire', True, WHITE)
        if 300 <= mouse[0] <= 400 and 800 <= mouse[1] <= 850: 
            pygame.draw.rect(screen,BLACK,rect) 
        else: 
            pygame.draw.rect(screen,DARK,rect)
        screen.blit(text_fire, (rect[0] + 30,rect[1]))  


    def Quit_button(screen, mouse, rect, font):
        # if mouse is hovered on a button it 
        # changes to lighter shade 
        text_quit = font.render('Quit', True, WHITE)
        if 500 <= mouse[0] <= 600 and 800 <= mouse[1] <= 850: 
            pygame.draw.rect(screen,BLACK,rect) 
        else: 
            pygame.draw.rect(screen,DARK,rect)
        # superimposing the text onto our button 
        screen.blit(text_quit, (rect[0]+25,rect[1])) 
     
    def Click(event, mouse, formula):
        if 500 <= mouse[0] <= 600 and 800 <= mouse[1] <= 850:
            pygame.quit()

