import numpy as np
import time
from board import is_goal_state, movement_allowed, get_next_state


def get_neighbors_with_actions(state):
    neighbors = []
    row, col = np.where(state == 0)
    row, col = row[0], col[0]

    movimentos = [(-1, 0, 'Cima'), (1, 0, 'Baixo'), (0, -1, 'Esquerda'), (0, 1, 'Direita')]
    for dr, dc, acao in movimentos:
        if movement_allowed((row, col), (dr, dc)):
            neighbor = get_next_state(state, [dr, dc], (row, col))
            neighbors.append((neighbor, acao))
    return neighbors


def depth_first_search(initial_state, max_depth=50, max_time=60, max_iterations=1000000):
    start_time = time.time()
    stack = [(initial_state, 0)]

    # MUDANÇA AQUI: Dicionário para guardar a profundidade em que o estado foi visto
    visited = {}
    nodes_expanded = 0

    while stack:
        elapsed_time = time.time() - start_time
        if elapsed_time > max_time:
            return {
                "success": False, "nodes_expanded": nodes_expanded,
                "cost": None, "time": elapsed_time, "status": "Timeout"
            }

        if nodes_expanded >= max_iterations:
            return {
                "success": False, "nodes_expanded": nodes_expanded,
                "cost": None, "time": elapsed_time, "status": "Max Iterations"
            }

        current, depth = stack.pop()
        state_tuple = tuple(current.flatten())

        # MUDANÇA AQUI: Só pulamos o estado se já o visitamos numa profundidade MENOR ou IGUAL.
        # Se chegamos nele agora por um caminho mais rápido, vale a pena explorar de novo!
        if state_tuple in visited and visited[state_tuple] <= depth:
            continue

        # Registra que visitamos este estado nesta profundidade
        visited[state_tuple] = depth
        nodes_expanded += 1

        if is_goal_state(current):
            return {
                "success": True, "nodes_expanded": nodes_expanded,
                "cost": depth, "time": time.time() - start_time, "status": "Success"
            }

        if depth < max_depth:
            for neighbor, acao in reversed(get_neighbors_with_actions(current)):
                neighbor_tuple = tuple(neighbor.flatten())

                # Otimização: Só adiciona na pilha se for um caminho melhor
                if neighbor_tuple not in visited or visited[neighbor_tuple] > depth + 1:
                    stack.append((neighbor, depth + 1))

    return {
        "success": False, "nodes_expanded": nodes_expanded,
        "cost": None, "time": time.time() - start_time, "status": "Exhausted"
    }