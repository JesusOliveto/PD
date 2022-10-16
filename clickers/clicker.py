#imports
import pygame
import time
import math

pygame.init()

#variables

clock = pygame.time.Clock()
deltaR = 0.0
r=0.0
A=0.0
a=1.0
b=1.0
c=1.0
d=1.0
k=1.0
black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
grey=(128,128,128)
display_width=800
display_height=600

#display
gameDisplay=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("mierder clicker v0.0.1")

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
    global deltaR
    A= (a*b*c*d)
    r= (r + A + k)
    A= round(A,5)
    #print("r=",r)
    clock.tick(30)
    deltaR= (A+k) *30


    
def main_loop():
    global r 
    global a 
    global b 
    global c
    global d
    global k
    global A
    costa=100
    costb=500
    costc=1000
    costd=10000
    costk=10
    
    game_running = True
    while game_running:
        if game_running: 
            rincrement()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mopos = pygame.mouse.get_pos()
                if mopos[0] > 300 and mopos[0] < 500 and mopos[1] > 100 and mopos[1] < 200:
                    if r >= costa:
                        #test buymax
                        aux= r/costa
                        aux=int(aux)
                        r= r - costa * aux
                        costa= costa * 1.05 * aux
                        a= a + 0.1 * aux
                        costa= round(costa,2)
                        a= round(a,2)
                        print("total a bought:",aux)
                        
                if mopos[0] > 300 and mopos[0] < 500 and mopos[1] > 300 and mopos[1] < 400:
                    if r >= costb:
                        aux= r/costb
                        aux=int(aux)
                        r= r - costb * aux
                        costb= costb * 1.1 * aux
                        b= b + 0.1 * aux
                        costb= round(costb,2)
                        b= round(b,2)
                        print("total b bought:",aux)
                if mopos[0] > 300 and mopos[0] < 500 and mopos[1] > 500 and mopos[1] < 600:
                    if r >= costc:
                        aux= r/costc
                        aux=int(aux)
                        r= r - costc * aux
                        costc= costc * 1.11 * aux
                        c= c + 0.1 * aux
                        costc= round(costc,2)
                        c= round(c,2)
                        print("total c bought:",aux)
                if mopos[0] > 600 and mopos[0] < 800 and mopos[1] > 100 and mopos[1] < 200:
                    if r >= costd:
                        aux= r/costd
                        aux=int(aux)
                        r= r - costd * aux
                        costd= costd * 1.12* aux
                        d= d + 0.1 * aux
                        costd= round(costd,2)
                        d= round(d,2)
                        print("total d bought:",aux)
                    
                if mopos[0] > 600 and mopos[0] < 800 and mopos[1] > 300 and mopos[1] < 400:
                    if r >= costk:
                        aux= r/costk
                        aux=int(aux)
                        r= r - costk * aux
                        costk= costk * 1.1 * aux
                        k= k + 1 * aux
                        costk= round(costk,2)
                        k= round(k,2)
                        print("total k bought:",aux)
        
        gameDisplay.fill(black)
        
        #grid de referencia
        for i in range(0, 900, 100):
            pygame.draw.line(gameDisplay, (255, 255, 255), (0, i), (900, i))
            pygame.draw.line(gameDisplay, (255, 255, 255), (i, 0), (i, 900))
            
        #info
        DrawText("r = " + str(f'{r:.2f}') , white, black, 100, 50, 20) 
        DrawText("deltaR = " + str(f'{deltaR:.2f}') , white, black, 100, 75, 20)
        rectangle(gameDisplay, grey, 0, 100, 200, 400)
        DrawText("r = A + k"  , white, black, 100, 110, 20)      
        DrawText("A= a*b*c*d"  , white, black, 100, 130, 20)
        
        #mejoras
        DrawText("a = " + str(a)  , white, black, 100, 150, 20)  
        DrawText("b = " + str(b)  , white, black, 100, 170, 20)
        DrawText("c = " + str(c)  , white, black, 100, 190, 20)
        DrawText("d = " + str(d)  , white, black, 100, 210, 20)
        DrawText("k = " + str(k)  , white, black, 100, 230, 20)
        DrawText("A = " + str(A)  , white, black, 100, 250, 20)
        
        #botones
        rectangle(gameDisplay, grey, 300, 100, 200, 100)
        DrawText("a+0.1 = " + str(costa)  , white, black, 400, 150, 20)
        DrawText("+" + str(int(r/costa))  , white, black, 400, 170, 20) 
        rectangle(gameDisplay, grey, 300, 300, 200, 100)
        DrawText("b+0.1 = " + str(costb)  , white, black, 400, 350, 20)
        DrawText("+" + str(int(r/costb))  , white, black, 400, 370, 20)
        rectangle(gameDisplay, grey, 300, 500, 200, 100)
        DrawText("c+0.1 = " + str(costc)  , white, black, 400, 550, 20)
        DrawText("+" + str(int(r/costc))  , white, black, 400, 570, 20)
        rectangle(gameDisplay, grey, 600, 100, 200, 100)
        DrawText("d+0.1 = " + str(costd)  , white, black, 700, 150, 20)
        DrawText("+" + str(int(r/costd))  , white, black, 700, 170, 20)
        rectangle(gameDisplay, grey, 600, 300, 200, 100)
        DrawText("k+1 = " + str(costk)  , white, black, 700, 350, 20)
        DrawText("+" + str(int(r/costk))  , white, black, 700, 370, 20)
        pygame.display.update()
        clock.tick(60)

main_loop()
pygame.quit()
quit()