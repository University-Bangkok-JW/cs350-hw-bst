class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insertNode(root, key):
    if root is None:
        return TreeNode(key)
    if key < root.val:
        root.left = insertNode(root.left, key)
    else:
        root.right = insertNode(root.right, key)
    return root

# Traversal functions
def inOrder(root):
    return inOrder(root.left) + [root.val] + inOrder(root.right) if root else []

def preOrder(root):
    return [root.val] + preOrder(root.left) + preOrder(root.right) if root else []

# Create BST and get traversals
def create_and_traverse_bst(data):
    root = None
    for num in data:
        root = insertNode(root, num)
    return {
        "inOrder": inOrder(root),
        "preOrder": preOrder(root)
    }

arrays = [
    [4, 5, 1, 3, 11],
    [2, 1, 7, 3, 10, 5, 8],
    [4, 1, 5, 3, 11, 18, 22, 7, 6, 9]
    ]

for i, data in enumerate(arrays, 1):
    print(f"Input {i}: {data}")
    result = create_and_traverse_bst(data)
    print(f"In Order: {result['inOrder']}")
    print(f"Pre Order: {result['preOrder']}")
    print("="*15)