class Cuenta:
    def __init__(self, ti, can, ed,):
        self.titular = ti
        self.cantidad = can
        self.edad = ed

    def mostrar(self):
        print("Titular: {}\nCantidad: {}\nEdad: {}\n".format(self.titular,self.cantidad,self.edad))

    def ingresar(self,cantidad):
        if (self.cantidad <=0):
            print("cantidad negativa")  
            self.cantidad = 0
            return False

    def retirar(self,cantidad):
        self.cantidad = self.cantidad-cantidad
        self.retiro=cantidad

        
class CuentaJoven():
    def __init__(self, ti, can, ed,por):
        self.titular = ti
        self.cantidad = can
        self.edad = ed
        self.porcentaje = por

    def mostrar(self):
        print("Titular: {}\nCantidad: {}\nEdad: {}\nPorcentaje: {}\n".format(self.titular,self.cantidad,self.edad,self.porcentaje))

    def validarTitular(self,validar_Edad):
        print("Entro al metodo")
        if (self.edad >= 18 and self.edad <= 25 ):
            print("cuenta valida")
        else:
            print("falce")
    def porciento(self,cantidad,porcentaje):
        resultado= (self.cantidad * self.porcentaje) / 100
        print("nuevo saldo total: ")

ti= " "
deposito=" "
retiro=" "
edad=" "
porciento = ""    


ti= input("ingresa el Titular: ")
deposito= float (input("ingresa la cantidad: "))
retiro= float (input("ingrese la cantidada retirar: "))
edad= int(input("ingresa tu edad: "))
porciento= float (input("ingresa el porcentaje: "))
print("\n")
print("Datos de la primer clase")
cantidad = Cuenta(ti, deposito, edad)
cantidad.mostrar()
if(cantidad.ingresar(deposito) != False):
    cantidad.retirar(retiro)  
cantidad.mostrar()

print("\n")
print("Datos de la segunda clase")
cuanta_Joven = CuentaJoven(ti,deposito,edad,porciento)
print("Cuenta joven")
cuanta_Joven.mostrar()
cuanta_Joven.validarTitular(edad)
cuanta_Joven.porciento(deposito,porciento)
