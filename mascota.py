print("mis mascotas")


mascota = input("ingrese nombre de la mascota: ")

opcion = mascota.lower()

if opcion in ("kuka", "rita"):
    print("es mi mascota la " + opcion)
else:
    print(opcion + ", no es mia")

