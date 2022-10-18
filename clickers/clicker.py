#imports
import pygame
import time
import math
import json

pygame.init()

#variables

clock = pygame.time.Clock()

data = {
    "deltaR" : 0.0,
    'r': 0.0,
    'A': 0.0,
    'a': 1.0,
    'b': 1.0,
    'c': 1.0,
    'd': 1.0,
    'k': 1.0,
    'costa': 100,
    'costb': 500,
    'costc': 1000,
    'costd': 10000,
    'costk': 10,
}

try:
    with open ("savegame.txt") as save_file:
        data=json.load(save_file)
except:
    print("no file created yet")

global auxa
global auxb
global auxc
global auxd
global auxk

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
    data["A"]=(data["a"]*data["b"]*data["c"]*data["d"])
    data["r"]= (data["r"] + data["A"] + data["k"])
    data["A"]= round(data["A"],5)
    #print("r=",r)
    clock.tick(30)
    data["deltaR"]= (data["A"]+data["k"]) *30


        
def getAuxa():
    global auxa
    auxa=0
    r= data["r"]
    costa= data["costa"]
    while r >= costa:
        auxa= auxa + 1
        r= r - costa
        costa= costa * 1.05


def getAuxb():
    global auxb
    auxb=0
    r= data["r"]
    costb= data["costb"]
    while r >= costb:
        auxb= auxb + 1
        r= r - costb
        costb= costb * 1.05

def getAuxc():
    global auxc
    auxc=0
    r= data["r"]
    costc= data["costc"]
    while r >= costc:
        auxc= auxc + 1
        r= r - costc
        costc= costc * 1.05

def getAuxd():
    global auxd
    auxd=0
    r= data["r"]
    costd= data["costd"]
    while r >= costd:
        auxd= auxd + 1
        r= r - costd
        costd= costd * 1.05
        
def getAuxk():
    global auxk
    auxk=0
    r= data["r"]
    costk= data["costk"]
    while r >= costk:
        auxk= auxk + 1
        r= r - costk
        costk= costk * 1.05

def saveGame():
    with open("savegame.txt", "w") as save_file:
        json.dump(data, save_file)


#MAIN LOOP
def main_loop():
    game_running = True
    while game_running:
        if game_running: 
            rincrement()
            getAuxa()
            getAuxb()
            getAuxc()
            getAuxd()
            getAuxk()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                saveGame()
                game_running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mopos = pygame.mouse.get_pos()
                if mopos[0] > 300 and mopos[0] < 500 and mopos[1] > 100 and mopos[1] < 200:
                    if data["r"] >= data["costa"]:
                        global auxa
                        for i in range(auxa):
                            if data["r"] >= data["costa"]:
                                data["a"] = data["a"] + 0.1
                                data["r"] = data["r"] - data["costa"]
                                data["costa"] = data["costa"] * 1.05
                                data["costa"] = round(data["costa"], 2)
                                data["a"] = round(data["a"], 2)
                        print("total a bought:",auxa)
                        
                if mopos[0] > 300 and mopos[0] < 500 and mopos[1] > 300 and mopos[1] < 400:
                    if data["r"] >= data["costb"]:
                        global auxb
                        for i in range(auxb):
                            data["r"]= data["r"] - data["costb"]
                            data["costb"]= data["costb"] * 1.05
                            data["b"]= data["b"] + 0.1
                            data["costb"]= round(data["costb"],2)
                            data["b"]= round(data["b"],2)
                        print("total b bought:",auxb)
                if mopos[0] > 300 and mopos[0] < 500 and mopos[1] > 500 and mopos[1] < 600:
                    if data["r"] >= data["costc"]:
                        global auxc
                        for i in range(auxc):
                            data["r"]= data["r"] - data["costc"]
                            data["costc"]= data["costc"] * 1.05
                            data["c"]= data["c"] + 0.1
                            data["costc"]= round(data["costc"],2)
                            data["c"]= round(data["c"],2)
                        print("total c bought:",auxc)
                if mopos[0] > 600 and mopos[0] < 800 and mopos[1] > 100 and mopos[1] < 200:
                    if data["r"] >= data["costd"]:
                        global auxd
                        for i in range(auxd):
                            data["r"]= data["r"] - data["costd"]
                            data["costd"]= data["costd"] * 1.05
                            data["d"]= data["d"] + 0.1
                            data["costd"]= round(data["costd"],2)
                            data["d"]= round(data["d"],2)
                        print("total d bought:",auxd)
                    
                if mopos[0] > 600 and mopos[0] < 800 and mopos[1] > 300 and mopos[1] < 400:
                    if data["r"] >= data["costk"]:
                        global auxk
                        for i in range(auxk):
                            if data["r"] >= data["costk"]:
                                data["r"]= data["r"] - data["costk"]
                                data["costk"]= data["costk"] * 1.05
                                data["k"]= data["k"] + 1
                                data["costk"]= round(data["costk"],2)
                                data["k"]= round(data["k"],2)
                        print("total k bought:",auxk)
        
        gameDisplay.fill(black)
        
        #grid de referencia
        for i in range(0, 900, 100):
            pygame.draw.line(gameDisplay, (255, 255, 255), (0, i), (900, i))
            pygame.draw.line(gameDisplay, (255, 255, 255), (i, 0), (i, 900))
            
        #info
        rectangle(gameDisplay, grey, 0, 0, 200, 400)
        DrawText("r = " + str(f'{data["r"]:.2f}') , white, black, 100, 50, 20) 
        DrawText("deltaR = " + str(f'{data["deltaR"]:.2f}') , white, black, 100, 75, 20)
        DrawText("r = A + k"  , white, black, 100, 110, 20)      
        DrawText("A= a*b*c*d"  , white, black, 100, 130, 20)
        
        #mejoras
        DrawText("a = " + str(data["a"])  , white, black, 100, 150, 20)  
        DrawText("b = " + str(data["b"])  , white, black, 100, 170, 20)
        DrawText("c = " + str(data["c"])  , white, black, 100, 190, 20)
        DrawText("d = " + str(data["d"])  , white, black, 100, 210, 20)
        DrawText("k = " + str(data["k"])  , white, black, 100, 230, 20)
        DrawText("A = " + str(data["A"])  , white, black, 100, 250, 20)
        
        #botones
        rectangle(gameDisplay, grey, 300, 100, 200, 100)
        DrawText("a+0.1 = " + str(data["costa"])  , white, black, 400, 150, 20)
        DrawText("+" + str(int(auxa))  , white, black, 400, 170, 20) 
        rectangle(gameDisplay, grey, 300, 300, 200, 100)
        DrawText("b+0.1 = " + str(data["costb"])  , white, black, 400, 350, 20)
        DrawText("+" + str(int(auxb))  , white, black, 400, 370, 20)
        rectangle(gameDisplay, grey, 300, 500, 200, 100)
        DrawText("c+0.1 = " + str(data["costc"])  , white, black, 400, 550, 20)
        DrawText("+" + str(int(auxc))  , white, black, 400, 570, 20)
        rectangle(gameDisplay, grey, 600, 100, 200, 100)
        DrawText("d+0.1 = " + str(data["costd"])  , white, black, 700, 150, 20)
        DrawText("+" + str(int(auxd))  , white, black, 700, 170, 20)
        rectangle(gameDisplay, grey, 600, 300, 200, 100)
        DrawText("k+1 = " + str(data["costk"])  , white, black, 700, 350, 20)
        DrawText("+" + str(int(auxk))  , white, black, 700, 370, 20)
        pygame.display.update()
        clock.tick(60)

main_loop()
pygame.quit()
quit()