#5.1. Pide un número real y responde si es positivo, negativo o cero, empleando "elif".

numero = float(input("Dime un número: "))
if numero > 0 :
    print("Es positivo")
elif numero < 0 :
    print("Es negativo")
else :
    print("Es cero")




#5.2. Pide al usuario un número entero del 1 al 12 y escribe el nombre del mes correspondiente (1=enero, 12=diciembre).

mes = int(input("Dime número de mes: "))
if mes == 1:
  print("Enero")
elif mes == 2:
  print("Febrero")
elif mes == 3:
  print("Marzo")
elif mes == 4:
  print("Abril")
elif mes == 5:
  print("Mayo")
elif mes == 6:
  print("Junio")
elif mes == 7:
  print("Julio")
elif mes == 8:
  print("Agosto")
elif mes == 9:
  print("Septiembre")
elif mes == 10:
  print("Octubre")
elif mes == 11:
  print("Noviembre")
elif mes == 12:
  print("Diciembre")
else:
  print("Mes incorrecto")