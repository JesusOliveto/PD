import pygame
import time
import math
import json


clock = pygame.time.Clock()

Aux = {
    'auxa' : 0.0,
    'auxb' : 0.0,
    'auxc' : 0.0,
    'auxd' : 0.0,
    'auxk' : 0.0,
    'auxw' : 0.0,
}

data = {
    "deltaR" : 0.0,
    'r': 0.0,
    'A': 0.0,
    'a': 1.0,
    'b': 1.0,
    'c': 1.0,
    'd': 1.0,
    'k': 1.0,
    'w': 1.0,
    'costa': 100,
    'costb': 500,
    'costc': 1000,
    'costd': 10000,
    'costk': 10,
}

black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
grey=(128,128,128)
display_width=800
display_height=600

#display
gameDisplay=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("mierder clicker v0.1.2")


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
    data["r"]= (data["r"] + data["A"] *data["w"]+ data["k"])
    data["A"]= round(data["A"],5)
    #print("r=",r)
    clock.tick(30)
    data["deltaR"]= (data["A"]* data["w"] +data["k"]) *30


        
def getAuxa():
    Aux["auxa"]=0
    r= data["r"]
    costa= data["costa"]
    while r >= costa:
        Aux["auxa"]= Aux["auxa"] + 1
        r= r - costa
        costa= costa * 1.05


def getAuxb():
    Aux["auxb"]=0
    r= data["r"]
    costb= data["costb"]
    while r >= costb:
        Aux["auxb"]= Aux["auxb"] + 1
        r= r - costb
        costb= costb * 1.05

def getAuxc():
    Aux["auxc"]=0
    r= data["r"]
    costc= data["costc"]
    while r >= costc:
        Aux["auxc"]= Aux["auxc"] + 1
        r= r - costc
        costc= costc * 1.05

def getAuxd():
    Aux["auxd"]=0
    r= data["r"]
    costd= data["costd"]
    while r >= costd:
        Aux["auxd"]= Aux["auxd"] + 1
        r= r - costd
        costd= costd * 1.05
        
def getAuxk():
    Aux["auxk"]=0
    r= data["r"]
    costk= data["costk"]
    while r >= costk:
        Aux["auxk"]= Aux["auxk"] + 1
        r= r - costk
        costk= costk * 1.05

def getAuxw():
    
    Aux["auxw"]= (data["a"]+data["b"]+data["c"]+data["d"])/10
    Aux["auxw"]= int(Aux["auxw"]//1)

def saveGame():
    with open("savegame.txt", "w") as save_file:
        json.dump(data, save_file)
    with open("var.txt", "w") as var_file:
        json.dump(Aux, var_file)


def prestige():
    data["r"]=0
    data["a"]=1
    data["b"]=1
    data["c"]=1
    data["d"]=1
    data["k"]=1
    data["costa"]=100
    data["costb"]=500
    data["costc"]=1000
    data["costd"]=10000
    data["costk"]=10
    data["w"]= data["w"]+ Aux["auxw"]