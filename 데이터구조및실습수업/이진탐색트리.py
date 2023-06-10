class BSTNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

def search_bst(n, key):
    if n == None:
        return None
    elif key == n.key:
        return n
    elif key < n.key:
        return search_bst(n.left, key)
    else:
        return search_bst(n.right, key)

def search_bst_iter(n,key):
    while n != None:
        if key == n.key:
            return n
        elif key < n.key:
            n = n.left
        else:
            n = n.right
            
    return None

def search_value_bst(n, value):
    if n == None: return None
    elif value == n.value:
        return n
    res = search_value_bst(n.left, value)
    if res is not None:
        return res
    else:
        return search_value_bst(n.right, value)

def search_max_bst(n):
    while n != None and n.right != None:
        n = n.right
    return n

def search_min_bst(n):
    while n != None and n.left != None:
        n = n.left
    return n

def insert_bst(r, n):
    if n.key < r.key:
        if r.left is None:
            r.left = n
            return True
        else:
            return insert_bst(r.left,n)
    elif n.key > r.key:
        if r.right is None:
            r.right = n
            return True
        else:
            return insert_bst(r.right, n)
    else:
        return False

def delete_bst_case1(parent, node, root):
    if parent is None:
        root = None
    else:
        if parent.left == node:
            parent.left = None
        else:
            parent.right = None
    return root

def delete_bst_case2(parent, node, root):
    if node.left is not None:
        child = node.left
    else:
        child = node.right
    
    if node == root:
        root = child
    else:
        if node is parent.left:
            parent.left = child
        else:
            parent.right = child
    return root

def delete_bst_case3(parent, node, root):
    succp = node
    succ = node.right
    while(succ.left != None):
        succp = succ
        succ = succ.left
    
    if(succp.left == succ):
        succp.left = succ.right
    else:
        succp.right = succ.right
    node.key = succ.key
    node.value = succ.value
    return root

def delete_bst(root, key):
    if root == None : return None
    
    parent = None
    node = root
    while node != None and node.key != key:
        parent = node
        if key < node.key : node = node.left
        else : node = node.right
        
    # if node == None: return None 삭제할 노드가 없음의 원래 코드. 조금 바꿨다. 이렇게하면 삭제대상없으면 BST맵에서 root가 지워짐.
    if node == None:
        print("삭제 할 대상을 찾지 못홤.")
    elif node.left == None and node.right == None:
        root = delete_bst_case1(parent, node, root)
    elif node.left == None or node.right == None:
        root = delete_bst_case2(parent, node, root)
    else :
        root = delete_bst_case3(parent, node, root)
    return root



#8장 메서드 끌어옴
def inorder(n):
    if n is not None:
        inorder(n.left)
        print(n.key, end=" ")
        inorder(n.right)

def count_node(n):
    if n is None:
        return 0
    else:
        return 1 + count_node(n.left) + count_node(n.right)

#이진탐색트리를 이용한 맵
class BSTMap():
    def __init__(self):
        self.root = None
        
    def isEmpty(self): return self.root == None
    def clear(self): self.root = None
    def size(self): return count_node(self.root) #8장 트리 함수
    def search(self, key): return search_bst(self.root, key)
    def searchValue(self, key): return search_value_bst(self.root, key)
    def findMax(self): return search_max_bst(self.root)
    def findMin(self): return search_min_bst(self.root)
    
    def insert(self, key, value=None):
        n = BSTNode(key, value)
        if self.isEmpty():
            self.root = n
        else:
            insert_bst(self.root, n)
    
    def delete(self, key):
        self.root = delete_bst(self.root, key)
    
    def display(self, msg = 'BSTMap :'):
        print(msg, end='')
        inorder(self.root)
        print()

map_ = BSTMap()
data = [35, 18, 7, 26, 12, 3, 68, 22, 30, 99]

print("[삽입 연산] : ", data)
for key in data:
    map_.insert(key)
map_.display("[중위 순회] : ")

if map_.search(26) != None: print('[탐색 26] : 성공')
else: print('[탐색 26] : 탐색 실패')
if map_.search(25) != None: print('[탐색 25] : 성공')
else: print('[탐색 25] : 탐색 실패')

map_.delete(3); map_.display("[3 삭제] : ")
map_.delete(68); map_.display("[68 삭제] : ")
map_.delete(18); map_.display("[18 삭제] : ")
map_.delete(35); map_.display("[35 삭제] : ")
map_.delete(3); map_.display("[3 삭제] : ")

