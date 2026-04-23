valido = False
while not valido:

    entrada = input("Ingresa la temperatura (18-30 °C): ").strip

    if entrada.isdigit():
        temperatura = int(entrada)
        if 18 <= temperatura <= 30:
            print("temperatura válida")
            valido = True
        else:
            print("fuera de rango")
    else:
        print("dato inválido")
