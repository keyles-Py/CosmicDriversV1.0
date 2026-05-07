import numpy as np
import os
from time import sleep
from random import randint
import keyboard
import msvcrt
from text import EN, ES

maain : bool = True #Estados del juego
game : bool = False
win : bool = False
over : bool = False

stdsize1 : int = 8 #configuración predeterminada
stdsize2 : int = 15
puntos : int = 40
puntaje : int = 0

LAN : dict = EN


def clear_input_buffer(): 
    while msvcrt.kbhit():
        msvcrt.getch()  

def casillaOcupada(mapa, size1, size2, posOcupadas):
    while True:
        pos1 = randint(0, size1-1)
        pos2 = randint(0, size2-1)
        if (pos1, pos2) not in posOcupadas:
            posOcupadas.add((pos1, pos2))
            return pos1, pos2
#                   4     11    ->   al crear el mapa con estos valores ocurre un error
def crearMapa(size1, size2):
    map = np.full((size1,size2)," ")
    posOcupadas = set()

    for i in range(0,round((size1*size2)*0.2)):
        pos1, pos2 = casillaOcupada(map, size1, size2, posOcupadas)
        map[pos1][pos2] = "X"
    for i in range(0,puntos):
        pos1, pos2 = casillaOcupada(map, size1, size2, posOcupadas)
        map[pos1][pos2] = "O"
    playerPos1, playerPos2 = casillaOcupada(map, size1, size2, posOcupadas) #posición al azar del jugador
    map[playerPos1][playerPos2] = "▶" #El jugador

    return map, playerPos1, playerPos2

def winn(mapa, size1, size2): #Función que determina si el jugador gano
    for i in range(0,size1-1):
        for j in range(0,size2-1):
            if mapa[i][j] == "O":
                return False
    return True

