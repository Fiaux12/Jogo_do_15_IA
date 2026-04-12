import numpy as np
from board import heuristic
import bfs
import dfs
from a_star import a_star

# Testes --------------------------------

# Caso de teste 1 (Movimentos perfeitos: 5)
state1 = np.array([
    [ 1,  2,  3,  4],
    [ 5,  6,  8, 12],
    [ 9, 10,  7,  0],
    [13, 14, 11, 15],
])

# Caso de teste 2 (Movimentos perfeitos: 10)
state2 = np.array([
    [ 1,  2,  3,  4],
    [ 5,  6,  8, 12],
    [13,  9, 10,  7],
    [14,  0, 11, 15],
])

# Caso de teste 3 (Movimentos perfeitos: 15)
state3 = np.array([
    [ 1,  2,  3,  4],
    [ 5,  9,  6, 12],
    [13,  0,  8,  7],
    [14, 11, 10, 15],
])

# Caso de teste 4 (Movimentos perfeitos: 20)
state4 = np.array([
    [ 5,  1,  3,  4],
    [ 2,  0,  6, 12],
    [13,  9,  8,  7],
    [14, 11, 10, 15],
])

# Caso de teste 5 (Movimentos perfeitos: 25)
state5 = np.array([
    [ 2,  5,  1,  4],
    [ 0,  6,  3, 12],
    [13,  9,  8,  7],
    [14, 11, 10, 15],
])

# Caso de teste 6 (Movimentos perfeitos: 30)
state6 = np.array([
    [ 5,  1,  4, 12],
    [ 2,  6,  3,  0],
    [13,  9,  8,  7],
    [14, 11, 10, 15],
])

# Caso de teste 7 (Movimentos perfeitos: 35)
# Nota: A matriz visual na imagem é idêntica ao caso 5 (25 movimentos)
state7 = np.array([
    [ 2,  5,  1,  4],
    [ 0,  6,  3, 12],
    [13,  9,  8,  7],
    [14, 11, 10, 15],
])

# Caso de teste 8 (Movimentos perfeitos: 40)
state8 = np.array([
    [ 2,  5,  1,  4],
    [ 6,  9,  3, 12],
    [ 0, 11,  8,  7],
    [13, 14, 10, 15],
])

# Agrupando os casos de teste e a quantidade de movimentos perfeitos esperados
test_cases = [
    (state1, 5),
    (state2, 10),
    (state3, 15),
    (state4, 20),
    (state5, 25),
    (state6, 30),
    (state7, 35),
    (state8, 40)
]

# Executando os testes
for index, (current_state, perfect_moves) in enumerate(test_cases, 1):
    print(f"\n{'=' * 50}")
    print(f"=== TESTANDO CASO {index} (Movimentos teóricos: {perfect_moves}) ===")
    print(f"{'=' * 50}")

    print('Estado inicial:')
    print(current_state)
    print(f'Heurística inicial: {heuristic(current_state)}\n')

    # 1. BFS
    print(">>> Executando BFS...")
    bfs.breadth_first_search(current_state)

    # 2. DFS
    print("\n>>> Executando DFS...")
    # Ajustando a profundidade máxima para permitir que o DFS alcance a solução
    dfs.depth_first_search(current_state, max_depth=(perfect_moves + 10))

    # 3. A*
    print("\n>>> Executando A*...")
    a_star(current_state)