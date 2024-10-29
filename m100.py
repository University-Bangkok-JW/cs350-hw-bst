class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self.insertNode(self.root, value)

    def insertNode(self, cur, value):
        if value < cur.value:
            if cur.left:
                self.insertNode(cur.left, value)
            else:
                cur.left = Node(value)
        else:
            if cur.right:
                self.insertNode(cur.right, value)
            else:
                cur.right = Node(value)

arrays = [1, 10, 8, 4, 6, 3, 2, 5]

bst = BST()
for i in arrays:
    bst.insert(i)
