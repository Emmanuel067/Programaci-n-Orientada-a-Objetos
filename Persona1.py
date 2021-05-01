class Persona:
    def __init__(self,nom, ed, indj):
        self.nombre = nom
        self.edad = ed
        self.ind = indj
        
    def mostrar(self):
        print("Nombre: {} \nEdad: {}\nIND: {}".format(self.nombre, self.edad, self.ind))

    def mayor(self):
        if (self.edad >= 18):
            print ("Es mayor de edad")
        elif(self.edad < 18):
            print("Es menor de edad")

name = ""
age = ""
idd = ""

name = input("Ingresa tu nombre: ")
age = int(input("Ingresa tu edad: "))
idd = input("Ingresa tu DNI: ")


Humano = Persona(name,age, idd)
Humano.mostrar()
Humano.mayor()
