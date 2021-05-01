class Cuenta:
    def __init__(self, ti, can, ):
        self.titular = ti
        self.cantidad = can
      

    def mostrar(self):
        print("Titular: {}\nCantidad: {}\nResto: {}\n".format(self.titular,self.cantidad,self.retirar))

    def ingresar(self,cantidad):
        if (self.cantidad <=0):
            print("cantidad negativa")  
            self.cantidad = 0
            return False

    def retirar(self,cantidad):
        self.cantidad = self.cantidad-cantidad
                
            
ti= " "
deposito=" "
retiro=" "
   
ti= input("ingresa el Titular: ")
deposito= float (input("ingresa la cantidad: "))
retiro= float (input("ingrese la cantidada retirar: "))
 
cantidad = Cuenta (ti, deposito)
cantidad.mostrar()
if(cantidad.ingresar(deposito) != False):
    cantidad.retirar(retiro)  
cantidad.mostrar()




    