import pygame

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


class Window():

    def __init__():
        screen 

    def Game_window():
        pygame.draw.rect(screen,WHITE,[20,20,1040,700])

 
    def History_window(event):
        History_rect = pygame.draw.rect(screen,WHITE,[650,750,400,100])
        if History_rect.collidepoint(event.pos):
            if event.y == 1:
                x += 1
            if event.y == -1:
                x -= 1
        with open('History.txt', 'r') as History:
            n = 0
            for line in History:
                n += 1 
                text_history = smallfont.render(line[:-2], True, BLACK)
                screen.blit(text_history, (670,750 + 24*n))
                if n > 5:
                    break



                

    def Input_window(formula, event):
        pygame.draw.rect(screen, color, input_rect, 2)
        if len(formula) == 0:
            x = 0
        else:
            width = 32
            maxlen = 14
            if len(formula) < maxlen:
                text_surface = base_font.render(formula, True, BLACK)
                screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
            else:
                text_surface = base_font.render(formula[-maxlen-x:x], True, BLACK)
                screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
            if event == pygame.K_LEFT and x != 0:
                x -= 1
            elif event == pygame.K_RIGHT and x != len(formula):
                x += 1


        return formula 



class Button():


    def Fire_button(mouse):
        # if mouse is hovered on a button it 
        # changes to lighter shade 
        if 300 <= mouse[0] <= 400 and 800 <= mouse[1] <= 850: 
            pygame.draw.rect(screen,BLACK,[300,800,100,50]) 
        else: 
            pygame.draw.rect(screen,DARK,[300,800,100,50])
        screen.blit(text_fire, (330,800))  


    def Quit_button(mouse):
        # if mouse is hovered on a button it 
        # changes to lighter shade 
        if 500 <= mouse[0] <= 600 and 800 <= mouse[1] <= 850: 
            pygame.draw.rect(screen,BLACK,[500,800,100,50]) 
        else: 
            pygame.draw.rect(screen,DARK,[500,800,100,50])
        # superimposing the text onto our button 
        screen.blit(text_quit, (525,800)) 
     
    def Click(event, mouse, formula):
        if 50 <= mouse[0] <= 150 and 20 <= mouse[1] <= 40:
            print('I am  here')
            with open('History.txt', 'w') as History:
                History.write(formula)
            global active
            active = False
        if 500 <= mouse[0] <= 600 and 800 <= mouse[1] <= 850:
            pygame.quit()

