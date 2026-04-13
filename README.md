# Jogo do 15 - Algoritmos de Busca
Este repositório contém a implementação do Jogo dos 15 utilizando diferentes algoritmos de busca estudados em Fundamentos de Inteligência Artificial

### Descrição
O objetivo do jogo é reorganizar uma grade 4×4 com números de 1 a 15, deixando a lacuna na última posição. O problema é modelado como um grafo de espaço de estados, em que cada configuração do tabuleiro representa um estado.

### Funcionalidades
Geração de estados iniciais aleatórios
Verificação de solubilidade (invariante de paridade)
Resolução do problema com diferentes algoritmos de busca

### Algoritmos implementados
Busca em Largura (BFS)
Busca em Profundidade (DFS)
A* com heurística de Distância de Manhattan

### Como executar
1. Instale as dependências:
pip install -r requirements.txt

2. Execute o programa:
python main.py

### Observações
O algoritmo A* apresenta melhor desempenho geral devido ao uso de heurística
BFS garante solução ótima, mas tem alto custo de memória
DFS é mais econômico em memória, porém não garante otimalidade

### Colaboradores 
Amanda Fiaux, Daniel Araújo e Yuri Wada
