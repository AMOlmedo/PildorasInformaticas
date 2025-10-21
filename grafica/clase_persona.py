class Persona:   #clase Persona
    def __init__(self, nombre,edad):  #constructor de la clase 
        #recibe por parametro nombre  y edad
        #por convencion _nombre y _edad deben ser tratadas como privadas
        self._nombre=nombre
        self._edad=edad

    def get_nombre(self):
        return self._nombre
    
    def set_nombre(self):
        self._nombre=nombre

    def get_edad(self):
        return self._edad
    
    def set_edad(self, edad):
        if edad <0:
            print("la edad no puede ser negativa")
        else:
            self._edad= edad
    
    def mostrar_detalle(self):
        print(f"Nombre: {self._nombre}, Edad: {self._edad}")

    # Decoradores

    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre= nombre

    @property
    def edad(self):
        return self._edad
    
    @edad.setter
    def edad(self, edad):
        if edad <0:
            print("la edad no puede ser negativa")
        else:
            self._edad=edad
    
    @nombre.deleter
    def nombre(self):
        print("eliminando nombre...")
        del self.nombre
        

adrian=Persona("Adrian", 52) #creo la instancia adrian de la clase Persona
print(adrian._nombre)
print(adrian._edad)

# Ahora utilizando buenas practicas con los getters
print(" Utilizando get para obtener los parametros de la instancia martina")
martina=Persona("Martina", 16)
print(martina.get_nombre())
print(martina.get_edad())

# Pero, para acceder se debe hacer por los metodos gettes y setters para controlar
# el acceso a las variables privada


#utilizando los decoradores
kuka=Persona("Kukaracha", 5)
print(f"Nombre: {kuka.nombre}, Edad: {kuka.edad}")

# del kuka.nombre




