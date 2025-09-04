## las tuplas no se puede modificar
miTupla=(10,20,30, "decada")
print(miTupla[3])

miLista=list(miTupla)  ##convierte lista a tupla
print(miTupla)

miLista=["Adrian", 50, 21.1,"olmedo", True]
miTupla=tuple(miLista)  ##convierte  tupla a lista
print(miTupla)

##count
miLista=["Adrian", 50, 50, 50,  21.1,"olmedo", True]
miTupla=tuple(miLista)
print(miTupla.count(50)) ##cuenta la cantidad de veces q tiene el elem 50

##len   da la cantidad de elementos
print(len(miTupla))

miTupla2=("adri",)  ##tupla unitaria
print(len(miTupla2))
print("----------")

tupla3=("adrian", 28, 8, 73)
nombre, dia, mes, year=tupla3 ##desempaquetado de tupla
print(nombre)
print(year)
print(mes)

