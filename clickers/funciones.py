import pygame
import time
import math
import json
import data_


clock = pygame.time.Clock()



black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
grey=(128,128,128)
display_width=800
display_height=600

#display
gameDisplay=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("mierder clicker v0.1.2")


def loadGame():
    try:
        with open ("savegame.txt") as save_file:
            data_.data=json.load(save_file)
    except:
        print("no file created yet")

    try:
        with open ("var.txt") as var_file:
            data_.Aux=json.load(var_file)
    except:
        print("no file created yet")
    
    print("data_.data LOADED: ", data_.data)


def DrawText(text, Textcolor, Rectcolor, x, y, fsize):
    font = pygame.font.Font('freesansbold.ttf', fsize)
    text = font.render(text, True, Textcolor, Rectcolor)
    textRect = text.get_rect()
    textRect.center = (x, y)
    gameDisplay.blit(text, textRect)
 
 
def rectangle(display, color, x, y, w, h):
    pygame.draw.rect(display, color, (x, y, w, h))
    
def rincrement():
    data_.data["A"]=(data_.data["a"]*data_.data["b"]*data_.data["c"]*data_.data["d"])
    data_.data["r"]= (data_.data["r"] + data_.data["A"] *data_.data["w"]+ data_.data["k"])
    data_.data["A"]= round(data_.data["A"],5)
    clock.tick(30)
    data_.data["deltaR"]= (data_.data["A"]* data_.data["w"] +data_.data["k"]) *30


        
def getAuxa():
    data_.Aux["auxa"]=0
    r= data_.data["r"]
    costa= data_.data["costa"]
    while r >= costa:
        data_.Aux["auxa"]= data_.Aux["auxa"] + 1
        r= r - costa
        costa= costa * 1.05


def getAuxb():
    data_.Aux["auxb"]=0
    r= data_.data["r"]
    costb= data_.data["costb"]
    while r >= costb:
        data_.Aux["auxb"]= data_.Aux["auxb"] + 1
        r= r - costb
        costb= costb * 1.05

def getAuxc():
    data_.Aux["auxc"]=0
    r= data_.data["r"]
    costc= data_.data["costc"]
    while r >= costc:
        data_.Aux["auxc"]= data_.Aux["auxc"] + 1
        r= r - costc
        costc= costc * 1.05

def getAuxd():
    data_.Aux["auxd"]=0
    r= data_.data["r"]
    costd= data_.data["costd"]
    while r >= costd:
        data_.Aux["auxd"]= data_.Aux["auxd"] + 1
        r= r - costd
        costd= costd * 1.05
        
def getAuxk():
    data_.Aux["auxk"]=0
    r= data_.data["r"]
    costk= data_.data["costk"]
    while r >= costk:
        data_.Aux["auxk"]= data_.Aux["auxk"] + 1
        r= r - costk
        costk= costk * 1.05

def getAuxw():
    
    data_.Aux["auxw"]= (data_.data["a"]+data_.data["b"]+data_.data["c"]+data_.data["d"])/10
    data_.Aux["auxw"]= int(data_.Aux["auxw"]//1)

def saveGame():
    try:
        with open("savegame.txt", "w") as save_file:
            json.dump(data_.data, save_file)
        with open("var.txt", "w") as var_file:
            json.dump(data_.Aux, var_file)
        print("data_.data SAVED: ", data_.data)
    except:
        print("NO SE GUARDÓ CULIAOOOOOOOOOOOOOOOOOOOOOOOOOO")

def prestige():
    data_.data["r"]=0
    data_.data["a"]=1
    data_.data["b"]=1
    data_.data["c"]=1
    data_.data["d"]=1
    data_.data["k"]=1
    data_.data["costa"]=100
    data_.data["costb"]=500
    data_.data["costc"]=1000
    data_.data["costd"]=10000
    data_.data["costk"]=10
    data_.data["w"]= data_.data["w"]+ data_.Aux["auxw"]