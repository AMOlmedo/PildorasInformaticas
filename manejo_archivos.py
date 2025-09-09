from io import open

archivo_texto =open("archivo.txt", "w") # open es el metodo  q crea el archico
# pide dos argumetntos, nombre el archivo y w de write es el modo que usaremos al archivo
#  q se utiliza
#esto crea el arcivo.txt automaticamente

frase="archivo creado por py \n el un ejemplo hay que respetar las fases: creacion, apertura, manipulacion y cierre  \nluego se modificara el archivo.txt"

archivo_texto.write(frase)

archivo_texto.close()
