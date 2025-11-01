import random

def adivinar_numero():
    num_secreto=random.randint(1,100)
    intentos=0
    while   True:
        numero=int(input('Adivina el numero'))
        if numero < num_secreto:
            print('es mayor')
        elif numero > num_secreto:
            print('es menor')
        else: 
            print(f'acertaste en {intentos}')
        break
    intentos +=1

adivinar_numero()

        
    
