# las LISTAS SON LOS ARRAY EN OTROS LENGUAJES
milista=["adri", "marti", "marce"]
print(milista[:])  #imprime todos los elem de la lista no olvidar los :
print(milista[-1])
print(milista[0:2])  # desde la posicion 0 hasta dos elementos
print(milista[:2])  # desde la posicion 0 hasta dos elementos (sin el cero )
print(milista[1:]) # de la posicion 1 hasta el final

milista.append("kuka")   # para agregar elem al final de la lista
print(milista)

milista.insert(2,"miel") #agrega elme a la lista en la posicion 2
print(milista)

milista.extend(["miti", "rita"]) #agrega VARIOSs elem al final de la lista
print(milista)

print(milista.index("kuka")) #da el indice del elem

print("adri" in milista)  #devuelve V o F  esta el elmen

milista.remove("miti")  #elimina un elemento de la lista
print(milista)

milista.pop()  #elimina el ultimo elem de la lista
print(milista)

