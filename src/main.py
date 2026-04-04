import numpy as np
from board import creat_new_state, is_solvable, is_goal_state, get_next_states, heuristic
from a_star import a_star

# current_state = creat_new_state()

current_state = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [0, 13, 14, 15],
])



#Cria um estado que tem solução
while not is_solvable(current_state):
    current_state = creat_new_state()

# breadth_first_search()
# depth_first_search()

list_of_states = a_star(current_state)

print("\n")

step = 0
for state in list_of_states:
    step += 1
    for line in state:
        print(line)
    print('Passo: ' + str(step))
    print('='*20)