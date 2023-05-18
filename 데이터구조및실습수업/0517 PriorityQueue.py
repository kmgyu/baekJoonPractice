import math

class PriorityQueue:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return len(self.items) == 0
    def size(self): return len(self.items)
    def clear(self): self.items = []
    
    def enqueue(self, item):
        self.items.append(item)
    def findMaxIndex(self):
        if self.isEmpty(): return None
        else:
            highest = 0
            for i in range(1, self.size()):
                if self.items[i][2] > self.items[highest][2]:
                    highest = i
            return highest
    def dequeue(self):
        highest = self.findMaxIndex()
        if highest is not None:
            return self.items.pop(highest)
    def peek(self):
        highest = self.findMaxIndex()
        if highest is not None:
            return self.items[highest]

ox,oy = 5,4
dx = [0,0,1,-1]
dy = [1,-1,0,0]
def dist(x,y):
    dx, dy = ox-x, oy-y
    return math.sqrt(dx**2 + dy**2)

def mySmartSearch():
    global mapsize
    q = PriorityQueue()
    q.enqueue((0,1,-dist(0,1)))
    print('PQueue: ')
    
    while not q.isEmpty():
        here = q.dequeue()
        print(here, end='->')
        x,y,_ = here
        if (map_[y][x]=='x'):return True
        else:
            map_[y][x]='.'
            for i in range(4):
                if y+dy[i] < 0 or x+dx[i] < 0 or y+dy[i] > mapsize or x+dx[i] > mapsize:continue
                if map_[y+dy[i]][x+dx[i]] == '0' or map_[y+dy[i]][x+dx[i]] == 'x':
                    q.enqueue((x+dx[i],y+dy[i],-dist(x+dx[i],y+dy[i])))
        print('우선순위큐: ', q.items)
    return False

map_ = [['1','1','1','1','1','1'],
       ['e','0','1','0','0','1'],
       ['1','0','0','0','1','1'],
       ['1','0','1','0','1','1'],
       ['1','0','1','0','0','x'],
       ['1','1','1','1','1','1'],]
mapsize = len(map_)
mySmartSearch()