import numpy as np
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


def depth_first_search(initial_state, max_depth=5, max_iterations=5000000):
    print("\n--- Iniciando DFS ---")
    stack = [(initial_state, [initial_state], [], 0)]
    visited = set()
    iterations = 0

    while stack:
        current, path, actions, depth = stack.pop()
        state_tuple = tuple(current.flatten())

        if state_tuple in visited:
            continue

        visited.add(state_tuple)
        iterations += 1

        if iterations % 1000 == 0:
            print(f"Iteração: {iterations} | Profundidade: {depth} | Fronteira: {len(stack)}")

        if iterations >= max_iterations:
            print(f"\n[ERRO] Limite de {max_iterations} iterações atingido sem solução.")
            print(f"Última profundidade explorada: {depth}")
            return None, None

        if is_goal_state(current):
            print(f"\n[SUCESSO] Solução DFS encontrada! Iterações: {iterations} | Profundidade: {depth}")
            return path, actions

        if depth >= max_depth:
            continue

        for neighbor, acao in reversed(get_neighbors_with_actions(current)):
            neighbor_tuple = tuple(neighbor.flatten())
            if neighbor_tuple not in visited:
                stack.append((neighbor, path + [neighbor], actions + [acao], depth + 1))

    print("\nFronteira exaurida sem encontrar solução.")
    return None, None
