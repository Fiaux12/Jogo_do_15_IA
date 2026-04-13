import numpy as np
import board
from bfs import breadth_first_search
from dfs import depth_first_search
from a_star import a_star

# ==========================================
# CONFIGURAÇÕES DO EXPERIMENTO
# ==========================================

NIVEIS_DIFICULDADE = [2, 3, 4, 5]  # Quantidade de passos no Random Walk
TENTATIVAS_POR_NIVEL = 5  # Quantidade de testes para cada nível
TEMPO_MAXIMO = 30  # Segundos por algoritmo
ITERACOES_MAXIMAS = 1000000  # Limite de nós expandidos
PROFUNDIDADE_DFS = 200  # Limite para a DFS não afundar infinitamente

# Dicionário para armazenar as estatísticas consolidadas
estatisticas = {
    nivel: {
        'BFS': {'sucessos': 0, 'nos': [], 'custo': [], 'tempo': []},
        'DFS': {'sucessos': 0, 'nos': [], 'custo': [], 'tempo': []},
        'A*': {'sucessos': 0, 'nos': [], 'custo': [], 'tempo': []}
    } for nivel in NIVEIS_DIFICULDADE
}

print("Iniciando bateria de testes estatísticos...")
print(f"Níveis de complexidade (Random Walk): {NIVEIS_DIFICULDADE}")
print(f"Tentativas por nível: {TENTATIVAS_POR_NIVEL}\n")

for passos in NIVEIS_DIFICULDADE:
    print(f"{'=' * 60}")
    print(f"=== TESTANDO COMPLEXIDADE: {passos} PASSOS (Random Walk) ===")
    print(f"{'=' * 60}")

    for tentativa in range(1, TENTATIVAS_POR_NIVEL + 1):
        print(f"\n--- Gerando Teste {tentativa}/{TENTATIVAS_POR_NIVEL} (Passos: {passos}) ---")

        estado_atual = board.create_new_valid_state_via_random_walk(passos)

        # --- 1. BFS ---
        res_bfs = breadth_first_search(estado_atual, max_time=TEMPO_MAXIMO, max_iterations=ITERACOES_MAXIMAS)
        if res_bfs['success']:
            estatisticas[passos]['BFS']['sucessos'] += 1
            estatisticas[passos]['BFS']['nos'].append(res_bfs['nodes_expanded'])
            estatisticas[passos]['BFS']['custo'].append(res_bfs['cost'])
            estatisticas[passos]['BFS']['tempo'].append(res_bfs['time'])

        # --- 2. DFS ---
        res_dfs = depth_first_search(estado_atual, max_depth=PROFUNDIDADE_DFS, max_time=TEMPO_MAXIMO,
                                     max_iterations=ITERACOES_MAXIMAS)
        if res_dfs['success']:
            estatisticas[passos]['DFS']['sucessos'] += 1
            estatisticas[passos]['DFS']['nos'].append(res_dfs['nodes_expanded'])
            estatisticas[passos]['DFS']['custo'].append(res_dfs['cost'])
            estatisticas[passos]['DFS']['tempo'].append(res_dfs['time'])

        # --- 3. A* ---
        res_astar = a_star(estado_atual, max_time=TEMPO_MAXIMO, max_iterations=ITERACOES_MAXIMAS)
        if res_astar['success']:
            estatisticas[passos]['A*']['sucessos'] += 1
            estatisticas[passos]['A*']['nos'].append(res_astar['nodes_expanded'])
            estatisticas[passos]['A*']['custo'].append(res_astar['cost'])
            estatisticas[passos]['A*']['tempo'].append(res_astar['time'])

        print(f"BFS -> Status: {res_bfs['status']} | Nós: {res_bfs['nodes_expanded']} | Tempo: {res_bfs['time']:.3f}s")
        print(f"DFS -> Status: {res_dfs['status']} | Nós: {res_dfs['nodes_expanded']} | Tempo: {res_dfs['time']:.3f}s")
        print(
            f"A* -> Status: {res_astar['status']} | Nós: {res_astar['nodes_expanded']} | Tempo: {res_astar['time']:.3f}s")

# ==============================================================================
# GERAÇÃO DA TABELA FINAL COM MÉDIAS (TAREFA 5)
# ==============================================================================
print("\n" + "=" * 90)
print("RELATÓRIO FINAL DE ESTATÍSTICAS (MÉDIAS DOS CASOS BEM-SUCEDIDOS)")
print("=" * 90)
print(
    f"{'Passos (RW)':<12} | {'Algoritmo':<10} | {'Sucesso (%)':<12} | {'Média Nós Exp.':<15} | {'Média Custo':<12} | {'Média Tempo (s)':<15}")
print("-" * 90)

for passos in NIVEIS_DIFICULDADE:
    for alg in ['BFS', 'DFS', 'A*']:
        dados = estatisticas[passos][alg]
        taxa_sucesso = (dados['sucessos'] / TENTATIVAS_POR_NIVEL) * 100

        # Calcula as médias apenas se houver pelo menos 1 sucesso
        if dados['sucessos'] > 0:
            media_nos = sum(dados['nos']) / dados['sucessos']
            media_custo = sum(dados['custo']) / dados['sucessos']
            media_tempo = sum(dados['tempo']) / dados['sucessos']

            print(
                f"{passos:<12} | {alg:<10} | {taxa_sucesso:>8.1f}%   | {media_nos:>14.1f} | {media_custo:>11.1f} | {media_tempo:>14.4f}")
        else:
            print(f"{passos:<12} | {alg:<10} | {taxa_sucesso:>8.1f}%   | {'N/A':>14} | {'N/A':>11} | {'N/A':>14}")
    print("-" * 90)