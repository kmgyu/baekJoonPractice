def path_length(root):
    ans = 0
    ansString = [] #경로길이 저장.
    stack = [[root, 0]] #Node, distance
    
    while stack: #후위 순회를 이용했음.
        node, dis = stack.pop()
        ans += dis
        ansString.append(dis)
        if node.left != None:
            stack.append([node.left, dis+1])
        if node.right != None:
            stack.append([node.right, dis+1])
    print(*ansString, sep="+", end="=")
    print(ans)

def reverse(root):
    # root노드를 받아와 연결된 걸 전부 스왑해준다.
    # 트리째로 받아오려면 많이 복잡해져서 그냥 기존 객체 스왑하는 걸로 만들어줬음.
    # 가리키는 객체는 똑같으니 작동은 하는데 많이 위험한? 방법으로 보인다.
    stack = [root] #Node, distance
    
    while stack: #후위 순회를 이용했음.
        node = stack.pop()
        if node != None: # None은 여기서 걸러낸다.
            node.left, node.right = node.right, node.left #swap한다.
            stack.append(node.left)
            stack.append(node.right)

class Node:
    def __init__(self, data, left = None, right = None): #frequency, data
        self.data = data #들어갈 문자
        self.left = left
        self.right = right

def preorder(n, level = 0): #테스트용 전위순회 코드. 재귀로 구현함.
    if n is not None:
        print(n.data, level)
        preorder(n.left, level+1)
        preorder(n.right, level+1)

#Test Tree
f = Node('F')
d = Node('D')
c = Node('C')
e = Node('E', None, f)
b = Node('B', c, d)
a = Node('A', b, e) #Root Node
path_length(a) #경로 길이 전부 합한 값 출력
reverse(a)
preorder(a)
