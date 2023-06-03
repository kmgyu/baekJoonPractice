class CircularQueue:
    def __init__(self):
        self.front = 0
        self.rear = 0
        self.items = [None] * MAX_qsize
    def isEmpty(self):return self.front == self.rear
    def isFull(self):return self.front == (self.rear+1)%MAX_qsize
    def clear(self):self.front = self.rear
    
    def enqueue(self, item):
        if not self.isFull():
            self.rear = (self.rear+1)%MAX_qsize
            self.items[self.rear] = item
    
    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front+1)%MAX_qsize
            return self.items[self.front]
    
    def peek(self):
        if not self.isEmpty():
            return self.items[(self.front+1)%MAX_qsize]
    
    def size(self):
        return (self.rear - self.front + MAX_qsize) % MAX_qsize
    def display(self):
        out = []
        if self.front < self.rear:
            out = self.items[self.front+1:self.rear+1]
        else:
            out = self.items[self.front+1:MAX_qsize] \
                + self.items[0:self.rear+1]
        print(f"f={self.front}, r={self.rear} ==> {out}")



# 노드 선언부
class TNode:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right



""" 전위, 중위, 후위, 레벨 순회 부분."""
def preorder(n):
    if n is not None:
        print(n.data, end=" ")
        preorder(n.left)
        preorder(n.right)

def inorder(n):
    if n is not None:
        inorder(n.left)
        print(n.data, end=" ")
        inorder(n.right)

def postorder(n):
    if n is not None:
        postorder(n.left)
        postorder(n.right)
        print(n.data, end=" ")

def levelorder(root):
    queue = CircularQueue()
    queue.enqueue(root)
    while not queue.isEmpty():
        n = queue.dequeue()
        if n is not None:
            print(n.data, end=' ')
            queue.enqueue(n.left)
            queue.enqueue(n.right)



# 노드 갯수세기
def count_node(n):
    if n is None:
        return 0
    else:
        return 1 + count_node(n.left) + count_node(n.right)
# 리프노드 계산
def count_leaf(n):
    if n is None:
        return 0
    elif n.left is None and n.right is None:
        return 1
    else:
        return count_leaf(n.left) + count_leaf(n.right)

# 높이 계산
def calc_height(n):
    if n is None:
        return 0
    hLeft = calc_height(n.left)
    hRight = calc_height(n.right)
    if (hLeft > hRight):
        return hLeft + 1
    else:
        return hRight + 1

#코드 선언부

# 레벨순회 카운트 리스트 288까지.
MAX_qsize = 6 #원형 큐 사이즈. 클래스에 적으면 읽기 힘들것같아서 선어눕분에 적음.

d = TNode('D', None, None)
e = TNode('E', None, None)
b = TNode('B', d, e)
f = TNode('F', None, None)
c = TNode('C', f, None)
root = TNode('A', b, c)

print('\n In-Order : ', end='')
inorder(root)
print('\n Pre-Order : ', end='')
preorder(root)
print('\n Post-Order : ', end='')
postorder(root)
print('\n Level-Order : ', end='')
levelorder(root)
print()

print(f"노드 개수 = {count_node(root)}개")
print(f"단말의 개수 = {count_leaf(root)}개")
print(f"트리의 높이 = {calc_height(root)}")
# 교재내용 -------------------------------------------------------------



#레벨 오더 이용 카운트노드. 책에서 나온거 아니고 직접만든거
def count_node2(root):
    cnt = 0
    queue = CircularQueue()
    queue.enqueue(root)
    while not queue.isEmpty():
        n = queue.dequeue()
        if n is not None:
            cnt += 1
            queue.enqueue(n.left)
            queue.enqueue(n.right)
    return cnt
print(f"노드 개수 = {count_node2(root)}개")