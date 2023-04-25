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

s = input()
gwal1 = [')','}',']']
gwal2 = ['(', '{', '[']



def check(s):
    myStack = Stack()
    for i in s:
        if i in gwal1: # ) } ] 중 하나.
            if not myStack.isEmpty():
                if (i == gwal1[0] and myStack.peek() == '(') \
                or (i == gwal1[1] and myStack.peek() == '{') \
                or (i == gwal1[2] and myStack.peek() == '['):
                    myStack.pop()
                else: return False #일치하지 않으면 브리끼
            else: return False #스택 비어있으면 브리끼
        
        elif i in gwal2: myStack.push(i) #여는 괄호면 푸시
    
    if myStack.isEmpty(): #스택 비어있으면 브리끼
        return True
    return False


def checkV2(lines):
    myStack = Stack()
    for s in lines:
        for i in s:
            if i in gwal1: # ) } ] 중 하나.
                if not myStack.isEmpty():
                    if (i == gwal1[0] and myStack.peek() == '(') \
                    or (i == gwal1[1] and myStack.peek() == '{') \
                    or (i == gwal1[2] and myStack.peek() == '['):
                        myStack.pop()
                    else: return False #일치하지 않으면 브리끼
                else: return False #스택 비어있으면 브리끼
            
            elif i in gwal2: myStack.push(i) #여는 괄호면 푸시
    
    if myStack.isEmpty(): #스택 비어있으면 브리끼
        return True
    return False



if check(s):
    print(1)
else:
    print(0)





filename = "ArrayStack.h"
infile = open(filename, "r")
lines = infile.readlines()
infile.close()

result = checkV2(lines)
print(filename, "--->", result)
#소스파일 괄호읽기프로그램 작성하기