Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import random
... 
... numero_secreto = random.randint(1, 100)
... intentos = 0
... max_intentos = 5
... 
... print("Adivina el número entre 1 y 100")
... 
... while intentos < max_intentos:
...     intento = int(input("Ingresa tu número: "))
...     intentos += 1
... 
...     if intento == numero_secreto:
...         print("¡Ganaste!")
...         break
...     elif intento < numero_secreto:
...         print("Muy bajo")
...     else:
...         print("Muy alto")
... 
... if intento != numero_secreto:
