import numpy as np
import copy

# Modelo de solução
goal_state = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 0],
]


#Cria novo estado corrente
def creat_new_state():
    values = np.arange(16)       
    np.random.shuffle(values)   
    new_state = values.reshape(4, 4)
    print(new_state)
    return new_state


#Verifica se o problema tem solução
def is_solvable(state):
    flat = state.flatten()
    board = flat[flat != 0]

    num_inversions = 0
    for i in range(len(board)):
        for j in range(i+1, len(board)):
            if board[i] > board[j]:
                num_inversions += 1

    zero_line = (flat == 0).nonzero()[0][0] // 4
    row_bottom = 4 - zero_line

    return (num_inversions + row_bottom) % 2 == 0


#Verifica se alcançou o objetivo
def is_goal_state(current_state):
    for i in range(len(current_state)):
        for j in range(len(current_state[i])):
            if current_state[i][j] != goal_state[i][j]:
                print(f"Error in position ({i}, {j}): {current_state[i][j]} != {goal_state[i][j]}")
                return False
    return True


#Busca uma posição especifica na solução
def search(value, goal_state):
    for i in range(len(goal_state)):
        for j in range(len(goal_state[i])):
            if goal_state[i][j] == value:
                return i, j
    raise Exception('Incorrect state')


#Distância de Manhattan: h = |x1 - x2| + |y1 - y2|
def get_distance(current_position, goal_position):
    return abs(current_position[0] - goal_position[0]) + abs(current_position[1] - goal_position[1])


#Heurística de Manhattan: 
def heuristic(current_state):
    total_distance = 0
    for i in range(len(current_state)):
        for j in range(len(current_state[i])):
            goal_i, goal_j = search(current_state[i][j], goal_state)
            total_distance += get_distance((i, j), (goal_i, goal_j))

    return total_distance



