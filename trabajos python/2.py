#bucle - 2

sistema_full = True

while sistema_full:
    print("1. arros con pollo")
    print("2. salchipapa")
    print("3. ajiaco")
    print("4. bandeja paisa")
    print("5. salir")

    opcion = input("elija algo del menu (en numero)")

    if opcion == "1":
        print("uds come arroz con pollo")

    elif opcion== "2":
        print("uds come salchipapa")
    elif opcion == "3":
        print(" uds come ajiaco")
    elif opcion== "4":
        print(" uds come bandeja paisa")
    elif opcion == "5":
        print("adios")
        sistema_full = False
    else:
        print("elija una opcion")
