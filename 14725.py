class TrieNode:
    def __init__(self):
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, words):
        cur_node = self.root
        for word in words:
            if word not in cur_node.children:
                cur_node.children[word] = TrieNode()
            cur_node = cur_node.children[word]

    def __str__(self):
        result = ''
        
        def dfs(node, depth):
            nonlocal result
            for key in sorted(node.children):
                result += '--'*depth + key + '\n'
                dfs(node.children[key], depth+1)
        dfs(self.root, 0)
        return result
input = open(0).readline

N = int(input())
trie = Trie()
for _ in range(N):
    trie.insert(input().split()[1:])

print(trie)