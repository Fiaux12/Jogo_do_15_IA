import numpy as np
from collections import deque
import time


def get_neighbors(state):
    neighbors = []
    r, c = np.where(state == 0)
    r, c = r[0], c[0]

    # Movimentos: Cima, Baixo, Esquerda, Direita
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 4 and 0 <= nc < 4:
            new_state = state.copy()
            new_state[r, c], new_state[nr, nc] = new_state[nr, nc], new_state[r, c]
            neighbors.append(new_state)
    return neighbors


def breadth_first_search(initial_state):
    start_time = time.time()

    # Estado meta padrão
    goal = np.array([
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 0]
    ])

    # Fila armazena (estado_atual, profundidade)
    # Removi o 'path' da fila para economizar MUITA memória,
    # já que a BFS em 4x4 explode rápido.
    queue = deque([(initial_state, 0)])
    explored = {tuple(initial_state.flatten())}

    nodes_expanded = 0
    max_iterations = 1000000  # 1 Milhão
    max_time = 60  # 1 Minuto

    while queue:
        current, depth = queue.popleft()
        nodes_expanded += 1

        # Verifica tempo de execução
        elapsed_time = time.time() - start_time
        if elapsed_time > max_time:
            print(f"\n[ABORTADO] Limite de tempo ({max_time}s) atingido.")
            break

        # Verifica limite de iterações
        if nodes_expanded >= max_iterations:
            print(f"\n[ABORTADO] Limite de {max_iterations} iterações atingido.")
            break

        # Verifica se chegou ao objetivo
        if np.array_equal(current, goal):
            end_time = time.time()
            print("-" * 30)
            print(f"Solução encontrada!")
            print(f"Nós expandidos: {nodes_expanded}")
            print(f"Custo da solução (profundidade): {depth}")
            print(f"Tempo de execução: {end_time - start_time:.4f} segundos")
            print("-" * 30)
            return True

        for neighbor in get_neighbors(current):
            state_tuple = tuple(neighbor.flatten())
            if state_tuple not in explored:
                explored.add(state_tuple)
                queue.append((neighbor, depth + 1))

    if not np.array_equal(current, goal):
        print(f"\nNós expandidos: {nodes_expanded}")
        print(f"Tempo de execução: {time.time() - start_time:.4f}s")
        print("Solução não encontrada nos limites definidos.")

    return None