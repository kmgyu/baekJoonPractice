from collections import deque

class MaxHeap: # 참고용 Maximum Heap.
    def __init__(self):
        self.heap = []
        self.heap.append(0)
    
    def size(self) : return len(self.heap) -1
    def isEmpty(self) : return self.size() == 0
    def Parent(self, i) : return self.heap[i//2]
    def Left(self, i) : return self.heap[i*2]
    def Right(self, i) : return self.heap[i*2+1]
    def display(self, msg = "힙 트리: ") :
        print(msg, self.heap[1:])
    
    def insert(self, n):
        self.heap.append(n)
        i = self.size()
        while (i != 1 and n > self.Parent(i)):
            self.heap[i] = self.Parent(i)
            i = i//2
        self.heap[i] = n
    
    def delete(self):
        parent = 1
        child = 2
        if not self.isEmpty():
            hroot = self.heap[1]
            last = self.heap[self.size()]
            while (child <= self.size()):
                if child < self.size() and self.Left(parent) < self.Right(parent):
                    child += 1
                if last >= self.heap[child] :
                    break
                self.heap[parent] = self.heap[child]
                parent = child
                child *= 2
                
            self.heap[parent] = last
            self.heap.pop()
            return hroot


# Tree Node를 요소로 받게 조금의 수정을 가한 Minimum Heap.
class MinHeap: 
    def __init__(self):
        self.heap = []
        self.heap.append(0)
    
    def size(self) : return len(self.heap) -1
    def isEmpty(self) : return self.size() == 0
    def Parent(self, i) : return self.heap[i//2]
    def Left(self, i) : return self.heap[i*2]
    def Right(self, i) : return self.heap[i*2+1]
    def display(self, msg = "힙 트리: ") :
        print(msg, self.heap[1:])
    
    def insert(self, n):
        self.heap.append(n)
        i = self.size()
        while (i != 1 and n.data < self.Parent(i).data):
            self.heap[i] = self.Parent(i)
            i = i//2
        self.heap[i] = n
    
    def delete(self):
        parent = 1
        child = 2
        if not self.isEmpty():
            hroot = self.heap[1]
            last = self.heap[self.size()]
            while (child <= self.size()):
                if child < self.size() and self.Left(parent).data > self.Right(parent).data:
                    child += 1
                if last.data < self.heap[child].data :
                    break
                self.heap[parent] = self.heap[child]
                parent = child
                child *= 2
                
            self.heap[parent] = last
            self.heap.pop()
            return hroot


class TNode:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right


def make_tree(freq):
    heap = MinHeap()
    resultHeap = MaxHeap()
    for n in freq:
        heap.insert(TNode(n, None, None))
    
    for i in range(1, len(freq)):
        e1 = heap.delete()
        e2 = heap.delete()
        heap.insert(TNode(e1.data+e2.data, e1, e2))
        print(f"node added : ({e1.data} + {e2.data})")
    return heap


def levelorder(root): #경로 저장이 편하게 레벨 순회를 사용했음.
    queue = deque() #Circular Queue까지 가져오기엔 너무 코드가 길어져 collections에서 deque를 가져왔습니다...
    queue.append([root, '']) # queue에 경로도 문자열 형태로 저장.
    while queue:
        n, dis = queue.popleft() # node and distance
        if n is not None:
            # print(n.data, end=' ')
            queue.append([n.left, dis+'1'])
            queue.append([n.right, dis+'0'])
            if n.left == n.right == None:
                print(f"Char : {label[freq.index(n.data)]} / frequency : {n.data} / HuffmanCode : {dis}")
                # index 조회로 인해 시간복잡도가 높아졌다... 다른 순회 방식을 사용하려 해봐도 딱히 좋은 방법은 생각나지 않는다.
                # 다른 순회방법에서도 어쩔 수 없이 index를 쓰게된다...

def preorder(n, dis=''): #전위순회방식. 이걸 사용한다고 리프노드를 최솟값부터 출력하진 않는다...
    if n is not None: #왜냐하면 만드는 과정에서 완전이진트리로 만든다는 보장이 없다... 최소 힙으로 만들거든...
        # print(n.data, end=" ")
        preorder(n.left, dis+'1')
        preorder(n.right, dis+'0')
        if n.left == n.right == None:
                print(f"Char : {label[freq.index(n.data)]} / frequency : {n.data} / HuffmanCode : {dis}")
                # frequency list랑 label list를 2차원 리스트로 만들어서 key를 frequency로 설정하고 정렬을 한번 해주면 되지 않을까?
                # 이분탐색해주면 트리순회의 시간복잡도가 n^2에서 nlog n이 걸릴 것이다... 끔찍하게 많아진 시간복잡도를 조금 덜 끔찍하게 만들어준다...
                # 근데 이분탐색은 또 언제 만드냐... 안할래 힘들어...

label = ['E', 'T', 'N', 'I', 'S']
freq = [15, 12, 8, 6, 4]


#허프만코딩트리 생성
resultHeap = make_tree(freq) #단 하나의 이진트리로 압축됨.
huffman = resultHeap.delete() #압축된 이진트리를 사용하기 쉽게 만들어줌.

print("---레벨 순회 방식---")
levelorder(huffman)
print("---전위 순회 방식---")
preorder(huffman)
# 317p 8.5 ~ 8.6을 과제로 추가로? 제출하면 된다.
# 9.4(AVL 트리) 안함 대신 10장(그래프)함.
# 탐색은 해시 안나감.