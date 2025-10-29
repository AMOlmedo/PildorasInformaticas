
def fibonacci(n):
    secuencia=[0,1]
    while len(secuencia)<n:
        siguiente=secuencia[-1]+ secuencia[-2]
        secuencia.append(siguiente)
    return secuencia

n = int(input("ingrese n numeros de la serie: "))
secuencia=fibonacci(n)
print(secuencia)