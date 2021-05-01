numero_filas=int(input("numero de filas:     "))
numero_columnas= int(input("numero de columnas:    "))


#matris1         matris2         matrisr
#1   2   3       1   2   3       1   4   9
#4   5   6       4   5   6
#7   8   9       7   8   9

def llenar(matriz,num_filas,num_columnas,mensaje):
    print(mensaje)
    for fila in range(0, num_filas):
        matriz.append( [] ) # añade una fila
        for columna in range(0, num_columnas):
            elemento = int(input("Ingresa un valor      "))
            matriz[fila].append(elemento)
def sumar(matriz_1,matriz_2,matriz_r,num_filas,num_columnas):
    for fila in range(0, num_filas):
        matriz_r.append( [] ) # añade una fila
        for columna in range(0, num_columnas):
            elemento = matriz_1[fila][columna] + matriz_2[fila][columna]
            matriz_r[fila].append(elemento)

def imprimir(matriz):
    cadena = ''
    for i in range(len(matriz)):
        cadena += '['
        for j in range(len(matriz[i])):
            cadena += '{:>4s}'.format(str(matriz[i][j]))
        cadena += ']\n'
    return cadena
matriz1 = []
matriz2 = []
matriz_resultado = []
llenar(matriz1,numero_filas,numero_columnas,"Ingresa los valores para la primer matriz")
llenar(matriz2,numero_filas,numero_columnas,"Ingresa los valores para la segunda matriz")
sumar(matriz1,matriz2,matriz_resultado,numero_filas,numero_columnas)
m = imprimir(matriz1)
print("Matriz1\n",m)
n = imprimir(matriz2)
print("Matriz2\n",n)
o = imprimir(matriz_resultado)
print("Resultado: \n",o)