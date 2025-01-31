from heapq import heappop, heappush
from math import inf

class Graph:
    def __init__(self, directed=True):
        self.edges = {}
        self.huristics = {}
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

    def set_huristics(self, huristics):
        self.huristics = huristics

    def neighbors(self, node):
        return self.edges[node]

    def cost(self, node1, node2):
        return self.edges[node1][node2]

    def a_star_search(self, start, goal):
        fringe = []
        heappush(fringe, (self.huristics[start], start))
        came_from = {start: None}
        cost_so_far = {start: 0}
        visited = set()
        found = False

        print('{:11s} | {}'.format('Expand Node', 'Fringe'))
        print('--------------------------------------------------')
        print('{:11s} | {}'.format('-', ', '.join(map(str, fringe))))

        while not found and len(fringe):
            current = heappop(fringe)
            print('{:11s} | {}'.format(current[1], ', '.join(map(str, fringe))))

            if current[1] == goal:
                found = True
                break

            for node in self.neighbors(current[1]):
                new_cost = cost_so_far[current[1]] + self.cost(current[1], node)
                if node not in visited or cost_so_far[node] > new_cost:
                    visited.add(node)
                    came_from[node] = current[1]
                    cost_so_far[node] = new_cost
                    heappush(fringe, (new_cost + self.huristics[node], node))

        if found:
            traced_path = []
            while current[1] in came_from:
                traced_path.append(current[1])
                current = (None, came_from[current[1]])
            traced_path.reverse()
            return traced_path, cost_so_far[goal]
        else:
            return None, inf

    @staticmethod
    def print_path(path, goal):
        print(' => '.join(path + [goal]))

# Example usage
graph = Graph(directed=True)
graph.add_edge('A', 'B', 4)
graph.add_edge('A', 'C', 1)
graph.add_edge('B', 'D', 3)
graph.add_edge('B', 'E', 8)
graph.add_edge('C', 'C', 0)
graph.add_edge('C', 'D', 7)
graph.add_edge('C', 'F', 6)
graph.add_edge('D', 'C', 2)
graph.add_edge('D', 'E', 4)
graph.add_edge('E', 'G', 2)
graph.add_edge('F', 'G', 8)

graph.set_huristics({'A': 8, 'B': 8, 'C': 6, 'D': 5, 'E': 1, 'F': 4, 'G': 0})

start, goal = 'A', 'G'
traced_path, cost = graph.a_star_search(start, goal)

if traced_path:
    print('Path:', end=' ')
    Graph.print_path(traced_path, goal)
    print("\nCost:", cost)
else:
    print('No path found')
