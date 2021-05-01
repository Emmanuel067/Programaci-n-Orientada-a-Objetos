#14.1. Pide al usuario dos números enteros, y da el valor True a una variable booleana llamada 
# "ambosPares" en caso de que las dos sean pares, o el valor False en caso contrario.
#  El programa debe comenzar con un comentario que diga de qué trata y otro que diga tu nombre.



# Prueba de booleanos
# Ejemplo de la introducción a Python, por Nacho Cabanes
 
n1 = int(input("Dime un número: "))
n2 = int(input("Dime otro número: "))
ambosPares = (n1 % 2 == 0) and (n2 % 2 == 0)
print("Ambos pares?", ambosPares)