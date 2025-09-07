# ejemplo de excepciones 
import math

def division():
    try:
        num1=(float(input("Ingrese el 1er numero: ")))
        num2=(float(input("Ingrese el 2er numero: ")))
    except ValueError:         # es una clase predefinida
        print("Ingrese numeros")

    except ZeroDivisionError:  # es una clase predefinida
        print("no se puede dividir por 0") 
    finally:   # se ejecuta si o si
        print("FIN")   
        
    print("el resultado es: " + str(num1/num2))

def raiz_cuadrara():
    num3 = (float(input("ingrese un numero para calcular la raiz: ")))
    if num3 < 0:
        raise ValueError ("el numero no puede ser negativo")
    else:
        return math.sqrt(mum3)

    
    try:
        print(raiz_cuadrara(num3))
    except ValueError as ErrorNuemroNegativo:
        print(ErrorNuemroNegativo)

division()
raiz_cuadrara()
print("FIN")