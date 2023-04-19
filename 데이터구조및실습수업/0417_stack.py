class Stack:
    def __init__(self):
        self.memory = list()
    def __str__(self):
        return str(self.memory)
    def __eq__(self, other): # == 연산
        if self.memory == other.memory:
            return True
        return False
    def __lt__(self, value):pass # a < b
    def __le__(self, value):pass # a <= b
    def __ne__(self, value):pass # a != b
    def __gt__(self, value):pass # a > b
    def __ge__(self, value):pass # a >= b
    
    
    def push(self, x):
        self.memory.append(x)
    def pop(self):
        if not self.isEmpty():
            self.memory.pop()

    def size(self): return len(self.memory)
    def isEmpty(self): return len(self.memory) == 0
    def peek(self): #맨끝의 값. top반환
        if not self.isEmpty(): return self.memory[-1]
    def clear(self): self.memory = []

odd = Stack()
even = Stack()
ruru = Stack()
for i in range(10):
    if i%2 == 0:
        even.push(i)
        ruru.push(i)
    else: odd.push(i)
print(even.peek())
print(odd)
print(even == odd)
print(even == ruru)