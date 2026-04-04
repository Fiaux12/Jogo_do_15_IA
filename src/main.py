import numpy as np
from board import creat_new_state, is_solvable, is_goal_state, get_next_states
from a_star import a_star

current_state = creat_new_state()

#Cria um estado que tem solução
while not is_solvable(current_state):
    current_state = creat_new_state()

# breadth_first_search()
# depth_first_search()

a_star()

print(current_state)
print("\n")

print(get_next_states(current_state))
