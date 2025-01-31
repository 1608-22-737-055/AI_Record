class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

# Depth-First Search function
def dfs(root, target):
    stack = [root]  # Initialize the stack with the root node

    while stack:
        current_node = stack.pop()  # Pop the top node from the stack
        print(f"Visiting node with value: {current_node.value}")

        if current_node.value == target:
            print(f"Target '{target}' found!")
            return current_node

        # Add the children of the current node to the stack
        # in reverse order to maintain correct traversal order
        stack.extend(reversed(current_node.children))

    print(f"Target '{target}' not found in the tree.")
    return None

# Example Usage:
# Constructing a tree for demonstration
root = TreeNode("A")
node_b = TreeNode("B")
node_c = TreeNode("C")
node_d = TreeNode("D")
node_e = TreeNode("E")
node_f = TreeNode("F")
node_g = TreeNode("G")

root.add_child(node_b)
root.add_child(node_c)
node_b.add_child(node_d)
node_b.add_child(node_e)
node_c.add_child(node_f)
node_c.add_child(node_g)

# Perform DFS to find a target node
target_node = dfs(root, "E")
if target_node:
    print(f"Target node found with value: {target_node.value}")
else:
    print("Target node not found.")
