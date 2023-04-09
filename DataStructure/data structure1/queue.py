from sys import stdin
input = stdin.readline
n = int(input())
q = list()
for _ in range(n):
    a = list(map(str, input().split()))
    if a[0] == "push":
        q.append(a[1])
    if a[0] == "pop":
        if len(q) != 0:
            print(q.pop(0))
        else:
            print(-1)
    if a[0] == "size":
        print(len(q))
    if a[0] == "empty":
        if len(q) != 0:
            print(0)
        else :
            print(1)
    if a[0] == "front":
        if len(q) != 0:
            print(q[0])
        else:
            print(-1)
    if a[0] == "back":
        if len(q) != 0:
            print(q[-1])
        else:
            print(-1)
# 돚거했다.
# import sys
# import queue
# input=lambda:sys.stdin.readline().rstrip()
#
# n=int(input())
# q=queue.Queue()
#
# for _ in range(n):
#     com,*num=input().split()
#     if com=='push':
#         q.put(int(num[0]))
#     elif com=='pop':
#         print(q.get() if not q.empty() else -1)
#     elif com=='size':
#         print(q.qsize())
#     elif com=='empty':
#         print(1 if q.empty() else 0)
#     elif com=='front':
#         print(q.queue[0] if not q.empty() else -1)
#     elif com=='back':
#         print(q.queue[-1] if not q.empty() else -1)