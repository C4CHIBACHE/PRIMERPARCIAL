def es_perfecto(n):
    if n <= 0:
        return False
    suma_divisores = 0
    for i in range(1, n):
        if n % i == 0:
            suma_divisores += i
    return suma_divisores == n

def cantidad_leds(numero):
    mapa_leds = {
        0: 6,
        1: 2,
        2: 5,
        3: 5,
        4: 4,
        5: 5,
        6: 6,
        7: 3,
        8: 7,
        9: 6
    }

    total_leds = 0
    if numero == 0:
        return mapa_leds[0]

    while numero > 0:
        digito = numero % 10
        total_leds += mapa_leds[digito]
        numero //= 10
    return total_leds


def menu():
    while True:
        print("\n=== MENÚ DE OPCIONES ===")
        print("1. Verificar si un número es perfecto")
        print("2. Calcular la cantidad de LEDs necesarios para un número")
        print("3. Salir")
        
        opcion = input("Selecciona una opción (1-3): ")

        if opcion == '1':
            numero = int(input("Introduce un número entero: "))
            if es_perfecto(numero):
                print(f"{numero} es un número perfecto.")
            else:
                print(f"{numero} no es un número perfecto.")
        
        elif opcion == '2':
            numero = int(input("Introduce un número entero: "))
            leds = cantidad_leds(numero)
            print(f"Se necesitan {leds} LEDs para representar el número.")
        
        elif opcion == '3':
            print("Saliendo del programa. ¡Hasta luego!")
            break
        
        else:
            print("Opción no válida. Intenta nuevamente.")


menu()



