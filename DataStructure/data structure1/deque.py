from sys import stdin
input = stdin.readline
n = int(input())
li = list()

for i in range(n):
    Q = list(map(str, input().split()))
    if "push_front" in Q:
        li.insert(0, Q[-1])
    elif "push_back" in Q:
        li.append(Q[-1])
    elif "pop_front" in Q:
        if len(li):
            print(li.pop(0))
        else:
            print(-1)
    elif "pop_back" in Q:
        if len(li):
            print(li.pop())
        else:
            print(-1)
    elif "size" in Q:
        print(len(li))
    elif "empty" in Q:
        if len(li):
            print(0)
        else:
            print(1)
    elif "front" in Q:
        if len(li):
            print(li[0])
        else:
            print(-1)
    elif "back" in Q:
        if len(li):
            print(li[-1])
        else:
            print(-1)
