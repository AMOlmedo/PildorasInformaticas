import pickle
#La librería Pickle de Python se usa para serializar y deserializar objetos. 
# Esto significa que puedes convertir un objeto de Python en una secuencia de 
# bytes (serialización) y luego reconstruir el objeto original a partir de esa secuencia
# de bytes (deserialización).

class Cliente:
    def __init__(self, nombre, apellido, direccion, telefono):
        self.nombre=nombre
        self.apellido=apellido
        self.direccion=direccion
        self.telefono=telefono
        print("Se ha creado el Cliente: ", self.nombre, self.apellido)
    def __str__(self):  #le da formato de cadena  de caracter, de lo contrario imprime algo asi <__main__.Cliente object at 0x000001CCB09DB140>
        return f"{self.nombre}{self.apellido}{self.direccion}{self.telefono}"


class ListaClientes:
    lista_clientes=[]
    #este constructor es para crear el archivo binario externo
    def __init__(self): 
        ListaDeCliente=open("archivo_externo_binario", "ab+") #ab+ permiso para agregar al binario
        ListaDeCliente.seek(0) #desplaza el cursor a la posicion 0 para ser leido
        try:
            self.lista_clientes=pickle.load(ListaDeCliente)
            print(f"se cargaron {len(self.lista_clientes)} clientes en el archivo externo")
        except:
            print("el archivo esta vacio, es la primera interaccion")
        finally:
            ListaDeCliente.close()
            del(ListaDeCliente)

    def addCliente(self,c):
        self.lista_clientes.append(c)
        self.guardarClienteArchivoExterno()
    
    def MostrarCliente(self):
        for c in self.lista_clientes:
            print(c)
    
    def guardarClienteArchivoExterno(self):  #guarda en el archivo externo
        ListaDeClientes=open("archivoExterno","wb")
        pickle.dump(self.lista_clientes, ListaDeClientes) # vuelca la info de la lista al archivobinario
        ListaDeClientes.close()
        del(ListaDeClientes)
    
    def mostrarInfoArchivoExterno(self):
        print("la info del archivo externo es: ")
        for c in self.lista_clientes:
            print(c)
    
misclientes=ListaClientes() #creo el objeto "misclientes"
cliente=Cliente("marti ", "olme ", "maipu ", "1234")
misclientes.addCliente(cliente)

misclientes.mostrarInfoArchivoExterno()
