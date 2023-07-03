import random


def adivina_el_numero(x):
    
    print("Bienvenido(a)! Adivina el número")
    
    numero_aleatorio = random.randint(1, x)
    
    prediccion = 0
    
    while prediccion != numero_aleatorio:
        prediccion = int(input(f"Adivina un número entre 1 y {x}: "))
        
        if prediccion < numero_aleatorio:
            print("Intentalo de nuevo. El número es demasiado pequeño")
        elif prediccion > numero_aleatorio:
            print("Intentalo de nuevo. El número es muy grande")

    print(f"Felicitaciones! Adivinaste el número {numero_aleatorio} correctamente")


adivina_el_numero(10)
        
        