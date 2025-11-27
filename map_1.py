# ejemplo funcion map

class Empleado:
    def __init__(self, nombre, cargo, salario):
        self.nombre=nombre
        self.cargo=cargo    
        self.salario=salario
    def __str__(self):
        return "{} que trabaja como {} tiene un salario de USD$ {}".format(self.nombre, self.cargo, self.salario)
    
    
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


print("=========== Aplicando comision del 10% con map y lambda =============")

#ejemplo funcion map
def caluculo_comision(empleado):
    if (empleado.salario<3000):
        empleado.salario=empleado.salario*1.10
    return empleado

empleados_con_comision=list(map(caluculo_comision, ListaEmpleados))

for empleado in empleados_con_comision:
    print(empleado) 

# Ahora utilizando una funcion lambda