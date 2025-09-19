from tkinter import *

root=Tk()

miFrame=Frame(root, width=500, height=400)
miFrame.pack()

miLebel= Label(miFrame, text="hola mundo",fg="red", font=(20))
miLebel.place(x=100, y=200) #lo ubica por coordenadas
miLebel.config(bg="yellow")

#miImagen=PhotoImage(file="just_tri.gif")
#miLebel2=Label(image=miImagen)
root.mainloop()