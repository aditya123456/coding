

class Node:
    def __init__(self, key):
        self.key = key
        self.child = []

    def addElement(self, key):
        new_node = Node(key)
        self.child.append(new_node)

class Tree:
    def __init__(self):
        self.root = None


node1 = Node(1)
node2 = Node(3)
node3 = Node(4)
node4 = Node(5)
tree = Tree()
tree.root = node1
node1.addElement(node2)
node1.addElement(node3)
node2.addElement(node4)

print(tree.root)


def traverse(node):
    if node.child:
        pass
    else:
        print(node.key)
    for child in node.child:
        traverse(child)
traverse(tree.root)


