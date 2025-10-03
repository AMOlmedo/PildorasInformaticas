from tkinter import *
from tkinter import messagebox  #para importar las ventas emergentes
from tkinter import filedialog  #
root=Tk()

barraMenu=Menu(root)
root.config(menu=barraMenu, width=300, height=200)

def abrirFile():
    archivo=filedialog.askopenfilename(title="Abrir", initialdir="C:", filetypes=(("Archivos Python", "*.py"),("Archivos Texto","*.txt" ))) 
    print(archivo)

def about():
    messagebox.showinfo("Info del Soft", "Version 1.0.0 - 2025")

def avisoOffLine():
    messagebox.showwarning("Ayuda Off Line", "Solo informacion en repositorio Local")

def avisoOnLine():
    messagebox.showerror("Internet", "Debe tener salida a Internet")

def salirApp():
    valor=messagebox.askquestion("Salir", "Desea salir de la Aplicacion?")
    if valor =="yes":
        root.destroy()
def guardarApp():
    saveApp=messagebox.askokcancel("Guardar", "Desea guardar los cambios?")
    if saveApp==False:
        root.destroy()
def reintentar():
    conxion=messagebox.askretrycancel("Reintenar", "Verifique la conexion a internet")

#Button(root, text="Open File", command=abrirFile).pack()

archivoFile=Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="File", menu=archivoFile)
archivoFile.add_cascade(label="New")
archivoFile.add_cascade(label="Open", command=abrirFile)
archivoFile.add_cascade(label="Save", command=guardarApp)
archivoFile.add_cascade(label="Save as")
archivoFile.add_separator()
archivoFile.add_cascade(label="Exit", command=salirApp)

archivoEdit=Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Edit", menu=archivoEdit)
archivoEdit.add_command(label="Copy")
archivoEdit.add_command(label="Cut")
archivoEdit.add_command(label="Paste")
archivoEdit.add_separator()
archivoEdit.add_command(label="Find")

archivoTools=Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Tools", menu=archivoTools)
archivoTools.add_command(label="Run")
archivoTools.add_command(label="Terminal", command=reintentar)
archivoTools.add_command(label="Zip")
archivoTools.add_separator()
archivoTools.add_command(label="Go To")

archivoHelp=Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Help", menu=archivoHelp)
archivoHelp.add_command(label="on line", command=avisoOnLine)
archivoHelp.add_command(label="off line", command=avisoOffLine)
archivoHelp.add_separator()
archivoHelp.add_command(label="About", command=about)

root.mainloop()