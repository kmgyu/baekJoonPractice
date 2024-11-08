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

    four = TNode(4)
    nine = TNode(9)
    root.left = four
    root.right = nine

    two = TNode(2)
    five = TNode(5)
    four.left = two
    four.right = five

    one = TNode(1)
    three = TNode(3)
    two.left = one
    two.right = three

    seven = TNode(7)
    ten = TNode(10)
    nine.left = seven
    nine.right = ten

    nine_2 = TNode(9)
    eleven = TNode(11)
    ten.left = nine_2
    ten.right = eleven
    
    return root
    

if __name__ == "__main__":
    tree = test_tree()
    print("전위 순회 결과")
    preorder(tree)
    print()
    print("중위 순회 결과")
    inorder(tree)
    print()
    print("후위 순회 결과")
    postorder(tree)