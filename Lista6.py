numero = int(input("Dígame cuántas palabras tiene la lista: "))
if numero < 1:
    print("¡Imposible!")
else:
    lista = []
    i = 0
    while(i < numero):
        print("Ingresa la palabra",str(i+1)+ ": ", end="")
        palabra = input()
        lista += [palabra]
        i=i+1    
    print("La lista creada es:", lista)
    inversa = []
    for i in lista:
        inversa = [i] + inversa
    print("La lista inversa es:", inversa)