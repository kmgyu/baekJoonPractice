class Stack:
    def __init__(self):
        self.memory = list()
    def __str__(self):
        return str(self.memory)
    def __eq__(self, other): # == 연산
        if self.memory == other.memory:
            return True
        return False
    # def __lt__(self, value):pass # a < b
    # def __le__(self, value):pass # a <= b
    # def __ne__(self, value):pass # a != b
    # def __gt__(self, value):pass # a > b
    # def __ge__(self, value):pass # a >= b
    
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

gwal1 = [')','}',']'] #closer braket
gwal2 = ['(', '{', '['] #opener braket

def check(s):
    myStack = Stack()
    for i in s:
        if i in gwal1: # opener bracket
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


def checkV2(filename, lines):
    myStack = Stack()
    stringJumper = False
    for s in range(len(lines)):
        for i in range(len(lines[s])):
            if lines[s][i] == "#" : break # 주석은 fun하고 cool하고 sexy하게 넘기다. 한줄 완전히 넘김.
            
            if stringJumper == lines[s][i] : #stringJumper로 문자열은 fun하고 cool하고 sexy하게 넘긴다.
                stringJumper = False #점퍼가 True이며, 따옴표가 나왔다는건 안넘겨도 된다는? 뜻. false로 전환하고 조건문 넘어감
            elif stringJumper: #True면 점프. 앞에서 따옴표인지 먼저 검사해줘야 한다.
                continue
            elif lines[s][i] in ['"', "'"] : #처음 따옴표를 만났을 때 작동한다.
                stringJumper = lines[s][i]
            
            if lines[s][i] in gwal1: # ) } ] 중 하나
                if not myStack.isEmpty():
                    
                    if (lines[s][i] == gwal1[0] and myStack.peek() == '(') \
                    or (lines[s][i] == gwal1[1] and myStack.peek() == '{') \
                    or (lines[s][i] == gwal1[2] and myStack.peek() == '['):
                        myStack.pop()
                    else:
                        errorMsg(3, s, i)
                        return #일치하지 않으면 브리끼
                else: 
                    errorMsg(2, s, i)
                    return #스택 비어있으면 브리끼
            elif lines[s][i] in gwal2: myStack.push(lines[s][i]) #여는 괄호면 푸시
    
    if myStack.isEmpty(): #스택 비어있으면 브리끼
        print(filename, "--->", True) #True이면 0 반환.
        return 0
    errorMsg(1, s, i)
    return

#errorMassage printer
def errorMsg(code, line, text): 
    print(f"error find: {code, line, text}", sep = ", ")

# s = input()
# if check(s):
#     print(1)
# else:
#     print(0)

relativePath = "./데이터구조및실습수업/" # this could be change....
filename = relativePath + input() + ".py"

infile = open(filename, "r", encoding="utf-8")
lines = infile.readlines()
infile.close()

checkV2(filename, lines)
#소스파일 괄호읽기프로그램 작성하기

# rule 1 : left bracket num = right bracket num
# rule 2 : same type left bracket priority > right bracket
# rule 3 : diffirent type of bracket unable to be pair.
# need to print errorcode : rule (rule) is undone and (line, text num)
# so it need to be print like : (errorcode, line, text num)

