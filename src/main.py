import numpy as np
from board import is_goal_state, creat_new_state, is_solvable

current_state = creat_new_state()
print(is_solvable(current_state))