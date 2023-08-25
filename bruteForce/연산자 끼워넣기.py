from math import inf

def solve(idx, add, sub, mul, div, num):
    global m, M
    if idx == n:
        m = min(num, m)
        M = max(num, M)
        return
    
    if add:
        solve(idx+1, add-1, sub, mul, div, num + A[idx])
    if sub:
        solve(idx+1, add, sub-1, mul, div, num - A[idx])
    if mul:
        solve(idx+1, add, sub, mul-1, div, num * A[idx])
    if div:
        if num*A[idx] < 0:
            solve(idx+1, add, sub, mul, div-1, (abs(num) // abs(A[idx])*-1))
        else:
            solve(idx+1, add, sub, mul, div-1, num // A[idx])

n = int(input())
A = list(map(int, input().split()))
oper = list(map(int, input().split())) # + - * //
m = inf
M = inf * -1
solve(1, oper[0], oper[1], oper[2], oper[3], A[0])
print(M, m, sep="\n")