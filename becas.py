# Beca si se cumple las  3 condiciones: 40Km, 2 bro y $1000
print("Ingrese los datos para evaluar la beca")
distancia = int(input("Ingrese la distacia: "))
hermanos = int(input("Ingrese la candidad de hermanos: "))
salario = int(input("Ingrese el salario: "))

if distancia>=40 and hermanos>=2 and salario<1000:
    print("corresponde beca")
else: 
    print("no corresponde beca")