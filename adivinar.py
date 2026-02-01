import random

minimo = 1
maximo = 10

numero_secreto = random.randint(minimo, maximo)

while True:
    intento = input(f'adivina un numero entre {minimo} y {maximo}:')
    intento = int(intento)
    if intento == numero_secreto:
        print("¡Felicidades! Has adivinado el número.")
        break
    elif intento < minimo or intento > maximo:
        print(f"Por favor, introduce un número entre {minimo} y {maximo}.")
    elif intento < numero_secreto:
        print("El número es mayor.")
    else:
        print("El número es menor.")
        
   