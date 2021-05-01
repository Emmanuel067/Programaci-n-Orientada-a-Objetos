#7.1. Crea un programa que pida al usuario que introduzca su nombre y un número entero,
#  y escriba su nombre en pantalla tantas veces como indique ese número entero.

nombre = input("Dime tu nombre: ")
cantidad = int(input("¿Cuántas veces quieres que lo escriba? "))
for i in range(0, cantidad):
    print(nombre)


#7.2. Pide al usuario un número entero (por ejemplo, 5) y 
# muestra la tabla de multiplicar de ese número (desde "5 x 1 = 5" hasta "5 x 10 = 50").

tabla = int(input("¿Qué tabla de multiplicar quieres? "))
for n in range(1, 11):
    print(tabla, "x", n, "=", tabla*n)




#7.3. Pide al usuario un número entero (por ejemplo, 58)
#  y responde todos los múltiplos de 7 que haya entre el número 1 y ese número (incluido).

n = int(input("Dime un número "))
print("Los múltiplos de 7 hasta ese número son...")
for i in range(1, n+1):
    if i % 7 == 0:
        print(i)