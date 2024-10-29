import sys
input=sys.stdin.readline
def solve(x,y,length):
 p=mat[x][y]
 l=length//2
 for i in range(x, x+length):
  for j in range(y, y+length):
   if p != mat[i][j]:
    for w in (0, l):
     for h in (0, l):
      solve(x+w, y+h, l)
    return
 ans[p]+=1
n=int(input())
mat=[list(map(int, input().split())) for _ in range(n)]
ans=[0,0]
solve(0,0,n)
print(*ans, sep="\n")