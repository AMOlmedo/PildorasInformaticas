from tkinter import *

root=Tk()

miFrame=Frame(root,width=400,height=300)
miFrame.pack()

#======ENTRY======
cuadroNombre=Entry(miFrame)
cuadroNombre.grid(row=0,column=1, padx=10, pady=10) #padx y pady es la distancia al borde del contenedor
cuadroNombre.config(fg="red", justify="center")

cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=1,column=1, padx=10, pady=10) # 10px arriba  y abajo  y 10px a izp y derecha

cuadroEdad=Entry(miFrame)
cuadroEdad.grid(row=2,column=1, padx=10, pady=10)

cuadroPass=Entry(miFrame)
cuadroPass.grid(row=3,column=1, padx=10, pady=10)
cuadroPass.config(show="*")  #muestra asteriscos por seguridad

areaTexto=Text(miFrame, width=15, height=5)
areaTexto.grid(row=3, column=1, padx=10, pady=10)
areaTexto.config(fg="red", bg="gray",)

scrollv=Scrollbar(miFrame, command=areaTexto.yview)
scrollv.grid(row=3, column=2, sticky="nsew")
areaTexto.config(yscrollcommand=scrollv.set)

#======LABEL======

nombreLabel=Label(miFrame, text="Nombre: ")
nombreLabel.grid(row=0,column=0, sticky="w", padx=10, pady=10)  #w west, a la izquierda

apellidoLabel=Label(miFrame, text="Apellido: ")
apellidoLabel.grid(row=1,column=0, sticky="w", padx=10, pady=10)

edadLabel=Label(miFrame, text="Edad: ")
edadLabel.grid(row=2,column=0, sticky="w", padx=10, pady=10)

passLabel=Label(miFrame, text="Password: ")
passLabel.grid(row=3,column=0, sticky="w", padx=10, pady=10)

textoLabel=Label(miFrame, text="Mensaje")
textoLabel.grid(row=4, column=0, padx=10, pady=10)

def enviar():
    print("se envio el mensaje")

enviarbtn=Button(root, text="enviar mensaje", command=enviar)
enviarbtn.pack()

root.mainloop()
