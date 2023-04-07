import sys

input = sys.stdin.readline
n = int(input())
stk = list()
for i in range(0, n):
    s = input().split()
    sl = len(stk)
    if s[0] == "push":
        stk.append(s[1])
    elif s[0] == "pop":
        if sl:
            print(stk[sl-1])
            stk.pop()
        else:
            print(-1)
    elif s[0] == "size":
        print(sl)
    elif s[0] == "empty":
        if sl:
            print(0)
        else:
            print(1)
    elif s[0] == "top":
        if sl:
            print(stk[sl-1])
        else:
            print(-1)


# class Stack:
#     def __init__(self):
#         self.memory = list()
#
#     def push(self, x):
#         self.memory.append(x)
#
#     def pop(self):
#         if len(self.memory):
#             print(self.memory[len(self.memory)-1])
#             self.memory.pop(len(self.memory)-1)
#         else:
#             print(-1)
#
#     def size(self):
#         print(len(self.memory))
#
#     def empty(self):
#         if len(self.memory):
#             print(0)
#         else:
#             print(1)
#
#     def top(self):
#         if len(self.memory):
#             print(self.memory[len(self.memory)-1])
#         else:
#             print(-1)
#
#
# n = int(input())
# stk = Stack()
# for i in range(0, n):
#     s = input().split()
#     if s[0] == "push":
#         stk.push(int(s[1]))
#     elif s[0] == "pop":
#         stk.pop()
#     elif s[0] == "size":
#         stk.size()
#     elif s[0] == "empty":
#         stk.empty()
#     elif s[0] == "top":
#         stk.top()

