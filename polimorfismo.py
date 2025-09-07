class Auto():
    def desplazamiento(self):
        print("me muevo con 4 ruedas")

class Moto():
    def desplazamiento(self):
        print("me muevo con 2 ruedas")

class Camion():
    def desplazamiento(self):
        print("me muevo con 6 ruedas")

vehiculo1=Moto()  # creamos una objeto de la clase moto
vehiculo1.desplazamiento()  #llamamos al METODO desplazamiento de la clase

vehiculo2=Auto()
vehiculo2.desplazamiento()

vehiculo3=Camion()
vehiculo3.desplazamiento()

print("======POLIMORFISMO======")

def desplazamientoVehiculo(vehiculo):
    vehiculo.desplazamiento()
#Polimorfismo: cambia dependiendo de las circunstancia y la clase que es llamada

miVehiculo=Camion()   #objeto de la clase camion
desplazamientoVehiculo(miVehiculo) #el desplazamiento los toma de la clase Camion

miVehiculo=Moto()  #ahora cambia de clase por lo tanto de condicion
desplazamientoVehiculo(miVehiculo)
                       