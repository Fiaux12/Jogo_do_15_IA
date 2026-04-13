import numpy as np
from collections import deque
import time


def get_neighbors(state):
    neighbors = []
    # Encontra a posição do zero (vazio)
    pos = np.where(state == 0)
    r, c = pos[0][0], pos[1][0]

    # Movimentos: Cima, Baixo, Esquerda, Direita
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 4 and 0 <= nc < 4:
            new_state = state.copy()
            new_state[r, c], new_state[nr, nc] = new_state[nr, nc], new_state[r, c]
            neighbors.append(new_state)
    return neighbors


def breadth_first_search(initial_state, max_time=60, max_iterations=100000):
    start_time = time.time()

    # Estado meta
    goal = np.array([
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 0]
    ])

    # Fila armazena (estado_atual, profundidade)
    queue = deque([(initial_state, 0)])

    # Set de explorados usando a representação em tupla (imutável) para eficiência
    explored = {tuple(initial_state.flatten())}

    nodes_expanded = 0

    while queue:
        current, depth = queue.popleft()
        nodes_expanded += 1

        # Verificação de segurança (Tempo)
        elapsed_time = time.time() - start_time
        if elapsed_time > max_time:
            return {
                "success": False,
                "nodes_expanded": nodes_expanded,
                "cost": None,
                "time": elapsed_time,
                "status": "Timeout"
            }

        # Verificação de segurança (Iterações/Memória)
        if nodes_expanded >= max_iterations:
            return {
                "success": False,
                "nodes_expanded": nodes_expanded,
                "cost": None,
                "time": elapsed_time,
                "status": "Max Iterations"
            }

        # Teste de Objetivo
        if np.array_equal(current, goal):
            return {
                "success": True,
                "nodes_expanded": nodes_expanded,
                "cost": depth,
                "time": elapsed_time,
                "status": "Success"
            }

        # Expansão de vizinhos
        for neighbor in get_neighbors(current):
            state_tuple = tuple(neighbor.flatten())
            if state_tuple not in explored:
                explored.add(state_tuple)
                queue.append((neighbor, depth + 1))

    return {
        "success": False,
        "nodes_expanded": nodes_expanded,
        "cost": None,
        "time": time.time() - start_time,
        "status": "Exhausted"
    }