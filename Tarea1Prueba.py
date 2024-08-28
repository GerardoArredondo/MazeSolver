from collections import deque

class Estado:
    def __init__(self, board, moves=0, previous=None):
        self.board = board
        self.moves = moves
        self.previous = previous

    def finalizar(self):
        return self.board == [1, 2, 3, 4, 5, 6, 7, 8, 0]

    def obtener_vecinos(self):
        def swap(board, i, j):
            nuevoArray = board[:]
            nuevoArray[i], nuevoArray[j] = nuevoArray[j], nuevoArray[i]
            return nuevoArray

        vecinos = []
        zero_index = self.board.index(0)
        movimientos_posibles = []

        # Movimiento arriba
        if zero_index >= 3:
            movimientos_posibles.append(zero_index - 3)
        # Movimiento abajo
        if zero_index <= 5:
            movimientos_posibles.append(zero_index + 3)
        # Movimiento izquierda
        if zero_index % 3 > 0:
            movimientos_posibles.append(zero_index - 1)
        # Movimiento derecha
        if zero_index % 3 < 2:
            movimientos_posibles.append(zero_index + 1)

        for move in movimientos_posibles:
            nuevoArray = swap(self.board, zero_index, move)
            vecinos.append(Estado(nuevoArray, self.moves + 1, self))

        return vecinos

    def __eq__(self, other):
        return self.board == other.board

    def __hash__(self):
        return hash(tuple(self.board))

def bfs(start_board):
    inicial = Estado(start_board)
    if inicial.finalizar():
        return inicial

    frontier = deque([inicial])
    visitados = set()

    while frontier:
        estado_actual = frontier.popleft()

        if estado_actual.finalizar():
            return estado_actual

        visitados.add(estado_actual)

        for vecino in estado_actual.obtener_vecinos():
            if vecino not in visitados and vecino not in frontier:
                frontier.append(vecino)

    return None

def arreglar_camino(goal_state):
    path = []
    current = goal_state
    while current:
        path.append(current.board)
        current = current.previous
    path.reverse()
    return path

initial_board = [0,1,3,4,5,6,2,7,8]  # Tablero inicial
goal_state = bfs(initial_board)

if goal_state:
    path = arreglar_camino(goal_state)
    print(f"Solución encontrada en {goal_state.moves} movimientos:")
    for step in path:
        print(step[:3])
        print(step[3:6])
        print(step[6:])
        print()
else:
    print("No se encontró solución.")
