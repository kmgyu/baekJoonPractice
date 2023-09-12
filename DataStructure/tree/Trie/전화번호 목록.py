# https://velog.io/@kimdukbae/%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-%ED%8A%B8%EB%9D%BC%EC%9D%B4-Trie
import sys
def input(): return sys.stdin.readline().rstrip()

class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}

class Trie(object):
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        curr_node = self.head
        for char in string:
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)
            if curr_node.data or curr_node.children[char].data :
                return False
            curr_node = curr_node.children[char]
        curr_node.data = True
        return True

    def search(self, string):
        curr_node = self.head
        for char in string:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
            else:
                return False
        if curr_node.data is not None:
            return True

t = int(input())
for i in range(t):
    n = int(input())
    tree = Trie()
    datas = [input() for _ in range(n)]
    datas.sort()
    for s in datas:
        if not tree.insert(s):
            print("NO")
            break
    else:
        print("YES")


