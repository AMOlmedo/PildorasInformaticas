class Persona():      # Creacion de la CLASE persona
    def __init__(self, nombre, edad, residencia):  # creacion del CONSTRUCTOR
        self.nombre=nombre    # estas son VARIABLES DE CLASE
        self.edad=edad
        self.residencia=residencia
    def descripcion(self):    #creacion  de un METODO descripcion de la clase Persona
        print("Nombre: ", self.nombre, "\nEdad: ", self.edad, "\nResidencia: ", self.residencia)

class Empleado(Persona):
    def __init__(self, salario, antiguedad):

        super().__init__("adrian", 50, "mza") # aca llamamos con super al metodo de la clase padre
        self.salaio=salario
        self.antiguedad=antiguedad

Adrian=Persona("Adrian", 52, "Argentina")  #creacion del OBJETO o INSTACIA heredada de la clase persona

Adrian.descripcion() # llamamos al METODO descricion

Adrian=Empleado(1500, 15)


