import numpy as np
from board import is_goal_state, get_next_states, heuristic

class Node:
    def __init__(self, previous, cost, heuristic, state):
        self.previous = previous
        self.cost = cost
        self.heuristic = heuristic
        self.state = state


def a_star(initial_state):
    # Dicionario de estados
    border = {tuple(initial_state.flatten()): Node(None, 0, heuristic(initial_state), initial_state) }

    # Verifica se um caminho já foi feito
    visited = set()

    iterations = 0

    while border:
        node, pos = get_cheapest_border(border)
        border.pop(pos)

        state_tuple = tuple(node.state.flatten())

        if state_tuple in visited:
            continue
        
        visited.add(state_tuple)
        iterations += 1

        # Parar depois de 
        if iterations == 10000:
            print("Não foi possivel achar uma solução em 10 mil interações")
            print(f'Iteração {iterations} | Fronteira: {len(border)} | custo={node.cost} | helritica={node.heuristic}')
            return Exception('No solution found')

        if is_goal_state(node.state):
            print(f'Solução encontrada em {iterations} iterações!')
            return get_list_of_states(node)

        expand_border(node, visited, border)

    raise Exception('No solution found')


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


# Busca a lista de novos estados
def get_list_of_states(node):
    list_of_states = [node.state]
    while node.previous:
        node = node.previous
        list_of_states.insert(0, node.state)
    return list_of_states


# Expande a fronteira verificando se o novo estado
# foi visitado ou se já se encontra na fronteira
def expand_border(node, visited, border):
    for state, cost in get_next_states(node.state):
        state_tuple = tuple(state.flatten())
        if state_tuple not in visited and state_tuple not in border:
            border[state_tuple] = Node(node, node.cost + cost, heuristic(state), state)

