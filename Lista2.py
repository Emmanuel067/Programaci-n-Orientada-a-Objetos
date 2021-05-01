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

    buscar_palabra = input("Dígame la palabra a buscar: ")
    cont = 0
    for i in lista:
        if i == buscar_palabra:
            cont += 1
    if cont == 0:
        print("La palabra '" + buscar_palabra + "' no aparece en la lista.")
    elif cont == 1:
        print("La palabra '" + buscar_palabra + "' aparece una vez en la lista.")
    else:
        print("La palabra '" + buscar_palabra + "' aparece", cont, "veces en la lista.")