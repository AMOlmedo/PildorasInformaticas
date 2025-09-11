import pickle

class Vehiculo():
    def __init__(self, marca, modelo): #constructor
        self.marca=marca
        self.modelo=modelo
        self.enMarcha=False
        self.acelera=False
        self.frena=False
    
    def arrancar(self): #metodo arrancar
        self.enMarcha=True

    def acelerar(self): # metodo acelerar
        self.acelera=True
    
    def frenar(self):  #metodo frenar
        self.frena=True
    
    def estado(self):
        print("Marca:", self.marca, "\nModelo:",self.modelo,"\nEn Marcha:", self.enMarcha,"\nAcelerando: ",self.acelera
              ,"\nFrenando: ", self.frena,)
    
# creamos 3 objetos de la clase vehiculo
auto1= Vehiculo("ford","ka")
auto2= Vehiculo("fiat","uno")
auto3= Vehiculo("vw","gol")

autos=[auto1, auto2, auto3]

# SERIALIZACION
archivo=open("autos_binarios","wb") #nombre el archivo binario y wb permisos
pickle.dump(autos,archivo) # parametros: de donde "autos" hacia donde "archivo"
archivo.close()
del (archivo)

# DESEREALIZACION
archivo_apertura= open("autos_binarios","rb") #aca se lee el binario
misAutos=pickle.load(archivo_apertura)  #aca se carga el binario en una variable nueva
archivo_apertura.close()

for c in misAutos:
    print(c.estado())




        