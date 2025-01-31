
# python BFS.py
#BFS Traversal: ['A', 'B', 'C', 'D', 'E', 'F']

from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

def bfs(root):
    if not root:
        return []

    queue = deque([root])  # Initialize the queue with the root node
    result = []  # List to store the traversal result

    while queue:
        current_node = queue.popleft()  # Dequeue the front node
        result.append(current_node.value)  # Add the node's value to the result

        # Enqueue all the children of the current node
        for child in current_node.children:
            queue.append(child)

    return result

# Constructing the tree
root = Node("A")
child_b = Node("B")
child_c = Node("C")
child_d = Node("D")
child_e = Node("E")
child_f = Node("F")

root.add_child(child_b)
root.add_child(child_c)
child_b.add_child(child_d)
child_b.add_child(child_e)
child_c.add_child(child_f)

# Apply BFS
bfs_result = bfs(root)
print("BFS Traversal:", bfs_result)


