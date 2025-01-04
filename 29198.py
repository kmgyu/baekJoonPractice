n, m, k = map(int, input().split())
strings = [sorted(input()) for _ in range(n)]
strings.sort()
s = []
for i in range(k):
    s += strings[i]

print(*sorted(s),sep='')