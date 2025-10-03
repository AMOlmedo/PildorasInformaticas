from tkinter import *

root=Tk()
root.title(" Lista de tareas:")

Label(root, text="Lista de tareas TO_DO").pack()

task1=IntVar()
task2=IntVar()
task3=IntVar()
task4=IntVar()
task5=IntVar()

def seleccionar():
    opcion=""
    if(task1==1):
        opcion+="tarea 1 seleccionada"

Checkbutton(root, text="Task1: ", variable=task1, onvalue=1, offvalue=0, command=seleccionar).pack()
Checkbutton(root, text="Task2: ", variable=task1, onvalue=1, offvalue=0, command=seleccionar).pack()
Checkbutton(root, text="Task3: ", variable=task1, onvalue=1, offvalue=0, command=seleccionar).pack()
Checkbutton(root, text="Task4: ", variable=task1, onvalue=1, offvalue=0, command=seleccionar).pack()
Checkbutton(root, text="Task5: ", variable=task1, onvalue=1, offvalue=0, command=seleccionar).pack()


root.mainloop()
