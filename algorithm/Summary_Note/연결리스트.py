class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

root_node = Node(0)
node_1 = None(1)
node_2 = None(2)

# 왼쪽에 넣어
root_node.left = node_1
node_1.parent = root_node

# 오른쪽에 넣어
root_node.right = node_2