class TNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def preorder(node):
    if node == None: return
    print(node.data, end=' ')
    preorder(node.left)
    preorder(node.right)

def inorder(node):
    if node == None: return
    inorder(node.left)
    print(node.data, end=' ')
    inorder(node.right)

def postorder(node):
    if node == None: return
    postorder(node.left)
    postorder(node.right)
    print(node.data, end=' ')

def test_tree():
    # test driver
    root = TNode(6)
    # 경사트리면 그냥 바로 할 수 있잖아.
    
    return root
    

if __name__ == "__main__":
    tree = test_tree()
    print("후위 순회 결과")
    postorder(tree)