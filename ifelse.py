# pildoras
edad=int(input("ingresar edad: "))
if 0<edad<111:  
    if edad >=110: 
        print(" edad incorrecta") 
    elif edad>=18:
        print("puede votar") 
    else:
        print("no puede votar")
else:
    print("ingrese una edad valida!")
  
print("-----ejemplo #2-------")

nota=int(input("ingrese la nota: "))

if nota<3:
    print("desaprobado")
elif nota<6:
    print("aprobado")
elif nota<8:
    print("MB")
else:
    print("exclente")

