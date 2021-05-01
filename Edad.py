class Edad:
    def __init__(self, edad):
        self.edad = edad

    def mostrar(self):
        print("usted {}\n".format,self.edad)

    def ingreso(self):
        if (self.edad >=18):
            print("es mayorde edad")
        elif(self.edad <18):
            print("es menor de edad")

    
eda= " "
eda= int(input("ingresa tu edad"))


años = Edad (eda)
años.ingreso()
años.mostrar
