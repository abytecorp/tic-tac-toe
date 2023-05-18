# -*- coding: utf-8 -*-

# Crear el tablero
board = [[' ' for _ in range(3)] for _ in range(3)]

# Definir el jugador actual
current_player = 'X'

# Ciclo principal del juego
while True:
    # Mostrar el tablero
    for row in board:
        print('|'.join(row))
        print('-' * 5)

    # Obtener la jugada del jugador
    row = int(input("Ingrese la fila (0-2): "))
    col = int(input("Ingrese la columna (0-2): "))

    # Verificar si la posición está vacía
    if board[row][col] == ' ':
        # Colocar la marca del jugador en la posición seleccionada
        board[row][col] = current_player

        # Verificar si el jugador actual ha ganado
        if (board[row][0] == board[row][1] == board[row][2] == current_player or
            board[0][col] == board[1][col] == board[2][col] == current_player or
            board[0][0] == board[1][1] == board[2][2] == current_player or
            board[0][2] == board[1][1] == board[2][0] == current_player):
            print("¡Jugador", current_player, "ha ganado!")
            break

        # Cambiar al siguiente jugador
        current_player = 'O' if current_player == 'X' else 'X'
    else:
        print("Posición inválida. Intente de nuevo.")

    # Verificar si hay un empate
    if all(board[row][col] != ' ' for row in range(3) for col in range(3)):
        print("¡Empate!")
        break
