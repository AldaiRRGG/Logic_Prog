# PROYECTO: COMPUTADOR ADIVINA EL NÚMERO
# Autor: Aldair Guallimba
# Descripción:
# El usuario piensa un número entre 0 y 50.
# La computadora intenta adivinarlo según las
# respuestas del usuario: mayor, menor o correcto.



print("COMPUTADOR ADIVINA EL NÚMERO ")
print("Piensa un número entre 0 y 50")

# Se establecen los límites iniciales
minimo = 0
maximo = 50

# Variable para contar los intentos realizados
intentos = 0

# El ciclo se repite hasta que el computador adivine
while True:

    # El computador calcula un número intermedio
    intento = (minimo + maximo) // 2

    # Se incrementa el contador de intentos
    intentos = intentos + 1

    print("¿Tu número es", intento, "?")

    # El usuario indica si el número es mayor,
    # menor o correcto
    respuesta = input(
        "Escribe mayor, menor o correcto: "
    )

    # Si el computador adivinó correctamente
    if respuesta == "correcto":

        print("¡Adiviné tu número!")
        print("Intentos realizados:", intentos)

        # Finaliza el programa
        break

    # Si el número pensado es mayor
    elif respuesta == "mayor":

        # Se actualiza el límite inferior
        minimo = intento + 1

    # Si el número pensado es menor
    elif respuesta == "menor":

        # Se actualiza el límite superior
        maximo = intento - 1

    # Si la respuesta ingresada es incorrecta
    else:

        print("Respuesta no válida.")