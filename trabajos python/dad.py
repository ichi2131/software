#bucle - 1

edad_valida = False

while not edad_valida:

    edad = input("ingrese su edad(en numero)").strip()

    if edad.isdigit():
        edad_limpia = int(edad)
        if edad_limpia >= 18:
            print("bienvenidos, puede pasar")
            edad_valida = True
        else:
                print("no puede pasar, adios pues")

    else:
        print ("ingrese un dato valido ")
        print ("continuemos la chamba")
