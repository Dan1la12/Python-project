import pygame, sys

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


input_rect = pygame.Rect(300, 750, 100, 30)
color_active = pygame.Color('lightskyblue3') 
color_passive = pygame.Color('gray15')
color = color_passive

active = False

# defining a font 
smallfont = pygame.font.SysFont('Corbel',35) 

text_quit = smallfont.render('Quit', True, WHITE)
text_fire = smallfont.render('Fire', True, WHITE)

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
     
    def Click(event, mouse):
        if 50 <= mouse[0] <= 150 and 20 <= mouse[1] <= 40:
            global active
            active = False
        print(mouse)
        if 500 <= mouse[0] <= 600 and 800 <= mouse[1] <= 850:
            pygame.quit()
        

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
                Button.Click(ev, mousepos)
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
        pygame.draw.rect(screen,WHITE,[20,20,1040,700])

        pygame.draw.rect(screen, color, input_rect, 2)
        text_surface = base_font.render(user_formula, True, (255, 255, 255))
        screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))

        input_rect.w = max(100, text_surface.get_width() + 10)

        Button.Quit_button(mousepos)
        Button.Fire_button(mousepos)

        pygame.display.flip()
        clock.tick(60)
