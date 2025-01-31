
# Program 3  Greedy Best First Search (GBFS) algorithm 

from heapq import heappop, heappush
from math import inf

class Graph:
    def __init__(self, directed=True):
        self.edges = {}
        self.heuristics = {}  # Corrected variable name
        self.directed = directed

    def add_edge(self, node1, node2, cost=1, reversed=False):
        try:
            neighbors = self.edges[node1]
        except KeyError:
            neighbors = {}
        neighbors[node2] = cost
        self.edges[node1] = neighbors
        if not self.directed and not reversed:
            self.add_edge(node2, node1, cost, True)

    def set_heuristics(self, heuristics):
        self.heuristics = heuristics  # Corrected method and variable name

    def neighbors(self, node):
        try:
            return self.edges[node]
        except KeyError:
            return []

    def cost(self, node1, node2):
        try:
            return self.edges[node1][node2]
        except KeyError:
            return inf

    def best_first_search(self, start, goal):
        found = False
        fringe = [(self.heuristics[start], start)]  # Priority queue sorted by heuristic
        visited = set([start])
        came_from = {start: None}
        cost_so_far = {start: 0}

        print('{:11s} | {}'.format('Expand Node', 'Fringe'))
        print('--------------------------------------------------')
        print('{:11s} | {}'.format('-', str(fringe[0])))

        while not found and fringe:
            current_priority, current_node = heappop(fringe)  # Extract node from tuple
            print('{:11s}'.format(current_node), end=' | ')

            if current_node == goal:
                found = True
                break

            for neighbor in self.neighbors(current_node):
                new_cost = cost_so_far[current_node] + self.cost(current_node, neighbor)
                if neighbor not in visited or new_cost < cost_so_far.get(neighbor, inf):
                    visited.add(neighbor)
                    came_from[neighbor] = current_node
                    cost_so_far[neighbor] = new_cost
                    # GBFS uses heuristic alone for priority
                    priority = self.heuristics[neighbor]
                    heappush(fringe, (priority, neighbor))

            # Display the fringe after updating
            fringe_sorted = sorted(fringe, key=lambda x: x[0])
            print(', '.join([f"({priority}, '{node}')" for priority, node in fringe_sorted]))

        if found:
            print("\nGoal reached!")
            return came_from, cost_so_far[goal]
        else:
            print(f'\nNo path from {start} to {goal}')
            return None, inf

    @staticmethod
    def print_path(came_from, goal):
        if goal not in came_from:
            return
        parent = came_from[goal]
        if parent:
            Graph.print_path(came_from, parent)
            print(' =>', goal, end='')
        else:
            print(goal, end='')

# Example usage
graph = Graph(directed=True)
graph.add_edge('A', 'B', 4)
graph.add_edge('A', 'C', 1)
graph.add_edge('B', 'D', 3)
graph.add_edge('B', 'E', 8)
graph.add_edge('C', 'D', 7)
graph.add_edge('C', 'F', 6)
graph.add_edge('D', 'C', 2)
graph.add_edge('D', 'E', 4)
graph.add_edge('E', 'G', 2)
graph.add_edge('F', 'G', 8)

heuristics = {'A': 8, 'B': 8, 'C': 6, 'D': 5, 'E': 1, 'F': 4, 'G': 0}
graph.set_heuristics(heuristics)

start, goal = 'A', 'G'
traced_path, cost = graph.best_first_search(start, goal)

if traced_path:
    print('Path:', end=' ')
    Graph.print_path(traced_path, goal)
    print(f'\nCost: {cost}')