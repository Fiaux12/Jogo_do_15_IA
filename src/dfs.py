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


def depth_first_search(initial_state, max_depth=50):
    start_time = time.time()
    # stack armazena (estado, profundidade)
    stack = [(initial_state, 0)]
    visited = set()
    nodes_expanded = 0

    max_iterations = 1000000  # 1 Milhão
    max_time = 60  # 60 Segundos

    while stack:
        # Verifica tempo de execução
        elapsed_time = time.time() - start_time
        if elapsed_time > max_time:
            print(f"\n[ABORTADO] Limite de tempo ({max_time}s) atingido.")
            break

        # Verifica limite de iterações
        if nodes_expanded >= max_iterations:
            print(f"\n[ABORTADO] Limite de {max_iterations} iterações atingido.")
            break

        current, depth = stack.pop()
        state_tuple = tuple(current.flatten())

        if state_tuple in visited:
            continue

        visited.add(state_tuple)
        nodes_expanded += 1

        if is_goal_state(current):
            end_time = time.time()
            print("-" * 30)
            print(f"Solução encontrada!")
            print(f"Nós expandidos: {nodes_expanded}")
            print(f"Custo da solução (profundidade): {depth}")
            print(f"Tempo de execução: {end_time - start_time:.4f} segundos")
            print("-" * 30)
            return True

        # Controle de profundidade para evitar recursão infinita no 15-puzzle
        if depth < max_depth:
            # reversed para manter a ordem de expansão original da sua lista
            for neighbor, acao in reversed(get_neighbors_with_actions(current)):
                neighbor_tuple = tuple(neighbor.flatten())
                if neighbor_tuple not in visited:
                    stack.append((neighbor, depth + 1))

    if not is_goal_state(current):
        print(f"\nNós expandidos: {nodes_expanded}")
        print(f"Tempo de execução: {time.time() - start_time:.4f}s")
        print("Solução não encontrada nos limites definidos.")

    return None