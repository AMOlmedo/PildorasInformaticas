# Crea un programa que pida introducir una dirección de email por teclado.
# El programa debe imprimir en consola si la dirección de email es correcta o no en función de si esta tiene el símbolo ‘@’. 
# Si tiene una ‘@’ la dirección será correcta. Si tiene más de una o ninguna ‘@’ la dirección será errónea. 
# Si la ‘@’ está al comienzo de la dirección de email o al final, la dirección también será errónea,

email=input("Ingresa la direccion de email: ")

i=0
for i in email:
    if i == "@":
        break
   

print(email + " es valido ")

# El método rfind() se usa para encontrar la última aparición de una subcadena dentro de una cadena, devolviendo el índice inicial de esta última ocurrencia
# El método count() se aplica a secuencias como cadenas (strings), listas y tuplas para contar el número de ocurrencias de un elemento específico dentro de esa secuencia
# El método find() es una función de cadena que busca la primera aparición de una subcadena dentro de una cadena mayor y devuelve el índice de su posición