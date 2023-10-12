def main():
    matriz = [[0 for _ in range(3)] for _ in range(3)]
    pantalla_inicial(matriz)
    
    while not is_game_over(matriz):
        imprimir_pantalla(matriz)
        sig_mov = input("Realiza el siguiente movimiento (arriba, abajo, izquierda, derecha, o 'salir' para salir): ")
        if sig_mov.lower() == 'salir':
            print("Fin del juego")
            break
        mover(matriz, sig_mov)
    
    if is_game_over(matriz):
        imprimir_pantalla(matriz)
        print("¡Felicidades, has ganado!")
    return

def pantalla_inicial(matriz):
    print("El juego ha iniciado")
    matriz_inicial = [
        ["7", "2", "4"],
        ["5", " ", "6"],
        ["8", "3", "1"],
    ]
    for fila in range(3):
        for columna in range(3):
            matriz[fila][columna] = matriz_inicial[fila][columna]

def imprimir_pantalla(matriz):
    for matriz in matriz:
        print(" ".join(matriz))

def localizar_espacio(matriz):
    for fila in range(3):
        for columna in range(3):
            if matriz[fila][columna] == ' ':
                return fila, columna

def is_game_over(matriz):
    win_conditions = [
        [" ", "1", "2"],
        ["3", "4", "5"],
        ["6", "7", "8"]
    ]
    return matriz == win_conditions

def mover(matriz, movimiento):
    espacio_fila, espacio_columna = localizar_espacio(matriz)
    
    if movimiento == 'arriba':
        nueva_fila = espacio_fila - 1
        nueva_columna = espacio_columna
    elif movimiento == 'abajo':
        nueva_fila = espacio_fila + 1
        nueva_columna = espacio_columna
    elif movimiento == 'izquierda':
        nueva_fila = espacio_fila
        nueva_columna = espacio_columna - 1
    elif movimiento == 'derecha':
        nueva_fila = espacio_fila
        nueva_columna = espacio_columna + 1
    else:
        print("Movimiento no válido")
        return
    
    if 0 <= nueva_fila < 3 and 0 <= nueva_columna < 3:
        matriz[espacio_fila][espacio_columna], matriz[nueva_fila][nueva_columna] = matriz[nueva_fila][nueva_columna], matriz[espacio_fila][espacio_columna]

if __name__ == "__main__":
    main()
