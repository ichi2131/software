def solicitar_temperatura() -> int:

    while True:
        entrada = input("Ingresa la temperatura (18-30 °C): ").strip()

        # Verificar que la entrada sea un número entero
        try:
            temperatura = int(entrada)
        except ValueError:
            print("Error: Debes ingresar un número entero. Por favor, intenta de nuevo.")
            continue

        # Validar el rango permitido
        if 18 <= temperatura <= 30:
            print("✅ Temperatura válida. Proceso completado.")
            return temperatura

        print("Error: La temperatura debe estar entre 18 y 30 grados. Intenta de nuevo.")


if __name__ == "__main__":
    solicitar_temperatura()
