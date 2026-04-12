import numpy as np
import time
from board import is_goal_state, get_next_states, heuristic

class Node:
    def __init__(self, previous, cost, heuristic, state):
        self.previous = previous
        self.cost = cost
        self.heuristic = heuristic
        self.state = state

def a_star(initial_state):
    start_time = time.time()
    # Dicionario de estados
    border = {tuple(initial_state.flatten()): Node(None, 0, heuristic(initial_state), initial_state)}

    # Verifica se um caminho já foi feito
    visited = set()
    nodes_expanded = 0
    max_iterations = 1000000  # 1 Milhão
    max_time = 60  # 60 Segundos

    while border:
        # Verifica tempo de execução
        elapsed_time = time.time() - start_time
        if elapsed_time > max_time:
            print(f"\n[ABORTADO] Limite de tempo ({max_time}s) atingido.")
            break

        # Verifica limite de iterações
        if nodes_expanded >= max_iterations:
            print(f"\n[ABORTADO] Limite de {max_iterations} iterações atingido.")
            break

        node, pos = get_cheapest_border(border)
        border.pop(pos)

        state_tuple = tuple(node.state.flatten())

        if state_tuple in visited:
            continue

        visited.add(state_tuple)
        nodes_expanded += 1

        if is_goal_state(node.state):
            end_time = time.time()
            print("-" * 30)
            print(f"Solução encontrada!")
            print(f"Nós expandidos: {nodes_expanded}")
            print(f"Custo da solução: {node.cost}")
            print(f"Tempo de execução: {end_time - start_time:.4f} segundos")
            print("-" * 30)
            return True # Retorna apenas True, ignorando o caminho percorrido

        expand_border(node, visited, border)

    if not is_goal_state(node.state):
        print(f"\nNós expandidos: {nodes_expanded}")
        print(f"Tempo de execução: {time.time() - start_time:.4f}s")
        print("Solução não encontrada nos limites definidos.")

    return None

# Busca a fronteira de menor custo
def get_cheapest_border(border):
    cheapest_node = None
    cheapest_state = None

    for key in border:
        value = border[key]
        if cheapest_node is None:
            cheapest_node = value
            cheapest_state = key
            continue

        if (value.cost + value.heuristic < cheapest_node.cost + cheapest_node.heuristic):
            cheapest_node, cheapest_state = value, key
    return cheapest_node, cheapest_state

# Expande a fronteira verificando se o novo estado
# foi visitado ou se já se encontra na fronteira
def expand_border(node, visited, border):
    for state, cost in get_next_states(node.state):
        state_tuple = tuple(state.flatten())
        if state_tuple not in visited and state_tuple not in border:
            border[state_tuple] = Node(node, node.cost + cost, heuristic(state), state)