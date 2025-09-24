from tkinter import *

raiz=Tk()  #crea la ventana

formulario=Frame(raiz, width=500, height=600) 
#crea el contenedor dentro de la ventana

formulario.pack()
#miFrame.pack() le dice a Tkinter que coloque ese marco en la ventana 
# usando el gestor de geometría pack().


#===== Entry - entradas del formulario =====
nombre=Entry(formulario)
nombre.grid(row=0, column=1, padx=15, pady=15)
nombre.config(fg="green", justify="left")

apellido=Entry(formulario)
apellido.grid(row=1,column=1, padx=15, pady=15)
apellido.config(fg="green" , justify="left")

telefono=Entry(formulario)
telefono.grid(row=2, column=1, padx=15, pady=15)
telefono.config(fg="green", justify="left")

email=Entry(formulario)
email.grid(row=3, column=1, padx=15, pady=15)
email.config(fg="green", justify="left")

textArea=Text(formulario, width=15, height=10) # no son pixels, son cantidad de caracteres
textArea.grid(row=4,column=1, padx=15,pady=15)
textArea.config(fg="blue")

scrollVertical=Scrollbar(formulario, command=textArea.yview) #yview scroll en verical eje y
scrollVertical.grid(row=4, column=2, sticky="nsew") #north south east west toda el espacio
textArea.config(yscrollcommand=scrollVertical.set) #para q el scroll se mueva en el textArea

#==== LABEL =====
# sticky se usa con el método grid() para controlar la disposición de los widgets en filas y columnas. 
nombreLabel=Label(formulario, text="Nombre:")
nombreLabel.grid(row=0,column=0, sticky="w",padx=15, pady=15)

apellidoLabel=Label(formulario, text="Apellido: ")
apellidoLabel.grid(row=1, column=0, sticky="w", padx=15,pady=15)

telefonoLabel=Label(formulario, text="Telefono: ")
telefonoLabel.grid(row=2, column=0, sticky="w",padx=15, pady=15)

emailLabel=Label(formulario, text="Email: ")
emailLabel.grid(row=3,column=0, sticky="w",padx=15, pady=15)

textoLabel=Label(formulario, text="Escribenos: ")
textoLabel.grid(row=4, column=0, sticky="n", padx=15, pady=15)

def botonEnviar():
    print("se envio el mensaje correctamente!!")

enviar=Button(raiz, text="Enviar!", command=botonEnviar)
enviar.pack()

raiz.mainloop()
#¿Qué hace mainloop()? Es un bucle infinito que:
# Mantiene la ventana abierta mientras el usuario no la cierre.
# Escucha eventos como clics, teclas, movimientos del mouse.
# Ejecuta funciones asociadas a esos eventos (por ejemplo, si hacés clic en un botón).
# Actualiza la interfaz en tiempo real según las acciones del usuario.
