import math
import random 
tablero=[]
TABLERO_FILAS=3
TABLERO_COLUMNAS=3
random.seed(5)
###
for i in range(9):
    tablero.append(" ")
    #casillavacia.append(i)
    ##3
def numero(literal,inferior,superior):
    while True:
        valor=input(literal)
        while(not valor.isnumeric()):
            print("solo se aseptan numeros entre {0} y {1}".format(inferior,superior))
            valor=input(literal)
        coor= int(valor)
        if(coor>= inferior and coor<= superior):
            return coor

        else:
            print("el valor es incorrecto introdusca un nuevo balor entre {0} y {1} ".format(inferior,superior))

def colocarficha(ficha):
    print("DAME LA POCISION: ")
    while True:
        fila= numero("fila entre [1 y 3]: ", 1,3)-1
        columna= numero("columna entre [1 y 3]: ",1,3)-1
      
        casilla=fila*TABLERO_COLUMNAS+columna
        if(tablero[casilla]!= " "):
            print("LA CASILLA ESTA OCUPADA")
        else:
            tablero[casilla]=ficha
            return casilla


def colocarfichamaquina(ficha):
    for casilla,valorcasilla in enumerate(tablero):
        if(valorcasilla==" "):
           tablero[casilla]=ficha
           return casilla

def pintartablero():
    pos=0
    print(("-"*18))
    for fila in range(3):
        for columna in range(3):
            print("|",tablero[pos]," ", end= " ")
            pos+=1
        print("|\n",("-")
*18)
def numerodehermanos(casilla,ficha, v, h):
    f=math.floor(casilla/TABLERO_COLUMNAS)
    c= casilla % TABLERO_COLUMNAS
    fila_nueva= f+v
    if (fila_nueva<0 or fila_nueva>= TABLERO_FILAS):
        return 0
    columna_nueva= c+h
    if(columna_nueva<0 or columna_nueva>=TABLERO_COLUMNAS):
        return 0
    pos=(fila_nueva*TABLERO_COLUMNAS+columna_nueva)
    if (tablero[pos]!=ficha):
        return 0
    else:
        return 1+numerodehermanos(pos,ficha,v,h)



def hemosganado(casilla,ficha):
    hermanos=numerodehermanos(casilla,ficha,-1,-1)+numerodehermanos(casilla,ficha,1,1)
    if (hermanos==2):
        return True
    hermanos=numerodehermanos(casilla,ficha,1,-1)+numerodehermanos(casilla,ficha,-1,1)
    if (hermanos==2):
       return True
    hermanos=numerodehermanos(casilla,ficha,-1,0)+numerodehermanos(casilla,ficha,1,0)
    if (hermanos==2):
       return True
    hermanos=numerodehermanos(casilla,ficha,0,-1)+numerodehermanos(casilla,ficha,0,1)
    if (hermanos==2):
       return True

jugadores=[]
numerodejugadores=numero("numero de jugadore: ",0,2)
for i in range(numerodejugadores):
    jugadores.append({"nombre":input("nombre del jugador"+str(i+1)+": "),"tipo":"h"})
for i in range(2-numerodejugadores):
    jugadores.append({"nombre":"maquina"+str(i+1),"tipo":"m"})
    
print("\n Empesamos la partida con los jugadores")
for jugador in jugadores:
    print("\t", jugador["nombre"])

continuar= True
fichasentablero=0
while continuar:
    pintartablero()
    numjugador=(fichasentablero&1)
    ficha='x' if numjugador==1 else 'o'
    if (jugadores[numjugador]["tipo"]=="h"):
        casilla=colocarficha(ficha)
    else:
        casilla=colocarfichamaquina(ficha)
    if (hemosganado(casilla,ficha)):
        continuar= False
        print(jugadores[numjugador]["nombre"],": !! Felicidades has ganado !!  ")
    fichasentablero+=1
    if(fichasentablero==9):
        continuar=False
pintartablero()