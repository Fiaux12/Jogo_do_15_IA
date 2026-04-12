import numpy as np
from board import creat_new_state, is_solvable, is_goal_state, get_next_states, heuristic
from a_star import a_star
import bfs
import dfs

# Testes --------------------------------

current_state = np.array([
    [ 1,  2,  3,  4],
    [ 5,  6,  7,  8],
    [ 9, 10, 11, 0],
    [13,  12, 14, 15],
])

# #35 movimentos e 3066 iterações
# current_state = np.array([
#     [ 9, 1,  6, 2],
#     [13, 5,  7, 3],
#     [15, 8, 10, 4],
#     [12, 0, 14, 11],
# ])

# 28 movimentos e 7582 iterações
# current_state = np.array([
#     [ 1,  2,  3,  6],
#     [ 5,  7,  4, 11],
#     [14, 13,  8, 10],
#     [ 0,  9, 15, 12],
# ])

# Mais de 10 mil interações
# current_state = np.array([
#     [14,  2,  4,  7],
#     [11,  8, 15,  3],
#     [ 1, 13,  0, 12],
#     [ 5,  6,  9, 10],
# ])

# Testes --------------------------------

#Cria um estado que tem solução
# current_state = creat_new_state()
# while not is_solvable(current_state):
#     current_state = creat_new_state()


solucao_bfs = bfs.breadth_first_search(current_state)
solucao_dfs, acoes_dfs = dfs.depth_first_search(current_state, max_depth=25)

print(f'Heurística inicial: {heuristic(current_state)}')
print(f'Estado inicial:')
print(current_state)

if solucao_dfs is not None:
    print(f'\nDFS encontrou uma solução em {len(solucao_dfs) - 1} movimentos: {acoes_dfs}')
else:
    print('\nDFS não encontrou solução dentro do limite.')

# list_of_states = a_star(current_state)
# step = 0
# for state in list_of_states:
#     step += 1
#     for line in state:
#         print(line)
#     print('Passo: ' + str(step))
#     print('='*20)
