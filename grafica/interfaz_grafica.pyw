from tkinter import *

raiz=Tk()
raiz.title("ventana de prueba")
raiz.resizable(1,0) #recibe parametros booleanos 1=true 0=False
#tambien puede ir True o False ei los parametros.
#el primer parametro es para el width y el segundo height

raiz.iconbitmap() #para cambiar el icono de la ventana
raiz.geometry("400x200") #tamanio de la ventana
raiz.config(bg="yellow")
# creacion del frame
miFrame=Frame()
miFrame.pack(side="left", anchor="n") #n de notth, s de south utiliza los puntos cardinales
miFrame.config(bg="gray")
miFrame.config(width="200", height="150")
miFrame.config(bd="15") #bd border
miFrame.config(cursor="hand2")
 #.config hay q ver tiene muchas utilidades

raiz.mainloop()  #mainlopp es un bucle infinito para q este a la escucha. Siempre debe estar al final

