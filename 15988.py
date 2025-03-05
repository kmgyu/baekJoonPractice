import sys
input = sys.stdin.readline
k = int(input())
mod = 1000000009
d = [1, 2, 4]
ques = []
for i in range(k):
    ques.append(int(input()))
for i in range(3, max(ques)):
    if d[i-1]+d[i-2]+d[i-3]>mod:
        d.append((d[i-1]+d[i-2]+d[i-3])%mod)
    else:
        d.append(d[i-1]+d[i-2]+d[i-3])
    
for i in ques:
    print(d[i-1]%mod)