# raiz cuadrada de un numero
import math

numero = int(input("Ingresa un numero:"))
intentos = 0
while numero<0:
    print("numero negativo")
    if intentos ==2:
        print("limite cantidad de intentos")
        break
    numero = int(input("Ingresa un numero:"))
    if numero<0:
        intentos=+1
if intentos<2:
    raiz_cuadrada=math.sqrt(numero)
    print("la raiz cuadrada de " + str(numero) + " es " + str(raiz_cuadrada) )





