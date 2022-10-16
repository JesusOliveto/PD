""" crear un juego incremental con python y pygame  similar a idle spiral """

#imports
import pygame
import time
import math

pygame.init()

#variables

clock = pygame.time.Clock()
r=0.0
A=0.0
a=0.0
b=0.0
c=0.0
d=0.0
k=1.0
black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
grey=(128,128,128)
display_width=800
display_height=600

#display
gameDisplay=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("inserte titulo aqui")

#funciones

def DrawText(text, Textcolor, Rectcolor, x, y, fsize):
    font = pygame.font.Font('freesansbold.ttf', fsize)
    text = font.render(text, True, Textcolor, Rectcolor)
    textRect = text.get_rect()
    textRect.center = (x, y)
    gameDisplay.blit(text, textRect)
 
 
def rectangle(display, color, x, y, w, h):
    pygame.draw.rect(display, color, (x, y, w, h))
    
def rincrement():
    global r
    global a 
    global b 
    global c
    global d
    global k
    global A 
    A= a*b*c*d+k
    r= r + A
    print("r=",r)
    clock.tick(5)


    
def main_loop():
    global r 
    global a 
    global b 
    global c
    global d
    global k
    global A
    costa=10
    costb=50
    costc=100
    costd=1000
    costk=1
    
    game_running = True
    while game_running:
        if game_running: 
            rincrement()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mopos = pygame.mouse.get_pos()
                if mopos[0] > 0 and mopos[0] < 100 and mopos[1] > 0 and mopos[1] < 100:
                    if r >= costa:
                        a=a+0.1
                        r=r-costa
                        costa=costa*1.1
        
        gameDisplay.fill(black)
        
        #grid de referencia
        for i in range(0, 900, 100):
            pygame.draw.line(gameDisplay, (255, 255, 255), (0, i), (900, i))
            pygame.draw.line(gameDisplay, (255, 255, 255), (i, 0), (i, 900))
            
        #info
        DrawText("r = " + str(f'{r:.2f}') , white, black, 100, 50, 20)  
        rectangle(gameDisplay, grey, 0, 100, 200, 400)
        DrawText("r = A + k"  , white, black, 100, 110, 20)      
        DrawText("A= a*b*c*d"  , white, black, 100, 130, 20)
        
        #mejoras
        DrawText("a+0.01 = " + str(costa)  , white, black, 100, 150, 20)  
        DrawText("b+0.01 = " + str(costb)  , white, black, 100, 170, 20)
        DrawText("c+0.01 = " + str(costc)  , white, black, 100, 190, 20)
        DrawText("d+0.01 = " + str(costd)  , white, black, 100, 210, 20)
        DrawText("k+1 = " + str(costk)  , white, black, 100, 230, 20)
        
        #botones
        rectangle(gameDisplay, grey, 300, 100, 200, 100)
        rectangle(gameDisplay, grey, 300, 300, 200, 100)
        rectangle(gameDisplay, grey, 300, 500, 200, 100)
        rectangle(gameDisplay, grey, 600, 100, 200, 100)
        rectangle(gameDisplay, grey, 600, 300, 200, 100)
        pygame.display.update()
        clock.tick(60)

main_loop()
pygame.quit()
quit()