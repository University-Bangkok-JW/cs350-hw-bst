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

def postOrder(root):
    return postOrder(root.left) + postOrder(root.right) + [root.val] if root else []

# Create BST and get traversals
def create_and_traverse_bst(data):
    root = None
    for num in data:
        root = insertNode(root, num)
    return {
        "inOrder": inOrder(root),
        "preOrder": preOrder(root),
        "postOrder": postOrder(root)
    }

arrays = [
    [4, 5, 1, 3, 11],
    [2, 1, 7, 3, 10, 5, 8],
    [4, 1, 5, 3, 11, 18, 22, 7, 6, 9]
    ]

print("="*15)
for i, data in enumerate(arrays, 1):
    print(f"Question {i}: {data}")
    print("-"*15)
    result = create_and_traverse_bst(data)
    print(f"In Order: {result['inOrder']}")
    print(f"Pre Order: {result['preOrder']}")
    print(f"Post Order: {result['postOrder']}")
    print("="*15)

###############
# Question 4 ##
###############
# Expression
class ExprTreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.val = value

# Helper functions for infix to expression tree
def precedence(op):
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    return 0

def exprTreeInfix(tokens):
    def buildTree(stack, opStack):
        right = stack.pop()
        left = stack.pop()
        operator = opStack.pop()
        node = ExprTreeNode(operator)
        node.left = left
        node.right = right
        stack.append(node)

    stack, opStack = [], []
    i = 0
    while i < len(tokens):
        if tokens[i].isdigit():
            stack.append(ExprTreeNode(tokens[i]))
        elif tokens[i] == '(':
            opStack.append(tokens[i])
        elif tokens[i] == ')':
            while opStack[-1] != '(':
                buildTree(stack, opStack)
            opStack.pop()
        else:
            while (opStack and opStack[-1] != '(' and
                   precedence(opStack[-1]) >= precedence(tokens[i])):
                buildTree(stack, opStack)
            opStack.append(tokens[i])
        i += 1
    while opStack:
        buildTree(stack, opStack)
    return stack[0]

def printInorder(node):
    if node:
        if node.left or node.right:
            print("(", end="")
        printInorder(node.left)
        print(node.val, end="")
        printInorder(node.right)
        if node.left or node.right:
            print(")", end="")

###############
# Question 4 ##
###############
# Infix notation to token list
print("Question 4")
questionText = "6 - 8 / ( 1 + 3 ) * 2"
tokens = questionText.split()
tree = exprTreeInfix(tokens)

print("Inorder of expression tree for Infix notation '6 - 8 / (1 + 3) * 2':")
printInorder(tree)
print()
print("="*15)

###############
# Question 5 ##
###############
# Function to build expression tree from prefix notation
def exprTreePrefix(tokens):
    token = tokens.pop(0)
    node = ExprTreeNode(token)
    if token in "+-*/":
        node.left = exprTreePrefix(tokens)
        node.right = exprTreePrefix(tokens)
    return node

# Prefix notation to token list
print("Question 5")
questionText = "+ * 4 2 / - 8 2 3"
tokens = questionText.split()
tree = exprTreePrefix(tokens)
print("Inorder of expression tree for Prefix notation '+ * 4 2 / - 8 2 3':")
printInorder(tree)
print()
print("="*15)
