import sys
input = sys.stdin.readline

n, m = map(int, input().split())
word = [[0]*4 for _ in range(m)]
a = {'A':0,'C':1,'G':2,'T':3}
b = ['A','C','G','T']
for i in range(n):
    dna = input()
    for j in range(m):
        word[j][a[dna[j]]] += 1
ans = 0
for i in range(m):
    r = max(word[i])
    for j in range(4):
        if word[i][j] == r:
            print(b[j], end = '')
            ans += n-r
            break
print()
print(ans)