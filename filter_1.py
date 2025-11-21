def num_par(num):
    if num % 2 ==0:
        return True
    else:
        return False
    
numeros=[1,2,3,4,5,6,7,8,9,10]

#list para dar formato de lista al resultado de filter
#filter aplica la funcion num_par a cada elemento de la lista numeros
#recibe dos parametros: la funcion y la lista
numeros_pares=list(filter(num_par, numeros))
print(numeros_pares)

# Ahora utilizando una funcion lambda
numeros_pares_lambda=list(filter(lambda num: num % 2 ==0, numeros))
print(numeros_pares_lambda)

# Ejemplo Filter con objetos de una clase

class Empleado:
    def __init__(self, nombre, cargo, salario):
        self.nombre=nombre
        self.cargo=cargo    
        self.salario=salario
    def __str__(self):
        return "{} que trabaja como {} tiene un salario de {}".format(self.nombre, self.cargo, self.salario)
    
ListaEmpleados=[
    Empleado("Juan", "Director", 7500),
    Empleado("Ana", "Presidente", 8500),
    Empleado("Antonio", "Administrativo", 2500),
    Empleado("Maria", "Secretaria", 2700),
    Empleado("Lucia", "Administrativo", 2400),
]

salarios_altos=list(filter(lambda empleado: empleado.salario>5000, ListaEmpleados))
#saleios altos recibe como parametros la funcion lambda y la lista de empleados
for empleado in salarios_altos:
    print(empleado)

