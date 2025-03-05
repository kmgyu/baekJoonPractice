from sys import stdin
print = stdin.readline

def recur(a, b, c):
    
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        return recur(20, 20, 20)
    elif boo[a][b][c]!=0:
        return boo[a][b][c]
    elif a < b and b < c:
        boo[a][b][c] = recur(a, b, c-1) + recur(a,b-1,c-1) -recur(a,b-1,c)
    else:
        boo[a][b][c] = recur(a-1, b, c) + recur(a-1, b-1, c) + recur(a-1, b, c-1)-recur(a-1, b-1, c-1)
    return boo[a][b][c]

while True:
    n,p,c = map(int,input().split())
    boo = [[[0]*21 for _ in range(21)] for _ in range(21)] #같은 주소복사 주의...
    if n == -1 and p == -1 and c == -1:
        break
    print(f"w({n}, {p}, {c}) = {recur(n,p,c)}")
