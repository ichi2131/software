# Caja registradora simple

producto = input("Producto: ").strip()
precio_txt = input("Precio unitario: ").strip()
cantidad_txt = input("Cantidad: ").strip()
dinero_txt = input("Dinero del cliente: ").strip()

try:
    precio = float(precio_txt)
    cantidad = int(cantidad_txt)
    dinero = float(dinero_txt)

    if precio <= 0 or cantidad <= 0 or dinero <= 0:
        print("Error: precio, cantidad y dinero deben ser mayores que 0.")
    else:
        total = precio * cantidad

        if dinero >= total:
            cambio = dinero - total
            print(f"Total: ${total:.2f}")
            print(f"Cambio: ${cambio:.2f}")
        else:
            print(f"No alcanza el dinero. Total: ${total:.2f}")

except:
    print("Error: debe ingresar números válidos.")