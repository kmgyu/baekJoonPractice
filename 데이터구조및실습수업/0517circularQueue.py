
class CircularQueue:
    def __init__(self):
        self.front = 0
        self.rear = 0
        self.items = [None] * MAX_qsize
    def isEmpty(self):return self.front == self.rear
    def isFull(self):return self.front == (self.rear+1)%MAX_qsize
    def clear(self):self.front = self.rear
    
    def enqueue(self, item):
        if not self.isFull():
            self.rear = (self.rear+1)%MAX_qsize
            self.items[self.rear] = item
    
    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front+1)%MAX_qsize
            return self.items[self.front]
    
    def peek(self):
        if not self.isEmpty():
            return self.items[(self.front+1)%MAX_qsize]
    
    def size(self):
        return (self.rear - self.front + MAX_qsize) % MAX_qsize
    def display(self):
        out = []
        if self.front < self.rear:
            out = self.items[self.front+1:self.rear+1]
        else:
            out = self.items[self.front+1:MAX_qsize] \
                + self.items[0:self.rear+1]
        print(f"f={self.front}, r={self.rear} ==> {out}")

dx = [0,0,1,-1]
dy = [1,-1,0,0]
def bfs():
    que = CircularQueue()
    que.enqueue((0,1))
    print('BFS: ')
    
    while not que.isEmpty():
        here = que.dequeue()
        print(here, end="->")
        x,y = here
        if(map[y][x] == 'x') : return True
        else:
            map[y][x] = '.'
        for i in range(4):
            if map[y+dy[i]][x+dx[i]] == '0' or map[y+dy[i]][x+dx[i]] == 'x':
                que.enqueue((x+dx[i],y+dy[i]))
    return False

map = [['1','1','1','1','1','1'],
       ['e','0','1','0','0','1'],
       ['1','0','0','0','1','1'],
       ['1','0','1','0','1','1'],
       ['1','0','1','0','0','x'],
       ['1','1','1','1','1','1'],]

MAX_qsize = 10
result = bfs()
if result : print("--> 미로탐색 성공")
else : print('--> 미로탐색 실패')