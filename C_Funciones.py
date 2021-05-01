#10.1. Crea una función que reciba 3 números y devuelva su suma.

def suma(n1, n2, n3):
    return n1+n2+n3
 
print("La suma de 6, 7 y 8 es", suma(6,7,8) )




#10.2. Crea una función que reciba una cadena de texto y una letra, 
# y devuelva la cantidad de veces que la letra aparece dentro de la cadena.

def cantidadVeces(texto, letra):
    cantidad = 0
    for l in texto:
        if l == letra:
            cantidad += 1
    return cantidad
 
print('Veces que "hasta mañana" contiene una "a":',
    cantidadVeces("hasta mañana", "a") )




#10.3. Crea un procedimiento que escriba una línea formada por
#  2 letras, repetidas varias veces. Por ejemplo, para "-", "=" y 3, escribiría "-=-=-=".

def repetir(letra1, letra2, veces):
    for i in range(0, veces):
        print(letra1, end="")
        print(letra2, end="")
 
repetir("-", "=", 3)

