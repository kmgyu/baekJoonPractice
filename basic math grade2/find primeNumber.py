#1929번
import sys
N, M = map(int, sys.stdin.readline().split())

num = set(i for i in range(N, M+1))
j = [True] * int(M**0.5+2)
l = len(j)

try:
    num.remove(1)
except:
    pass

for k in range(2, l+1):
    i = k
    if j == False:
        continue

    while i <= M:
        i += k
        if i <= l:
            j[i-1] = False
        try:
            num.remove(i)
        except:
            pass
print(*sorted(num), sep="\n")

