from collections import deque

def mostrar_matriz(matriz):
    for fila in matriz:
        print("|", " | ".join(map(str, fila)), "|")
        print("|---|---|---|")

def encontrar_cero(matriz):
    for i, fila in enumerate(matriz):
        if 0 in fila:
            return i, fila.index(0)

def mover(matriz, movimiento):
    i, j = encontrar_cero(matriz)
    nueva_matriz = [fila[:] for fila in matriz]
    movimientos = {'izquierda': (0, -1), 'derecha': (0, 1), 'arriba': (-1, 0), 'abajo': (1, 0)}

    if movimiento in movimientos:
        di, dj = movimientos[movimiento]
        ni, nj = i + di, j + dj
        if 0 <= ni < 3 and 0 <= nj < 3:
            nueva_matriz[i][j], nueva_matriz[ni][nj] = nueva_matriz[ni][nj], nueva_matriz[i][j]
            return nueva_matriz
    return None

def resolver_puzzle(matriz_inicial, matriz_final):
    frontera = deque([(matriz_inicial, [])])
    explorados = set()

    while frontera:
        matriz_actual, camino = frontera.popleft()
        explorados.add(tuple(map(tuple, matriz_actual)))

        if matriz_actual == matriz_final:
            return camino

        for movimiento in ['izquierda', 'derecha', 'arriba', 'abajo']:
            nueva_matriz = mover(matriz_actual, movimiento)
            if nueva_matriz is not None and tuple(map(tuple, nueva_matriz)) not in explorados:
                frontera.append((nueva_matriz, camino + [movimiento]))

    return None

matriz_inicial = [
    [7, 2, 4],
    [5, 0, 6],
    [8, 3, 1]
]

matriz_final = [
    [8, 7, 6],
    [5, 4, 3],
    [2, 1, 0]
]

print("Matriz Inicial:")
mostrar_matriz(matriz_inicial)

camino = resolver_puzzle(matriz_inicial, matriz_final)

if camino is not None:
    costo_total = len(camino)
    coordenadas_finales = encontrar_cero(matriz_inicial)
    for i, movimiento in enumerate(camino, start=1):
        print(f"Paso {i}: Mover {movimiento}")
        matriz_inicial = mover(matriz_inicial, movimiento)
        print("Nueva Matriz:")
        mostrar_matriz(matriz_inicial)
        coordenadas_finales = encontrar_cero(matriz_inicial)
        print(f"Cordenadas de la posición del valor 7: ({coordenadas_finales[0]},{coordenadas_finales[1]})")

    print(f"Costo total de los movimientos: {costo_total}")
    print(f"Cordenadas finales de la posición del valor 7: ({coordenadas_finales[0]},{coordenadas_finales[1]})")
else:
    print("No se encontró una solución.")