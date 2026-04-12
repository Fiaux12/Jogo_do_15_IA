import numpy as np
from collections import deque

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
    # Estado meta padrão
    goal = np.array([
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 0]
    ])

    # fila que armazena o estado_atual, profundidade e o caminho percorrido)
    queue = deque([(initial_state, 0, [initial_state])])
    explored = {tuple(initial_state.flatten())}
    iterations = 0
    max_iterations = 200000  # Limite de 200 mil

    print(f"\n--- Iniciando BFS ---")

    while queue:
        current, depth, path = queue.popleft()
        iterations += 1

        if iterations % 1000 == 0:
            print(f"Iteração: {iterations} | Profundidade: {depth} | Fronteira: {len(queue)}")

        # Verifica limite de iterações
        if iterations >= max_iterations:
            print(f"\n[ERRO] Limite de {max_iterations} iterações atingido sem solução.")
            print(f"Última profundidade explorada: {depth}")
            return None

        if np.array_equal(current, goal):
            print(f"\n[SUCESSO] Solução encontrada! Iterações: {iterations} | Profundidade: {depth}")
            return path

        for neighbor in get_neighbors(current):
            state_tuple = tuple(neighbor.flatten())
            if state_tuple not in explored:
                explored.add(state_tuple)
                queue.append((neighbor, depth + 1, path + [neighbor]))

    print("\nFronteira exaurida sem encontrar solução.")
    return None
