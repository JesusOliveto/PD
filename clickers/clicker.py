#imports
from funciones import *

pygame.init()

#variables




try:
    with open ("savegame.txt") as save_file:
        data=json.load(save_file)
except:
    print("no file created yet")

try:
    with open ("var.txt") as var_file:
        Aux=json.load(var_file)


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
            getAuxw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                saveGame()
                game_running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mopos = pygame.mouse.get_pos()
                if mopos[0] > 300 and mopos[0] < 500 and mopos[1] > 100 and mopos[1] < 200:
                    if data["r"] >= data["costa"]:
                        for i in range(Aux["auxa"]):
                            if data["r"] >= data["costa"]:
                                data["a"] = data["a"] + 0.1
                                data["r"] = data["r"] - data["costa"]
                                data["costa"] = data["costa"] * 1.05
                                data["costa"] = round(data["costa"], 2)
                                data["a"] = round(data["a"], 2)
                        print("total a bought:",Aux["auxa"])
                        
                if mopos[0] > 300 and mopos[0] < 500 and mopos[1] > 300 and mopos[1] < 400:
                    if data["r"] >= data["costb"]:
                        for i in range(Aux["auxb"]):
                            data["r"]= data["r"] - data["costb"]
                            data["costb"]= data["costb"] * 1.05
                            data["b"]= data["b"] + 0.1
                            data["costb"]= round(data["costb"],2)
                            data["b"]= round(data["b"],2)
                        print("total b bought:",Aux["auxb"])
                if mopos[0] > 300 and mopos[0] < 500 and mopos[1] > 500 and mopos[1] < 600:
                    if data["r"] >= data["costc"]:
                        for i in range(Aux["auxc"]):
                            data["r"]= data["r"] - data["costc"]
                            data["costc"]= data["costc"] * 1.05
                            data["c"]= data["c"] + 0.1
                            data["costc"]= round(data["costc"],2)
                            data["c"]= round(data["c"],2)
                        print("total c bought:",Aux["auxc"])
                if mopos[0] > 600 and mopos[0] < 800 and mopos[1] > 100 and mopos[1] < 200:
                    if data["r"] >= data["costd"]:
                        for i in range(Aux["auxd"]):
                            data["r"]= data["r"] - data["costd"]
                            data["costd"]= data["costd"] * 1.05
                            data["d"]= data["d"] + 0.1
                            data["costd"]= round(data["costd"],2)
                            data["d"]= round(data["d"],2)
                        print("total d bought:",Aux["auxd"])
                    
                if mopos[0] > 600 and mopos[0] < 800 and mopos[1] > 300 and mopos[1] < 400:
                    if data["r"] >= data["costk"]:
                        for i in range(Aux["auxk"]):
                            if data["r"] >= data["costk"]:
                                data["r"]= data["r"] - data["costk"]
                                data["costk"]= data["costk"] * 1.05
                                data["k"]= data["k"] + 1
                                data["costk"]= round(data["costk"],2)
                                data["k"]= round(data["k"],2)
                        print("total k bought:",Aux["auxk"])
                if mopos[0] > 600 and mopos[0] < 800 and mopos[1] > 500 and mopos[1] < 600:
                    if Aux["auxw"] >= 1:
                        prestige()
                        print("prestige")
                    else:
                        print("como vas a prestigiar con 0, so tonto vo?")
        
        gameDisplay.fill(black)
        
        #grid de referencia
        for i in range(0, 900, 100):
            pygame.draw.line(gameDisplay, (255, 255, 255), (0, i), (900, i))
            pygame.draw.line(gameDisplay, (255, 255, 255), (i, 0), (i, 900))
            
        #info
        rectangle(gameDisplay, grey, 0, 0, 200, 400)
        DrawText("r = " + str(f'{data["r"]:.2f}') , white, black, 100, 50, 20) 
        DrawText("deltaR = " + str(f'{data["deltaR"]:.2f}') , white, black, 100, 75, 20)
        DrawText("r = w*A + k"  , white, black, 100, 110, 20)      
        DrawText("A= a*b*c*d"  , white, black, 100, 130, 20)
        
        #mejoras
        DrawText("a = " + str(data["a"])  , white, black, 100, 150, 20)  
        DrawText("b = " + str(data["b"])  , white, black, 100, 170, 20)
        DrawText("c = " + str(data["c"])  , white, black, 100, 190, 20)
        DrawText("d = " + str(data["d"])  , white, black, 100, 210, 20)
        DrawText("k = " + str(data["k"])  , white, black, 100, 230, 20)
        DrawText("A = " + str(data["A"])  , white, black, 100, 250, 20)
        DrawText("w = " + str(data["w"])  , white, black, 100, 270, 20)
        
        #botones
        rectangle(gameDisplay, grey, 300, 100, 200, 100)
        DrawText("a+0.1 = " + str(data["costa"])  , white, black, 400, 150, 20)
        DrawText("+" + str(int(Aux["auxa"]))  , white, black, 400, 170, 20) 
        rectangle(gameDisplay, grey, 300, 300, 200, 100)
        DrawText("b+0.1 = " + str(data["costb"])  , white, black, 400, 350, 20)
        DrawText("+" + str(int(Aux["auxb"]))  , white, black, 400, 370, 20)
        rectangle(gameDisplay, grey, 300, 500, 200, 100)
        DrawText("c+0.1 = " + str(data["costc"])  , white, black, 400, 550, 20)
        DrawText("+" + str(int(Aux["auxc"]))  , white, black, 400, 570, 20)
        rectangle(gameDisplay, grey, 600, 100, 200, 100)
        DrawText("d+0.1 = " + str(data["costd"])  , white, black, 700, 150, 20)
        DrawText("+" + str(int(Aux["auxd"]))  , white, black, 700, 170, 20)
        rectangle(gameDisplay, grey, 600, 300, 200, 100)
        DrawText("k+1 = " + str(data["costk"])  , white, black, 700, 350, 20)
        DrawText("+" + str(int(Aux["auxk"]))  , white, black, 700, 370, 20)
        rectangle(gameDisplay, grey, 600, 500, 200, 100)
        DrawText("PRESTIGE"  , white, black, 700, 550, 20)
        DrawText("W +" + str(int(Aux["auxw"]))  , white, black, 700, 570, 20)
        pygame.display.update()
        clock.tick(60)

main_loop()
pygame.quit()
quit()