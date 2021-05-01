#8.1. Crea un array con los números 10, 20, 30, 40, 50 y luego muestra los que hay en las
#  posiciones impares (primero, tercero y quinto: 10, 30 y 50).

datos = [10, 20, 30, 40, 50]
print(datos[0])
print(datos[2])
print(datos[4])


#8.2. Pide al usuario 10 números y luego muestra los que son pares.

datos = []
for n in range(1, 11):
    dato = int(input("Dime el dato "+ str(n) +": "))
    datos.append(dato)
print("Los datos pares son:")
for d in datos:
    if d % 2 == 0:
        print(d)


#8.3. Pide al usuario un número entero del 1 al 12 
# y escribe el nombre del mes correspondiente (1=enero, 12=diciembre), usando un array.

nombres = ["enero", "febrero", "marzo", "abril", "mayo", "junio",
    "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
mes = int(input("Dime el número de mes (1 a 12): "))
print("El mes es:", nombres[mes-1])