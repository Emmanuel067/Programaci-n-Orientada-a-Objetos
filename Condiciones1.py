#4.1. Pide al usuario un número entero y responde si es par o impar (pista: es par si el resto de la división entre 2 es 0).

n = int(input("Dime un número: "))
if n % 2 == 0 :
    print("Es par")
else :
    print("Es impar")


#4.2. Pide un número real y responde si es positivo, negativo o cero (pista: deberás enlazar dos "if").

numero = float(input("Dime un número: "))
if numero > 0 :
    print("Es positivo")
else :
    if numero < 0 :
        print("Es negativo")
    else :
        print("Es cero")

#4.3. Pide dos números enteros y muestra en pantalla su división (o el mensaje de aviso "no se puede dividir entre cero" si el segundo es cero).

n1 = int(input("Dime el primer número: "))
n2 = int(input("Dime el segundo número: "))
if n2 != 0 :
    print("Su división es:", n1/n2)
else :
    print("No se puede dividir entre cero")