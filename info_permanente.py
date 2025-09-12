import pickle

class Persona:
    def __init__(self,nombre, genero, edad):
        self.nombre = nombre
        self.genero = genero
        self.edad = edad
        print("se ha creado una persona nueva con el nombre de: ", self.nombre)
    
    def __str__(self): #convierte en cadena de texto la informacion de un objeto
        #return "{}{}{}".format(self.nombre, self.genero, self.edad)
        return f"{self.nombre} {self.genero} {self.edad}"  #f-Strings de la version 3.6 en adelante
        #es igual al  return de la linea anterior pero mas legible.

class ListaPersonas:
    personas=[ ]
    def __init__(self):
        listaDePersonas=open("archivo_guardado", "ab+") # ab+ agregar informacion en binario
        listaDePersonas.seek(0)  #  desplaza el curson a la posicion 0 para que asi lea toda la lista
        try:
            self.personas=pickle.load(listaDePersonas) #se carga en la lista personas
            print("se cargaron {} personas del archivo externo".format(len(self.personas)))
        except:
            print("el archivo esta vacio")
        finally:
            listaDePersonas.close()    
            del(listaDePersonas)


    def agregarPersonas(self,p):
        self.personas.append(p)
        self.guardarPersonasArchivoExterno()
    
    def mostrarPersonas(self):
        for p in self.personas:
            print(p)

    def guardarPersonasArchivoExterno(self):
        ListaDePersonas=open("archivo_guardado", "wb")
        pickle.dump(self.personas, ListaDePersonas)
        ListaDePersonas.close()
        del (ListaDePersonas)

    def mostrarInfoArchivoExterno(self):
        print("la informacion del archivo externo es la siguiente: ")
        for p in self.personas:
            print(p)


miLista=ListaPersonas()
personas=Persona("kuka ", "masculino ", 52)
miLista.agregarPersonas(personas)  
miLista.mostrarInfoArchivoExterno()      


