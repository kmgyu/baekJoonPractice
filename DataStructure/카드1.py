import sys
from collections import deque
input = sys.stdin.readline
c = deque(list(range(1, int(input())+1)))
card = []
while c:card.append(c.popleft());c.rotate(-1)
print(*card)