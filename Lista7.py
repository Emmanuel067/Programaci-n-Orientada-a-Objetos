numero = int(input("Dígame cuántas palabras tiene la lista: "))

if numero < 1:
    print("¡Imposible!")
else:
    lista = []
    for i in range(numero):
        print("Dígame la palabra", str(i + 1) + ": ", end="")
        palabra = input()
        lista += [palabra]
    print("La lista creada es:", lista)

    for i in range(len(lista)-1, -1, -1):
        if lista[i] in lista[:i]:
            del(lista[i])
    print("La lista sin repeticiones es:", lista)