while maain: #bucle principal
    while True:
        clear_input_buffer()
        print("Cosmic Drivers V1.0")
        print(LAN["Menu"])
        opt = input(":")
        try:
            opt = int(opt)
            break
        except ValueError:
            print(LAN["adv1"])
            sleep(1)
            os.system('cls')
    os.system('cls')

    if opt == 1:
        map, pos1, pos2 = crearMapa(stdsize1,stdsize2)
        puntaje = 0
        game = True
        while game:
            print(map, end="")
            print(LAN["score"],puntaje)

            if keyboard.is_pressed('w'): #control de movimientos del jugador
                if pos1==0:
                    map[pos1][pos2] = "▲"
                else:
                    if map[pos1-1][pos2] == "O":    
                        puntaje = puntaje + 1
                        map[pos1-1][pos2] = "▲"
                        map[pos1][pos2] = " "
                        pos1 = pos1-1
                        if winn(map, stdsize1, stdsize2):
                            game = False
                            win = True
                    elif map[pos1-1][pos2] == "X":  
                        game = False
                        over = True
                    else:                           
                        map[pos1-1][pos2] = "▲"
                        map[pos1][pos2] = " "
                        pos1 = pos1-1
                        if winn(map, stdsize1, stdsize2):
                            game = False
                            win = True

            elif keyboard.is_pressed('s'):
                if pos1+1==stdsize1:
                    map[pos1][pos2] = "▼"
                else:
                    if map[pos1+1][pos2] == "O":
                        puntaje = puntaje +1
                        map[pos1+1][pos2] = "▼"
                        map[pos1][pos2] = " "
                        pos1 = pos1+1
                        if winn(map, stdsize1, stdsize2):
                            game = False
                            win = True
                    elif map[pos1+1][pos2] == "X":
                        game = False
                        over = True
                    else:
                        map[pos1+1][pos2] = "▼"
                        map[pos1][pos2] = " "
                        pos1 = pos1+1
                        if winn(map, stdsize1, stdsize2):
                            game = False
                            win = True

            elif keyboard.is_pressed('a'):
                if pos2 == 0:
                    map[pos1][pos2] = "◀"
                else:
                    if map[pos1][pos2-1] == "O":
                        puntaje = puntaje + 1
                        map[pos1][pos2-1] = "◀"
                        map[pos1][pos2] = " "
                        pos2 = pos2-1
                        if winn(map, stdsize1, stdsize2):
                            game = False
                            win = True
                    elif map[pos1][pos2-1] == "X":
                        game = False
                        over = True
                    else:
                        map[pos1][pos2-1] = "◀"
                        map[pos1][pos2] = " "
                        pos2 = pos2-1
                        if winn(map, stdsize1, stdsize2):
                            game = False
                            win = True
                        
            elif keyboard.is_pressed('d'):
                if pos2+1 == stdsize2:
                    map[pos1][pos2] = "▶"
                else:
                    if map[pos1][pos2+1] == "O":
                        puntaje = puntaje + 1
                        map[pos1][pos2+1] = "▶"
                        map[pos1][pos2] = " "
                        pos2 = pos2+1
                        if winn(map, stdsize1, stdsize2):
                            game = False
                            win = True
                    elif map[pos1][pos2+1] == "X":
                        game = False
                        over = True
                    else:
                        map[pos1][pos2+1] = "▶"
                        map[pos1][pos2] = " "
                        pos2 = pos2+1
                        if winn(map, stdsize1, stdsize2):
                            game = False
                            win = True
            sleep(0.1)
            os.system('cls')
            
            while win:
                print(LAN["win"])
                sleep(2)
                os.system('cls')
                win = False

            while over:
                print(LAN["lose"])
                puntaje = 0
                sleep(2)
                os.system('cls')
                over = False

    elif opt == 2:
        while True:
            while True:
                print(LAN["config"])
                #print("y la cantidad de puntos en el mapa")
                #print("1. tamaño del mapa\n2. cantidad de puntos")
                ans = input(":")
                try:
                    ans = int(ans)
                    break
                except ValueError:
                    print(LAN["adv1"])
                    sleep(1)
                    os.system('cls')

            if ans == 1:
                while True:
                    print(LAN["configMap1"])
                    print(LAN["currentValues"], stdsize1, stdsize2)
                    stdsize1 = input(":")
                    try:
                        stdsize1 = int(stdsize1)
                        if stdsize1 <= 8 and stdsize1 > 4:
                            break
                        else:
                            print(LAN["configMap1"])
                            sleep(1)
                            os.system('cls')
                    except ValueError:
                        print(LAN["valueError"])
                        sleep(1)
                        os.system('cls')
                while True:
                    print(LAN["configMap2"])
                    stdsize2 = input(":")
                    try:
                        stdsize2 = int(stdsize2)
                        if stdsize2 <= 15 and stdsize2 > 11:
                            break
                        else:
                            print(LAN["configMap2"])
                            sleep(1)
                            os.system('cls')
                    except ValueError:
                        print(LAN["valueError"])
                        sleep(1)
                        os.system('cls')
                print(LAN["successConfigMap"])
                print(LAN["currentValues"], stdsize1, stdsize2)
                sleep(1)
                os.system('cls')
                break    
            elif ans == 2:
                while True:
                    print(LAN["configScore"])
                    puntos = int(input(":"))
                    if puntos >= stdsize1*stdsize2:
                        print(LAN["configScoreError"], stdsize1*stdsize2)
                        sleep(2)
                        os.system('cls')
                    else:
                        print(LAN["successConfigScore"], puntos)
                        print(LAN["successConfigMap"])
                        sleep(2)
                        os.system('cls')
                        break
                break
            elif ans == 3:
                while True:
                    print("1. EN\n2. ES")
                    try:
                        lan = int(input(":"))
                        if lan in [1,2]:
                            lanopt = EN if lan == 1 else ES 
                            LAN = lanopt
                            print(LAN["LangChange"])
                            sleep(1)
                            os.system('cls')
                            break
                    except ValueError:
                        print("Error")
                break
            else:
                print(LAN["NoValidOption"])
                sleep(1)
                os.system('cls')
    elif opt == 3:
        print(LAN["Exit"])
        sleep(1)
        break
    else:
        print(LAN["NoValidOption"])
        sleep(1)
        os.system('cls')