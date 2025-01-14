import sys
def input(): return sys.stdin.readline().rstrip()

def solve(line):
    l = -1
    cnt = 0
    for i in range(w):
        if l == -1 and line[i] in ['/', '\\']:
            l = i
        elif line[i] in ['/', '\\']:
            cnt += i-l
            l = -1
    return cnt

h, w = map(int, input().split())
lines = [list(input()) for _ in range(h)]
ans = 0
for line in lines:
    ans += solve(line)
print(ans)