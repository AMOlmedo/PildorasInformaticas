from tkinter import *
raiz=Tk()
miFrame=Frame(raiz)
miFrame.pack()

 #======pantalla=====
pantalla=Entry(miFrame)
pantalla.grid(row=1,column=1, padx=10, pady=10, columnspan=4) #columnspan ocupa el ancho de 4 columanas
pantalla.config(background="black", fg="#03f943", justify="right")


#====teclado=====




raiz.mainloop()