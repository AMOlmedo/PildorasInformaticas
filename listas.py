## las listas son array q se pueden modifica
miLista=["Adrian", 50, 21.1,"olmedo", True]
##distintos ejemplos
print(miLista)
print(miLista[0])
print(miLista[-2])
print(miLista[0:2])
print(miLista[1:2])
print(miLista[2:])

miLista.append(235470008) ##agrega un  elem al final
print(miLista)

miLista.insert(2, "martin") ##insert elemtos en la posicion indicada
print(miLista)

miLista.extend([6554,"Pedregal"])  ##agrega elemento al final de la lista
print(miLista)

print(miLista.index(50))##devuelve la posicion del elemnto solicitado

print(21.1 in miLista)

miLista.remove("olmedo")
print(miLista)

miLista.pop() ##elimina el ultimo valor de la lista
print(miLista)

miLista2=[12.5, 20.45]
miLista3=[miLista  + miLista2] ##concatenal dos listas
print(miLista3) 

miLista4=["Adrian", 50, 21.1,"olmedo", True] * 3
print(miLista) 

      






