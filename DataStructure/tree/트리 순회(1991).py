from sys import stdin
input = stdin.readline

class Tree:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

def preorder(node):
    if node != None:
        print(tree[node].data, end="")
        preorder(tree[node].left)
        preorder(tree[node].right)

def inorder(node):
    if node != None:
        inorder(tree[node].left)
        print(tree[node].data, end="")
        inorder(tree[node].right)

def postorder(node):
    if node != None:
        postorder(tree[node].left)
        postorder(tree[node].right)
        print(tree[node].data, end="")

tree = dict()
n = int(input())
for i in range(n):
    node, l, r = input().split()
    if l == '.': l = None
    if r == '.': r = None
    tree[node] = Tree(node, l, r)

preorder('A')
print()
inorder('A')
print()
postorder('A')