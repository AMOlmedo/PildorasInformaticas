# Crea un programa que pida dos números por teclado. 
# El programa tendrá una función llamada “DevuelveMax” encargada 
# de devolver el número más alto de los dos introducidos.
def devuelveMax():
    num1=int(input("ingrese el primer numero: "))
    num2=int(input("ingrese el segundo numero: "))


    if num1 > num2:
        print("el numero " + num1 + "es mayor")
    else:
        print(" el numero " + num2 + "es mayor")

print("fin")