import random

numero_secreto = random.randint(1, 100)
intentos = 0
max_intentos = 5
ganaste = False

print("Adivina el número entre 1 y 100")

while intentos < max_intentos:
    try:
        intento = int(input("Ingresa tu número: "))
        intentos += 1

        if intento == numero_secreto:
            print("Ganaste")
            ganaste = True
            break
        elif intento < numero_secreto:
            print("Muy bajo")
        else:
            print("Muy alto")

    except ValueError:
        print("Ingresa un número válido")

if not ganaste:
    print("Perdiste. El número era:", numero_secreto)
