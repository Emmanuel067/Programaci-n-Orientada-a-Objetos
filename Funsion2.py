def cantidadVeces(texto, letra):
    cantidad = 0
    for l in texto:
        if l == letra:
            cantidad += 1
    return cantidad
 
print('Veces que "arbol cresera" contiene una "a":',
    cantidadVeces("arbol cresera", "a") )