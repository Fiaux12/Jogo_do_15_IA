import numpy as np
import time
from board import is_goal_state, get_next_states, heuristic


class Node:
    def __init__(self, previous, cost, heuristic, state):
        self.previous = previous
        self.cost = cost
        self.heuristic = heuristic
        self.state = state


def a_star(initial_state, max_time=60, max_iterations=1000000):
    start_time = time.time()
    # Dicionario de estados
    border = {tuple(initial_state.flatten()): Node(None, 0, heuristic(initial_state), initial_state)}

    # Verifica se um caminho já foi feito
    visited = set()
    nodes_expanded = 0

    while border:
        # Verifica tempo de execução
        elapsed_time = time.time() - start_time
        if elapsed_time > max_time:
            return {
                "success": False,
                "nodes_expanded": nodes_expanded,
                "cost": None,
                "time": elapsed_time,
                "status": "Timeout"
            }

        # Verifica limite de iterações
        if nodes_expanded >= max_iterations:
            return {
                "success": False,
                "nodes_expanded": nodes_expanded,
                "cost": None,
                "time": elapsed_time,
                "status": "Max Iterations"
            }

        node, pos = get_cheapest_border(border)
        border.pop(pos)

        state_tuple = tuple(node.state.flatten())

        if state_tuple in visited:
            continue

        visited.add(state_tuple)
        nodes_expanded += 1

        if is_goal_state(node.state):
            return {
                "success": True,
                "nodes_expanded": nodes_expanded,
                "cost": node.cost,  # O custo é igual à profundidade neste caso
                "time": time.time() - start_time,
                "status": "Success"
            }

        expand_border(node, visited, border)

    # Se a fronteira esvaziar e não achar solução
    return {
        "success": False,
        "nodes_expanded": nodes_expanded,
        "cost": None,
        "time": time.time() - start_time,
        "status": "Exhausted"
    }


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

        # A* f(n) = g(n) + h(n)
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