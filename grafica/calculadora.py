from tkinter import *
raiz=Tk()
miFrame=Frame(raiz)
miFrame.pack()
opreracion=""
resultado=0

 #======pantalla=====
numeroPantalla=StringVar()  # ver al pie del archivo
pantalla=Entry(miFrame,textvariable=numeroPantalla)
pantalla.grid(row=1,column=1, padx=10, pady=10, columnspan=4) #columnspan ocupa el ancho de 4 columanas
pantalla.config(background="black", fg="#03f943", justify="right")

#==== puslo teclado=====
def numeroPulsado(num):
    global opreracion
    if opreracion !="": 
        numeroPantalla.set(num)
        opreracion=""
    else:
        numeroPantalla.set(numeroPantalla.get() + num)

def suma(num):
    global opreracion
    global resultado
    resultado+=int(num)
    opreracion="suma" 
    numeroPantalla.set(resultado)

def resta():
    global opreracion
    opreracion="resta"

def el_resultado():
    global resultado
    numeroPantalla.set(resultado + int(numeroPantalla.get()))
    resultado=0

#====teclado fila 1 =====
boton7=Button(miFrame, text="7",width="3",command=lambda:numeroPulsado("7"))
boton7.grid(row=2, column=1)
boton8=Button(miFrame, text="8",width="3",command=lambda:numeroPulsado("8"))
boton8.grid(row=2, column=2)
boton9=Button(miFrame, text="9",width="3",command=lambda:numeroPulsado("9"))
boton9.grid(row=2, column=3)
botonDiv=Button(miFrame, text="/",width="3")
botonDiv.grid(row=2, column=4)
#====teclado fila 2 =====
boton4=Button(miFrame, text="4",width="3", command=lambda:numeroPulsado("4"))
boton4.grid(row=3, column=1)
boton5=Button(miFrame, text="5",width="3",command=lambda:numeroPulsado("5"))
boton5.grid(row=3, column=2)
boton6=Button(miFrame, text="6",width="3",command=lambda:numeroPulsado("6"))
boton6.grid(row=3, column=3)
botonMult=Button(miFrame, text="x",width="3")
botonMult.grid(row=3, column=4)
#====teclado fila 3 =====
boton1=Button(miFrame, text="1",width="3",command=lambda:numeroPulsado("1"))
boton1.grid(row=4, column=1)
boton2=Button(miFrame, text="2",width="3",command=lambda:numeroPulsado("2"))
boton2.grid(row=4, column=2)
boton3=Button(miFrame, text="3",width="3",command=lambda:numeroPulsado("3"))
boton3.grid(row=4, column=3)
botonResta=Button(miFrame, text="-",width="3", command=lambda:resta())
botonResta.grid(row=4, column=4)
#====teclado fila 4 =====
boton0=Button(miFrame, text="0",width="3",command=lambda:numeroPulsado("0"))
boton0.grid(row=5, column=1)
botonComa=Button(miFrame, text=",",width="3",command=lambda:numeroPulsado(","))
botonComa.grid(row=5, column=2)
botonIgual=Button(miFrame, text="=",width="3", command=lambda:el_resultado())
botonIgual.grid(row=5, column=3)
botonSuma=Button(miFrame, text="+",width="3", command=lambda:suma(numeroPantalla.get()))
botonSuma.grid(row=5, column=4)

raiz.mainloop()

# StringVar() es una clase del módulo Tkinter que se utiliza para crear una variable de texto 
# que puede vincularse a widgets de interfaz gráfica como Entry (entrada de texto) y Label (etiqueta).
# Permite una gestión dinámica del contenido del widget, lo que significa que cualquier cambio en la
# variable StringVar se refleja automáticamente en el widget asociado, y viceversa, creando un enlace bidireccional. 

#FUNCION ANONIMA LAMBDA
# En Python, una función lambda es una función anónima, es decir, una función sin nombre,
#  que se define usando la palabra clave lambda. Son útiles para crear funciones pequeñas y
#  de un solo uso en el mismo lugar donde se requieren, sin tener que definirlas formalmente
#  con def. Se utilizan comúnmente con funciones de orden superior como map(), filter() y 
# sorted() para simplificar el código, pero solo pueden contener una única expresión,
#  no múltiples sentencias. 