from sys import stdin
input = stdin.readline
class MaxHeap: # 참고용 Maximum Heap.
    def __init__(self):
        self.heap = []
        self.heap.append(0)
    
    def size(self) : return len(self.heap) -1
    def isEmpty(self) : return self.size() == 0
    def Parent(self, i) : return self.heap[i//2]
    def Left(self, i) : return self.heap[i*2]
    def Right(self, i) : return self.heap[i*2+1]
    
    def insert(self, n):
        self.heap.append(n)
        i = self.size()
        while (i != 1 and n > self.Parent(i)):
            self.heap[i] = self.Parent(i)
            i = i//2
        self.heap[i] = n
    
    def delete(self):
        parent = 1
        child = 2
        if not self.isEmpty():
            hroot = self.heap[1]
            last = self.heap[self.size()]
            while (child <= self.size()):
                if child < self.size() and self.Left(parent) < self.Right(parent):
                    child += 1
                if last >= self.heap[child] :
                    break
                self.heap[parent] = self.heap[child]
                parent = child
                child *= 2
                
            self.heap[parent] = last
            self.heap.pop()
            return hroot
        else:
            return 0

n = int(input())
heap = MaxHeap()
cnt = 0
for i in range(n):
    a = int(input())
    if a == 0:
        print(heap.delete())
    else:
        heap.insert(a)
# for i in range(n):
#     a = int(input())
#     if a == 0:
#         parent = 1
#         child = 2
#         size = len(heap)-1
#         if size > 1:
#             hroot = heap[1]
#             last = heap[-1]
#             while child <= size:
#                 if child < size and heap[parent*2] < heap[parent*2+1]:
#                     child += 1
#                 if last >= heap[child]:
#                     break
#                 heap[parent] = heap[child]
#                 parent = child
#                 child *= 2
#             heap[parent] = last
#             heap.pop()
#             print(hroot)
#             print(heap)
#         else:
#             print(0)
#     else:
#         heap.append(n)
#         j = len(heap)-1
#         while (j != 1 and n > j//2):
#             heap[j] = heap[j//2]
#             j = j//2
#         heap[j] = a



