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

    buscar_palabra = input("Dígame la palabra a remplasar: ")
    sustituir = input("fue remplazada por la palabra: ")
    for i in range (len(lista)):
        if lista[i] == buscar_palabra:
            lista[i] = sustituir
    print("Nueva lsita ", lista)        

     
      