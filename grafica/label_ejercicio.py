from tkinter import *

root=Tk()

miFrame=Frame(root, width=500, height=400)
miFrame.pack()
#.pack() es uno de los métodos de geometría que ofrece Tkinter para 
# posicionar widgets (como Frame, Button, Label, etc.) dentro de su 
# contenedor (por ejemplo, una ventana o un frame).

miLebel= Label(miFrame, text="hola mundo",fg="red", font=(20))
miLebel.place(x=100, y=200) #lo ubica por coordenadas
miLebel.config(bg="yellow")

#miImagen=PhotoImage(file="just_tri.gif")
#miLebel2=Label(image=miImagen)
root.mainloop()