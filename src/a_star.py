class Node:
    def __init__(self, previous, cost, heuristic, state):
        self.previous = previous
        self.cost = cost
        self.heuristic = heuristic
        self.state = state
    