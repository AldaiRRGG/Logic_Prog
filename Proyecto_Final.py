
# PROYECTO: COMPUTADOR ADIVINA EL NÚMERO
# Autor: Aldair Guallimba
# El usuario piensa un número entre 0 y 50.
# La computadora intenta adivinarlo usando



print("-------------------------------------------")
print("  COMPUTADOR ADIVINA EL NÚMERO")
print("-------------------------------------------")

# Tupla que almacena las respuestas válidas
respuestas_validas = ("mayor", "menor", "correcto")

# Variables para guardar el mejor récord y el número de partidas jugadas
mejor_record = None
partidas_jugadas = 0

# Ciclo principal del programa
while True:

    # Menú principal
    print("\nMENÚ PRINCIPAL")
    print("1. Iniciar juego")
    print("2. Salir")

    opcion = input("Seleccione una opción: ")

    # Si el usuario decide iniciar el juego
    if opcion == "1":

        # Se incrementa el número de partidas jugadas
        partidas_jugadas = partidas_jugadas + 1

        print("\nPiensa un número entre 0 y 50.")
        input("Presiona ENTER cuando estés listo...")

        # Se establecen los límites iniciales
        minimo = 0
        maximo = 50

        # Contador de intentos realizados
        intentos = 0

        # Lista para almacenar el historial de intentos
        historial_intentos = []

        # Ciclo que se ejecuta hasta que la computadora adivine el número
        while True:

            # La computadora calcula un número intermedio
            intento = (minimo + maximo) // 2

            # Se incrementa el contador de intentos
            intentos = intentos + 1

            # Se guarda el intento en la lista
            historial_intentos.append(intento)

            print("\n¿Tu número es", intento, "?")

            # El usuario debe indicar si el número es mayor, menor o correcto
            respuesta = input(
                "Escribe mayor, menor o correcto: "
            ).lower()

            # Validación para aceptar únicamente respuestas válidas
            if respuesta not in respuestas_validas:

                print("Error: solo se permite ingresar texto válido: mayor, menor o correcto.")

            # Si la computadora adivinó correctamente
            elif respuesta == "correcto":

                print("\n¡Adiviné tu número!")
                print("El número es:", intento)
                print("Intentos realizados:", intentos)

                # Se muestra el historial de intentos
                print("Historial de intentos:", historial_intentos)

                # Se verifica si se obtuvo un nuevo récord
                if mejor_record is None or intentos < mejor_record:

                    mejor_record = intentos

                    print("¡Nuevo mejor récord!",
                          mejor_record, "intentos")

                # Mensajes según la cantidad de intentos realizados
                if intentos <= 3:

                    print("¡Excelente! La computadora estuvo muy precisa.")

                elif intentos <= 5:

                    print("Buen trabajo, el número fue encontrado rápidamente.")

                else:

                    print("La computadora necesitó varios intentos.")

                # Se muestra el total de partidas jugadas
                print("Partidas jugadas:", partidas_jugadas)

                # Finaliza la partida actual
                break

            # Si el usuario indica que el número es mayor
            elif respuesta == "mayor":

                # Se verifica que no se exceda el límite máximo
                if intento == 50:

                    print("\nYa se llegó al número máximo permitido.")
                    print("Tu número no puede ser mayor que 50.")
                    print("Revisa tu respuesta.")

                else:

                    # Se actualiza el límite inferior
                    minimo = intento + 1

            # Si el usuario indica que el número es menor
            elif respuesta == "menor":

                # Se verifica que no se exceda el límite mínimo
                if intento == 0:

                    print("\nYa se llegó al número mínimo permitido.")
                    print("Tu número no puede ser menor que 0.")
                    print("Revisa tu respuesta.")

                else:

                    # Se actualiza el límite superior
                    maximo = intento - 1

            # Verifica inconsistencias en las respuestas del usuario
            if minimo > maximo:

                print("\nExiste una inconsistencia en las respuestas ingresadas.")
                print("El programa no puede continuar con esos datos.")

                break

    # Si el usuario decide salir del programa
    elif opcion == "2":

        print("\nGracias por usar el programa.")
        print("Total de partidas jugadas:", partidas_jugadas)

        # Muestra el mejor récord obtenido
        if mejor_record is not None:

            print("Mejor récord obtenido:",
                  mejor_record, "intentos")

        # Finaliza el programa
        break

    # Si el usuario ingresa una opción inválida
    else:

        print("Opción inválida. Ingrese 1 para iniciar o 2 para salir.")