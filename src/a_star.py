import numpy as np
from board import is_goal_state, get_next_states, heuristic


class Node:
    def __init__(self, previous, cost, heuristic, state):
        self.previous = previous
        self.cost = cost
        self.heuristic = heuristic
        self.state = state


def a_star(initial_state):
    border = [Node(None, 0, heuristic(initial_state), initial_state)]

    while border:
        node, pos = get_cheapest_border(border)
        if is_goal_state(node.state):
            return get_list_of_states(node)
        border.pop(pos)
        border += expand_border(node)
    raise Exception('Stack overflow')

def get_cheapest_border(border):
    cheapest_node, pos = border[0], 0
    for i in range(1, len(border)):
        current_node = border[i]
        if (current_node.cost + current_node.heuristic < cheapest_node.cost + cheapest_node.heuristic):
            cheapest_node, pos = border[i], i
    
    return cheapest_node, pos

def get_list_of_states(node):
    list_of_states = [node.state]
    while node.previous:
        node = node.previous
        list_of_states.insert(0, node.state)
    return list_of_states

def expand_border(node):
    return [Node(node, node.cost + cost, heuristic(state), state) 
            for state, cost in get_next_states(node.state) 
            if is_new_state(state, node)]


#Evita ciclos
def is_new_state(state, node):
    while node:
        if np.array_equal(node.state, state):
            return False
        node = node.previous
    return True