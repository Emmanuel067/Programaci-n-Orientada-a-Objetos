#6.1. Crea un programa que pida al usuario que introduzca la suma de 135 y 768. Deberá 
# repetirse hasta que introduzca el resultado correcto.

suma = int(input("Cuánto es 135+768? "))
while suma != 903:
    suma = int(input("No! Vuelve a intentar... Cuánto es 135+768? "))
print("Perfecto!")



#6.2. Pide un código y una contraseña al usuario. No se le dejará proseguir hasta 
# que el código sea 1234 y la clave sea 5000.

login = input("Dime tu código de acceso: ")
password = input("Dime tu contraseña: ")
while not (login == "1234" and password == "5000"):
    print("Acceso denegado!")
    login = input("Dime tu código de acceso: ")
    password = input("Dime tu contraseña: ")
print("Acceso concedido!")