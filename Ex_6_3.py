numero_filas=5
numero_columnas= 14
meses = ["","En","Feb","Mar","Ab","May","Jun","Jul","Agos","Sep","Oct","Nov","Diciem","Total "]
materias = ["","Español    ","Matematicas","Geografia  ","Total      "]
def llenar(matriz,num_filas,num_columnas,mensaje):
    print(mensaje)
    res1 = 0
    res2 = 0
    res3 = 0
    res4 = 0
    res5 = 0
    res6 = 0
    res7 = 0
    res8 = 0
    res9 = 0
    res10 = 0
    res11 = 0
    res12 = 0
    mat1 = 0
    elemento0 = 0
    elemento2 = 0
    elemento3 = 0
    elemento4 = 0
    elemento5 = 0
    elemento6 = 0
    elemento7 = 0
    elemento8 = 0
    elemento9 = 0
    elemento10 = 0
    elemento11 = 0
    elemento12 = 0
    final = 0
    mayor=0
    posicion=0
    for fila in range(0, num_filas):
        matriz.append( [] ) # añade una fila
        for columna in range(0, num_columnas):

            #elemento = int(input("Ingresa un valor      "))
               
            if fila == 0:
                elemento = meses[columna]
                matriz[fila].append(elemento)
            if columna == 1 and fila>0:
                elemento0 = int(input("Mes: {0} \nIngresa el numero de horas para la materia de {1} ".format(meses[1],materias[fila])))
                if columna == 1 and fila ==4 :
                    matriz[fila].append(res1) 
                else:   
                    res1 = res1 + elemento0
                    matriz[fila].append(elemento0)
            if columna == 2 and fila>0:
                elemento2 = int(input("Mes: {0} \nIngresa el numero de horas para la materia de {1} ".format(meses[2],materias[fila])))
                if columna == 2 and fila == 4:
                    matriz[fila].append(res2)
                else:    
                    res2 = res2 + elemento2
                    matriz[fila].append(elemento2)
            if columna == 3 and fila>0:
                elemento3 = int(input("Mes: {0} \nIngresa el numero de horas para la materia de {1} ".format(meses[3],materias[fila])))
                if columna == 3 and fila == 4:
                    matriz[fila].append(res3)
                else:    
                    res3 = res3 + elemento3
                    matriz[fila].append(elemento3)
            if columna == 4 and fila>0:
                elemento4 = int(input("Mes: {0} \nIngresa el numero de horas para la materia de {1} ".format(meses[4],materias[fila])))
                if columna == 4 and fila == 4:
                    matriz[fila].append(res4)
                else:    
                    res4 = res4 + elemento4
                    matriz[fila].append(elemento4)
            if columna == 5 and fila>0:
                elemento5 = int(input("Mes: {0} \nIngresa el numero de horas para la materia de {1} ".format(meses[5],materias[fila])))
                if columna == 5 and fila == 4:
                    matriz[fila].append(res5)
                else:    
                    res5 = res5 + elemento5
                    matriz[fila].append(elemento5)
            ###
            if columna == 6 and fila>0:
                elemento6 = int(input("Mes: {0} \nIngresa el numero de horas para la materia de {1} ".format(meses[6],materias[fila])))
                if columna == 6 and fila == 4:
                    matriz[fila].append(res6)
                else:    
                    res6 = res6 + elemento6
                    matriz[fila].append(elemento6)
            ###
            if columna == 7 and fila>0:
                elemento7 = int(input("Mes: {0} \nIngresa el numero de horas para la materia de {1} ".format(meses[7],materias[fila])))
                if columna == 7 and fila == 4:
                    matriz[fila].append(res7)
                else:    
                    res7 = res7 + elemento7
                    matriz[fila].append(elemento7)
            ####
            if columna == 8 and fila>0:
                elemento8 = int(input("Mes: {0} \nIngresa el numero de horas para la materia de {1} ".format(meses[8],materias[fila])))
                if columna == 8 and fila == 4:
                    matriz[fila].append(res8)
                else:    
                    res8 = res8 + elemento8
                    matriz[fila].append(elemento8)
            ###
            if columna == 9 and fila>0:
                elemento9 = int(input("Mes: {0} \nIngresa el numero de horas para la materia de {1} ".format(meses[9],materias[fila])))
                if columna == 9 and fila == 4:
                    matriz[fila].append(res9)
                else:    
                    res9 = res9 + elemento9
                    matriz[fila].append(elemento9)
                        
            ####            
            if columna == 10 and fila>0:
                elemento10 = int(input("Mes: {0} \nIngresa el numero de horas para la materia de {1} ".format(meses[10],materias[fila])))
                if columna == 10 and fila == 4:
                    matriz[fila].append(res10)
                else:    
                    res10 = res10 + elemento10
                    matriz[fila].append(elemento10)
            ###
            if columna == 11 and fila>0:
                elemento11 = int(input("Mes: {0} \nIngresa el numero de horas para la materia de {1} ".format(meses[11],materias[fila])))
                if columna == 11 and fila == 4:
                    matriz[fila].append(res11)
                else:    
                    res11 = res11 + elemento11
                    matriz[fila].append(elemento11)
            ###
            if columna == 12 and fila>0:
                elemento12 = int(input("Mes: {0} \nIngresa el numero de horas para la materia de {1} ".format(meses[12],materias[fila])))
                if columna == 12 and fila == 4:
                    matriz[fila].append(res12)
                else:    
                    res12 = res12 + elemento12
                    matriz[fila].append(elemento12)
            if columna == 0:
                elemento= materias[fila]
                matriz[fila].append(elemento)
            mat1 = int(elemento0) + int(elemento2) + int(elemento3) + int(elemento4) + int(elemento5) + int(elemento6) + int(elemento7) + int(elemento8) + int(elemento9) + int(elemento10) + int(elemento11) + int(elemento12)
            if columna == 13:
                elemento = mat1
                matriz[fila].append(elemento)
            final += mat1
            if mat1> mayor:
                mayor= mat1
                posicion=fila
            
                
        print("De la materia {0} estudiaste la cantida de {1} horas ".format(materias[fila],mat1))
    matriz[4][13]=38
    print("De la materia {0} estudiaste un total de {1} horas ".format(materias[posicion],mayor))
            
             
def imprimir(matriz):
    cadena = ''
    for i in range(len(matriz)):
        cadena += '['
        for j in range(len(matriz[i])):
            cadena += '   {:>4s}   '.format(str(matriz[i][j]))
        cadena += '  ]\n  '
    return cadena

    
matris=[]
llenar(matris,numero_filas,numero_columnas,"Matris")
m = imprimir(matris)
print(m)