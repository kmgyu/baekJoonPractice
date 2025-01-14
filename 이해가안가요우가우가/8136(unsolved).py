import sys
import collections
input = sys.stdin.readline

class Node:
    def __init__(self):
        self.children = collections.defaultdict(Node)
        self.word_id = -1
        self.palindrome_word_ids = []
        
class Trie:
    def __init__(self):
        self.root = Node()
        
    @staticmethod
    def is_palindrome(word: str) -> bool:
        return word[::] == word[::-1]
    
    # 단어 삽입
    def insert(self, index, word) -> None:
        node = self.root
        for i, char in enumerate(reversed(word)):
            if self.is_palindrome(word[0:len(word) - i]):
                node.palindrome_word_ids.append(index)
            node = node.children[char]
        node.word_id = index
        
    # 단어 판별
    def search(self, index, word):
        result = 0
        node = self.root
        
        while word:
            if node.word_id >= 0:
                if self.is_palindrome(word):
                    result += 1
            if not word[0] in node.children:
                return result
            node = node.children[word[0]]
            word = word[1:]
        
        if node.word_id >= 0 and node.word_id != index:
            result += 1
            
        for palindrome_word_id in node.palindrome_word_ids:
            result += 1
            
        return result


n = int(input())
words = [input().split()[1] for _ in range(n)]

trie = Trie()
        
for i, word in enumerate(words):
    trie.insert(i, word)
    
results = 0
for i, word in enumerate(words):
    results += trie.search(i, word)

print(results+n)