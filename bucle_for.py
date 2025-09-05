# Ejemplos de for
for i in ["adrian", "martin", "olmedo"]:
    print(i)

print("=============")

for i in ["adrian", "martin", "olmedo"]:
    print(i, end=" ")  #end muestra uno al lado del otro y el estapacio esta en " "

print("======validacion de email=====")

emmail=False
mi_email=input("ingresa una direccion de email: ")
for i in mi_email:
    if i =="@":
        emmail=True
if emmail==True:
    print("es una direccion valida")
else:
    print("es una direccion invalida")

print("======print f =====")

for i in range(5,20,3): # de la pssicion 5 a la 20 con saltos de 3
    print(f"vuelta nuemero {i}")





