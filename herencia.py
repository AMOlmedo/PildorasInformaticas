# ejemplo de Herencia POO
class Vehiculo():    # creacion de la clase "Vehiculo"
    # constructor
    def __init__(self, marca, modelo): # __init__ indica que es un constructor
        self.marca=marca      # Aqui se define el estado inicial
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False
    # Metodos (que hace. Tambien modifica el estado inicial)
    def arrancar(self):
        self.enmarcha=True
    def acelerar(self):
        self.acelera=True
    def frenar(self):
        self.frena=True
    def estado(self):
        print("\n Marca: ", self.marca, "\n Modelo: ", self.modelo, "\n En marcha: ", self.enmarcha, "\n Acelerando: ", self.acelera, "\n Frena: ", self.frena )

class Moto(Vehiculo):  # La clase Moto HEREDA de la clase Vehiculo
    pass

miMoto=Moto("honda", "CBR")  # Creamos la instancia miMoto de la clase  Moto. con los parametros que pide el constructor

miMoto.estado()   # llamamos al metod "estado" de la instacia "miMoto"
            

            