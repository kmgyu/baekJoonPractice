MAX_QSIZE = 10
class CircularQueue:
    def __init__(self):
        self.front = 0
        self.rear = 0
        self.items = [None]*MAX_QSIZE
    def isEmpty(self):return self.front == self.rear
    def isFull(self):return self.front == (self.rear+1)%MAX_QSIZE
    def clear(self): self.front = self.rear
    def enqueue(self, item):
        if not self.isFull():
            self.rear = (self.rear+1)%MAX_QSIZE
            self.items[self.rear] = item
        
    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front+1)%MAX_QSIZE
            return self.items[self.front]
    
    def peek(self):
        if not self.isEmpty():
            return self.items[(self.front+1)%MAX_QSIZE]
    
    def size(self):
        return (self.rear-self.front+MAX_QSIZE)%MAX_QSIZE
    
    def display(self):
        out = []
        if self.front < self.rear:
            out = self.items[self.front+1:self.rear+1]
        else:
            out = self.items[self.front+1:MAX_QSIZE] \
                + self.items[0:self.rear+1]
        print("[f=%s,r=%d] ==> "%(self.front, self.rear), out)

q = CircularQueue()
for i in range(8): q.enqueue(i)
q.display()
for i in range(5): q.dequeue()
q.display()
for i in range(8, 14): q.enqueue(i)
q.display()

# 원형큐에서 front와rear를 중복된 인덱스에 놓지 않는 이유:
# 포화상태와 공백상태 구분

# 원형큐는 논리적인 원형구조, 물리적으로는 선형

# front == rear가 공백상태인 이유
# 하나 삽입하고 없애보셈.
# 수학적 사고 + 알고리즘적 사고가 필요한 법이다..
# front와 rear가 움직이는 것이 어렵다..흑흑
