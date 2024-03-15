from collections import deque


class Node:
    def __init__(self, key):
        self.value = key
        self.left = []
        self.right = []


class Tree:
    def __init__(self):
        self.root = None

    def dfs_inorder(self, root):
        if root:
            self.dfs_inorder(root.left)
            print(root.value)
            self.dfs_inorder(root.right)
    def dfs_preorder(self, root):
        if root:
            print(root.value)
            self.dfs_preorder(root.left)
            self.dfs_preorder(root.right)

    def dfs_postorder(self, root):
        if root:
            self.dfs_postorder(root.left)
            self.dfs_postorder(root.right)
            print(root.value)

    def bfs_traversal(root):
        if not root:
            return

        # Create a queue for BFS
        queue = deque()
        # Enqueue the root node
        queue.append(root)

        while queue:
            # Dequeue a node and print its value
            node = queue.popleft()
            print(node.val, end=" ")

            # Enqueue the left child if it exists
            if node.left:
                queue.append(node.left)
            # Enqueue the right child if it exists
            if node.right:
                queue.append(node.right)


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
tree = Tree()
tree.root = node1
node1.left = node2
node1.right = node3

tree.dfs_preorder(tree.root)

tree.dfs_postorder(tree.root)

tree.dfs_inorder(tree.root)