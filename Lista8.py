numero = int(input("Dígame cuántas palabras tiene la primera lista: "))

if numero < 1:
    print("¡Imposible!")
else:
    primera = []
    for i in range(numero):
        print("Dígame la palabra", str(i + 1) + ": ", end="")
        palabra = input()
        primera += [palabra]
    print("La primera lista es:", primera)

    for i in range(len(primera)-1, -1, -1):
        if primera[i] in primera[:i]:
            del(primera[i])

    numero2 = int(input("Dígame cuántas palabras tiene la segunda lista: "))

    if numero2 < 1:
        print("¡Imposible!")
    else:
        segunda = []
        for i in range(numero2):
            print("Dígame la palabra", str(i + 1) + ": ", end="")
            palabra = input()
            segunda += [palabra]
        print("La segunda lista es:", segunda)

        for i in range(len(segunda)-1, -1, -1):
            if segunda[i] in segunda[:i]:
                del(segunda[i])

        comunes = []
        for i in primera:
            if i in segunda:
                comunes += [i]
        print("Palabras que aparecen en las dos listas:", comunes)

        soloPrimera = []
        for i in primera:
            if i not in segunda:
                soloPrimera += [i]
        print("Palabras que sólo aparecen en la primera lista:", soloPrimera)

        soloSegunda = []
        for i in segunda:
            if i not in primera:
                soloSegunda += [i]
        print("Palabras que sólo aparecen en la segunda lista:", soloSegunda)

        todas = comunes + soloPrimera + soloSegunda
        print("Todas las palabras:", todas)