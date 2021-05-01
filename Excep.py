try:
    frase = input("Dime el nombre de un fichero: ")
    fichero = open(frase, "r")
 
except:
    print("No se ha podido acceder al fichero")
 
else:
    lineas = fichero.readlines()
    fichero.close()
 
    for i in range(0, len(lineas) ):
        print( lineas[i].rstrip() )

