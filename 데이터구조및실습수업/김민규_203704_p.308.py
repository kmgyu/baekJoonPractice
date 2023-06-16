
class MinHeap:  # Tree Node를 요소로 받는다. 노드의 빈도속성을 기준으로 비교한다.
    def __init__(self): #교재의 코드를 수정하여 Minimum Heap으로 수정함.
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
        while (i != 1 and n.freq < self.Parent(i).freq):
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
                if child < self.size() and self.Left(parent).freq > self.Right(parent).freq:
                    child += 1
                if last.freq < self.heap[child].freq :
                    break
                self.heap[parent] = self.heap[child]
                parent = child
                child *= 2
                
            self.heap[parent] = last
            self.heap.pop()
            return hroot

class Node:
    def __init__(self, freq, data): #frequency, data
        self.freq = freq #빈도
        self.data = data #들어갈 문자
        self.left = None
        self.right = None

def make_tree(freq):
    heap = MinHeap()
    for n in freq:
        heap.insert(n)
    # 바텀업 방식으로 접근해준다.
    for i in range(1, len(freq)):
        e1 = heap.delete()
        e2 = heap.delete()
        if len(e1.data) < len(e2.data): #e1의 길이가 길 경우, e2보다 빈도가 낮은 것이 합쳐진 노드다. 따라서 빈도수 많은게 오른쪽으로 와야함.
            e1, e2 = e2, e1 #e2가 더 많다. 그래서 스왑해줌
        e3 = Node(e1.freq+e2.freq, e1.data+e2.data) #새로운 노드 생성(부모임)
        e3.left = e1 #자식노드 이어주기.
        e3.right = e2
        heap.insert(e3) #힙 트리에 넣어줌.
    return heap.delete() #최종적으로 이진트리 반환.

def preorder(n): #전위순회방식. 이걸 사용한다고 리프노드를 최솟값부터 출력하진 않는다...
    print("Nodes by PreOrder: ", end="")
    huffmanTable = dict() # 코드표를 저장할 딕셔너리.
    stack = [[n, '', '']] #node, distance, direction
    
    while stack: #재귀는 반복문으로 구현이 가능하다...
        node, distance, direction = stack.pop()
        if node is not None: #!=을 해도 될 것 같지만... 코드 이해를 위해...
            print((node.freq, node.data, direction), end=" ") # nodes by preorder의 출력을 만족시키기 위해 direction을 추가했다.
            stack.append([node.right, distance + '0', 0])
            stack.append([node.left, distance + '1', 1])
            if node.left == node.right == None: #리프노드일때 허프만 코드표에 등록. 순회와 동시에 테이블에 등록한다.
                huffmanTable[node.data] = distance #따라서 테이블을 만들기 위해 추가적인 조회를 할 필요가 없어졌다.
    print()
    return huffmanTable #코드표를 반환한다. 코드가 좀 많이 복잡해졌다....

def tablePrint(huffmanTable): #코드표에 저장해둔걸 출력한다.
    print("symbols with Codes", huffmanTable)


# 예! 시! 코! 드!
label1 = [Node(15, 'E'), Node(12, 'T'), Node(8, 'N'), Node(6, 'I'), Node(4, 'S')]
label2 = [Node(45, 'A'), Node(13, 'B'), Node(12, 'C'), Node(16, 'D'), Node(9, 'E'), Node(5, 'F')]

huffman = make_tree(label1) #만들어진 이진트리 저장
huffmanTable = preorder(huffman) #전위순회후 만들어진 테이블 받아오기
tablePrint(huffmanTable) #출력.

huffman = make_tree(label2) #label2에서도 같은 방식으로 사용해준다.
huffmanTable = preorder(huffman)
tablePrint(huffmanTable)




