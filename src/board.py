import numpy as np
import copy

# Modelo de solução
goal_state = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 0],
])

# goal_state = np.array([
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 0],
# ])


#Cria novo estado corrente
def creat_new_state():
    values = np.arange(16)       
    np.random.shuffle(values)   
    new_state = values.reshape(4, 4)
    return new_state

#Cria novo estado corrente USANDO RANDOM WALK (SEMPRE SOLÚVEL, RECEBE A QUANTIDADE DE "EMBARALHADAS")
def create_new_valid_state_via_random_walk(steps):
    """
    Gera um estado inicial a partir de uma caminhada aleatória, partindo do
    objetivo, sendo que cada passo (step) é uma mexida diferente.
    Apenas para dar uma noção, se step=5 fica um puzzle muito fácil, pois ele vai sair
    do estado meta e vai mexer o jogo apenas 5 vezes.
    """
    current_state = goal_state.copy()
    movements = [([-1, 0]), ([1, 0]), ([0, 1]), ([0, -1])]

    for _ in range(steps):
        # Localiza a posição atual do zero
        zero_pos = search(0, current_state)
        # Filtra apenas os movimentos que não saem do tabuleiro
        valid_moves = [m for m in movements if movement_allowed(zero_pos, m)]
        # Escolhe um movimento aleatório da lista de válidos
        chosen_move = valid_moves[np.random.choice(len(valid_moves))]
        # Aplica o movimento e atualiza o estado corrente
        current_state = get_next_state(current_state, chosen_move, zero_pos)

    return current_state

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
    return np.array_equal(current_state, goal_state)


#Busca uma posição especifica na solução
def search(value, state):
    result = np.argwhere(state == value)
    if len(result) == 0:
        raise Exception('Incorrect state')
    return tuple(result[0])


#Distância de Manhattan: h = |x1 - x2| + |y1 - y2|
def get_distance(current_position, goal_position):
    return abs(current_position[0] - goal_position[0]) + abs(current_position[1] - goal_position[1])


#Heurística de Manhattan
def heuristic(current_state):
    total_distance = 0
    for i in range(current_state.shape[0]):
        for j in range(current_state.shape[1]):
            # if current_state[i][j] == 0:  # ← isso está aqui?
            #     continue
            goal_i, goal_j = search(current_state[i][j], goal_state)
            total_distance += get_distance((i, j), (goal_i, goal_j))
    return total_distance


#Verifica se um movimento pode ser feito
def movement_allowed(position, movement):
    row, col = position
    d_row, d_col = movement

    new_row = row + d_row
    new_col = col + d_col

    return 0 <= new_row <= 3 and 0 <= new_col <= 3

#Movimenta o Zero criando um novo estado
def get_next_state(current_state, movement, empty_position):
    new_state = current_state.copy()

    row, col = empty_position
    d_row, d_col = movement

    new_row = row + d_row
    new_col = col + d_col

    new_state[row][col], new_state[new_row][new_col] = (
        new_state[new_row][new_col],
        new_state[row][col],
    )

    return new_state

#Gera todos os estados possiveis a partir do atual
def get_next_states(current_state):
    i, j = search(0, current_state)
    movements = [[-1, 0], [1, 0], [0, 1], [0, -1]]
    next_states = []
    for movement in movements:
        if movement_allowed((i, j), movement):
            next_states.append((get_next_state(current_state, movement, (i, j)), 1))

    return next_states

