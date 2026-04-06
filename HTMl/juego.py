import os
import random
import time


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def mostrar_ayuda(palabra, num_letras):
    indices = random.sample(range(len(palabra)), num_letras)
    pistas = {i: palabra[i] for i in indices}

    resultado = ""
    for i in range(len(palabra)):
        if i in pistas:
            resultado += palabra[i] + " "
        else:
            resultado += "_ "
    return resultado.strip()


def turno_adivinar(jugador, palabra):
    clear()
    print(f"🔎 Turno de {jugador} para adivinar")
    print(f"La palabra tiene {len(palabra)} caracteres.")
    print("_ " * len(palabra))
    print("\nTienes 3 intentos.")

    ayudas_disponibles = ["ayuda1", "ayuda2", "ayuda3"]
    random.shuffle(ayudas_disponibles)

    intentos = 3

    while intentos > 0:
        print("\nOpciones:")
        print("1) Adivinar palabra")
        print(f"2) Pedir ayuda ({len(ayudas_disponibles)} disponibles)")
        op = input("Elige opción: ").strip()

        if op == "1":
            intento = input("Ingresa tu intento: ").strip().lower()
            if intento == palabra:
                print("🎉 ¡Correcto! Ganaste esta ronda.")
                time.sleep(1.5)
                return True
            else:
                intentos -= 1
                print("❌ Incorrecto.")
                print(f"Intentos restantes: {intentos}")

        elif op == "2":
            if not ayudas_disponibles:
                print("No quedan ayudas.")
                continue

            ayuda = ayudas_disponibles.pop(0)

            if ayuda == "ayuda1":
                print("\n🟦 Ayuda 1 → Revela 1 letra:")
                print(mostrar_ayuda(palabra, 1))

            elif ayuda == "ayuda2":
                print("\n🟩 Ayuda 2 → Revela 2 letras:")
                print(mostrar_ayuda(palabra, 2))

            elif ayuda == "ayuda3":
                print("\n🟥 Ayuda 3 → Revela 3 letras:")
                cant = min(3, len(palabra))
                print(mostrar_ayuda(palabra, cant))

        else:
            print("Opción inválida.")

    print(f"\n💀 Se acabaron los intentos. La palabra era: {palabra}")
    time.sleep(2)
    return False


def jugar_ronda(jugador_palabra, jugador_adivina):
    clear()
    print(f"✏️ {jugador_palabra}, escribe una palabra secreta.")
    palabra = input("Palabra: ").strip().lower()
    while not palabra.isalpha():
        palabra = input("Solo letras, escribe otra palabra: ").strip().lower()

    clear()
    print(f"🔒 Palabra guardada. Turno de {jugador_adivina}.")
    time.sleep(1)

    return turno_adivinar(jugador_adivina, palabra)


def main():
    clear()
    print("=== 🔤 JUEGO DE ADIVINAR PALABRAS — 2 JUGADORES ===\n")
    jugador1 = input("Nombre del Jugador 1: ")
    jugador2 = input("Nombre del Jugador 2: ")

    puntos1 = 0
    puntos2 = 0

    ronda = 1

    while puntos1 < 2 and puntos2 < 2:
        clear()
        print(f"=== RONDA {ronda} ===")
        print(f"Puntaje: {jugador1} {puntos1} — {puntos2} {jugador2}")
        print("\nTurno de colocar palabra y turno de adivinar alternan cada ronda.")
        time.sleep(2)

        if ronda % 2 == 1:
            gano = jugar_ronda(jugador1, jugador2)
            if gano:
                puntos2 += 1
        else:
            gano = jugar_ronda(jugador2, jugador1)
            if gano:
                puntos1 += 1

        ronda += 1

    clear()
    print("=== RESULTADO FINAL ===")
    print(f"{jugador1}: {puntos1} puntos")
    print(f"{jugador2}: {puntos2} puntos")

    if puntos1 > puntos2:
        print(f"\n🏆 ¡{jugador1} gana el juego!")
    else:
        print(f"\n🏆 ¡{jugador2} gana el juego!")

    print("\nGracias por jugar 🎉")


if __name__ == "__main__":
    main()
