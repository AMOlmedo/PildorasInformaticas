print("Estado del Alumno")
nota_al=input("ingrese la nota: ")  ##hay q convertir String a int
##se puede colocar un String en el argunmento del input
def evaluacion(nota):
    valoracion="aprobado"
    if nota<7:
        valoracion="suspenso"
    return valoracion
print(evaluacion(int(nota_al))) ##convierte a int y nota_al es el parametros de la fnc