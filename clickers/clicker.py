#imports de las funciones y del bloque de datos
from funciones import *
import data_

pygame.init()

#variables que no uso xd
black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
grey=(128,128,128)
display_width=800
display_height=600
#display
gameDisplay=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("mierder clicker v4.20.69")


#MAIN LOOP
def main_loop():
    game_running = True
    #background
    bg_img = pygame.image.load('Images/bg.jpg')
    bg_img = pygame.transform.scale(bg_img,(800,600))
    gameDisplay.blit(bg_img,(0,0))
    #pantalla de carga
    DrawText("LOADING SAVEGAME", (255, 255, 0), (0, 0, 0), 400, 50, 50)
    DrawText("MSK Games", (255, 10, 10), (0, 0, 0), 400, 200, 20)
    pygame.display.update()
    loadGame()
    time.sleep(3)
    print("data_.data LOADED MAIN: ", data_.data)
    while game_running:
        if game_running:
            #hilos paralelos
            rincrement()
            getAuxa()
            getAuxb()
            getAuxc()
            getAuxd()
            getAuxk()
            getAuxw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #guardar el juego al cerrarlo
                saveGame()
                game_running = False
            #INCREMENTOS 
            if event.type == pygame.MOUSEBUTTONDOWN:
                #checkea posiciones para generar los botones y los eventos (cambiar a funciones cuando se pueda)
                mopos = pygame.mouse.get_pos()
                if mopos[0] > 300 and mopos[0] < 500 and mopos[1] > 100 and mopos[1] < 200:
                    if data_.data["r"] >= data_.data["costa"]:
                        for i in range(data_.Aux["auxa"]):
                            if data_.data["r"] >= data_.data["costa"]:
                                data_.data["a"] = data_.data["a"] + 0.1
                                data_.data["r"] = data_.data["r"] - data_.data["costa"]
                                data_.data["costa"] = data_.data["costa"] * 1.05
                                data_.data["costa"] = round(data_.data["costa"], 2)
                                data_.data["a"] = round(data_.data["a"], 2)
                        print("total a bought:",data_.Aux["auxa"])
                        
                if mopos[0] > 300 and mopos[0] < 500 and mopos[1] > 300 and mopos[1] < 400:
                    if data_.data["r"] >= data_.data["costb"]:
                        for i in range(data_.Aux["auxb"]):
                            data_.data["r"]= data_.data["r"] - data_.data["costb"]
                            data_.data["costb"]= data_.data["costb"] * 1.05
                            data_.data["b"]= data_.data["b"] + 0.1
                            data_.data["costb"]= round(data_.data["costb"],2)
                            data_.data["b"]= round(data_.data["b"],2)
                        print("total b bought:",data_.Aux["auxb"])
                        
                if mopos[0] > 300 and mopos[0] < 500 and mopos[1] > 500 and mopos[1] < 600:
                    if data_.data["r"] >= data_.data["costc"]:
                        for i in range(data_.Aux["auxc"]):
                            data_.data["r"]= data_.data["r"] - data_.data["costc"]
                            data_.data["costc"]= data_.data["costc"] * 1.05
                            data_.data["c"]= data_.data["c"] + 0.1
                            data_.data["costc"]= round(data_.data["costc"],2)
                            data_.data["c"]= round(data_.data["c"],2)
                        print("total c bought:",data_.Aux["auxc"])
                        
                if mopos[0] > 600 and mopos[0] < 800 and mopos[1] > 100 and mopos[1] < 200:
                    if data_.data["r"] >= data_.data["costd"]:
                        for i in range(data_.Aux["auxd"]):
                            data_.data["r"]= data_.data["r"] - data_.data["costd"]
                            data_.data["costd"]= data_.data["costd"] * 1.05
                            data_.data["d"]= data_.data["d"] + 0.1
                            data_.data["costd"]= round(data_.data["costd"],2)
                            data_.data["d"]= round(data_.data["d"],2)
                        print("total d bought:",data_.Aux["auxd"])
                #WARNING: k incrementa de a 1, distinto que los demas, tener en cuenta para la actualizacion a funcion    
                if mopos[0] > 600 and mopos[0] < 800 and mopos[1] > 300 and mopos[1] < 400:
                    if data_.data["r"] >= data_.data["costk"]:
                        for i in range(data_.Aux["auxk"]):
                            if data_.data["r"] >= data_.data["costk"]:
                                data_.data["r"]= data_.data["r"] - data_.data["costk"]
                                data_.data["costk"]= data_.data["costk"] * 1.05
                                data_.data["k"]= data_.data["k"] + 1
                                data_.data["costk"]= round(data_.data["costk"],2)
                                data_.data["k"]= round(data_.data["k"],2)
                        print("total k bought:",data_.Aux["auxk"])
                #prestigio queda asi xd         
                if mopos[0] > 600 and mopos[0] < 800 and mopos[1] > 500 and mopos[1] < 600:
                    if data_.Aux["auxw"] >= 1:
                        prestige()
                        print("prestige")
                    else:
                        print("como vas a prestigiar con 0, so tonto vo?")
        
        gameDisplay.fill(black)
        
        #grid de referencia
        for i in range(0, 900, 100):
            pygame.draw.line(gameDisplay, (255, 255, 255), (0, i), (900, i))
            pygame.draw.line(gameDisplay, (255, 255, 255), (i, 0), (i, 900))
            
        #info lateral
        rectangle(gameDisplay, grey, 0, 0, 200, 400)
        DrawText("r = " + str(f'{data_.data["r"]:.2f}') , white, black, 100, 50, 20) 
        DrawText("deltaR = " + str(f'{data_.data["deltaR"]:.2f}') , white, black, 100, 75, 20)
        DrawText("r = w*A + k"  , white, black, 100, 110, 20)      
        DrawText("A= a*b*c*d"  , white, black, 100, 130, 20)
        
        #feedback de mejoras
        DrawText("a = " + str(data_.data["a"])  , white, black, 100, 150, 20)  
        DrawText("b = " + str(data_.data["b"])  , white, black, 100, 170, 20)
        DrawText("c = " + str(data_.data["c"])  , white, black, 100, 190, 20)
        DrawText("d = " + str(data_.data["d"])  , white, black, 100, 210, 20)
        DrawText("k = " + str(data_.data["k"])  , white, black, 100, 230, 20)
        DrawText("A = " + str(data_.data["A"])  , white, black, 100, 250, 20)
        DrawText("w = " + str(data_.data["w"])  , white, black, 100, 270, 20)
        
        #botones
        rectangle(gameDisplay, grey, 300, 100, 200, 100)
        DrawText("a+0.1 = " + str(data_.data["costa"])  , white, black, 400, 150, 20)
        DrawText("+" + str(int(data_.Aux["auxa"]))  , white, black, 400, 170, 20) 
        rectangle(gameDisplay, grey, 300, 300, 200, 100)
        DrawText("b+0.1 = " + str(data_.data["costb"])  , white, black, 400, 350, 20)
        DrawText("+" + str(int(data_.Aux["auxb"]))  , white, black, 400, 370, 20)
        rectangle(gameDisplay, grey, 300, 500, 200, 100)
        DrawText("c+0.1 = " + str(data_.data["costc"])  , white, black, 400, 550, 20)
        DrawText("+" + str(int(data_.Aux["auxc"]))  , white, black, 400, 570, 20)
        rectangle(gameDisplay, grey, 600, 100, 200, 100)
        DrawText("d+0.1 = " + str(data_.data["costd"])  , white, black, 700, 150, 20)
        DrawText("+" + str(int(data_.Aux["auxd"]))  , white, black, 700, 170, 20)
        rectangle(gameDisplay, grey, 600, 300, 200, 100)
        DrawText("k+1 = " + str(data_.data["costk"])  , white, black, 700, 350, 20)
        DrawText("+" + str(int(data_.Aux["auxk"]))  , white, black, 700, 370, 20)
        rectangle(gameDisplay, grey, 600, 500, 200, 100)
        DrawText("PRESTIGE"  , white, black, 700, 550, 20)
        DrawText("W +" + str(int(data_.Aux["auxw"]))  , white, black, 700, 570, 20)
        
        #display y frames
        pygame.display.update()
        clock.tick(60)

main_loop()
pygame.quit()
quit()