import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def find(n):
    if dock[n] == n:
        return n
    dock[n] = find(dock[n])
    return dock[n]

g = int(input())
p = int(input())
plane = [int(input()) for _ in range(p)]

dock = list(range(g+1))
gate = [0] * (g+1)

cnt = 0
for i in range(p):
    tmp = find(min(plane[i], g))
    if tmp != 0 and gate[tmp] == 0:
        gate[tmp] = 1
        dock[tmp] -= 1
        cnt += 1
    else: break

print(cnt)