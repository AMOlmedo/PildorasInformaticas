# suma resta multiplicacion y division de dos numeros con manejo de excepciones
def suma(num1,num2):
    return num1 + num2
def resta(num1,num2):
    return num1 - num2
def multiplicacion(num1, num2):
    return num1 * num2
def division(num1,num2):
    try:                 # manejo de execpciones
        return num1 / num2
    except ZeroDivisionError:
        print("No se puede dividir por 0")
        return "Operacion no valida"

var1 = (int(input("ingrese el 1er numero: ")))
var2 = (int(input("ingrese el 2do numero: ")))

opcion = input("Ingrea la operacion deseada de suma, resta, multiplicacion, division: ")
operacion=opcion.lower()

if operacion == "suma":
    print(suma(var1,var2))
elif operacion == "resta": 
    print(resta(var1,var2))
elif operacion=="multiliplicacion":
    print(multiplicacion(var1,var2))
elif operacion == "division":
    print(division(var1,var2))
else:
    print("minguna opocion es correcta")