#ejemplos de funciones lambda

area_triangulo=lambda base, altura: (base*altura)/2
print("el area del triangulo es: ", area_triangulo(5,4))

def area_triangulo2(base, altura):
    return (base*altura)/2

print("el area del triangulo es: ", area_triangulo2(5,4))

#ejemplo 2

destacar_valor=lambda comision: "USD$ {} !!".format(comision)

comision_vendedor=5000
print(destacar_valor(comision_vendedor))

