# En un archivo: la serializacion convierte en binario el codigo
import pickle

nombres=["adrian","martin","martina"]

archivo_binario=open("nombres","wb")
    #el metodo open recibe por parametro el nombre de la lista y los permisos escritura w y b de binario

pickle.dump(nombres,archivo_binario)
    #se vuelca el archivo al binario y crear el archivo "nombres" en binario

archivo_binario.close()

del (archivo_binario) # se puede borrar si lo deseamos

# ====== DESEREALIZACION DE UN ARCHIVO BINARIO=====

fichero=open("nombres", "rb") #creamos un nuevo archivo q recibe los datos del binario

lista=pickle.load(fichero) #crea la lista con el archivo nuevo

print(lista)