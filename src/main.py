import numpy as np


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


current_state = creat_new_state()
print(is_solvable(current_state))