#우선순위 큐를 이용ㅎ아여 임의의 리스트로부터 k번째 큰 항목을 찾는 프로그램 작성하기
import random
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
                if self.items[i] > self.items[highest]:
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

k = int(input("몇번째로 큰 요소를 찾을 건지?????? : "))
print(f"{k}번째로 큰 요소를 찾으시오!!!!")
qsize = 30
Pq = PriorityQueue()
for i in range(qsize): #qsize내에서 난수생성으로 임의의 값을 가진 요소 추기.
    Pq.enqueue(random.randrange(1,100))
print(f"임의생성 리스트: {Pq.items}")
for i in range(k-1):
    Pq.dequeue()
print(f"{k}로 큰 요소는 {Pq.dequeue()}입니다.")