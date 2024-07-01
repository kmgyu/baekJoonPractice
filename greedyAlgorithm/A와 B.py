from collections import deque

s = input()
t = input()
temp = deque(t)

for i in range(len(t)-len(s)):
    if temp.pop() == "B": temp.reverse()

for a,b in zip(s,temp):
    if a != b:
        print(0); break
else: print(1)
