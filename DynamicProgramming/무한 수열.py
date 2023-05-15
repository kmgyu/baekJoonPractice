import sys
sys.setrecursionlimit(10**6)
A = {0:1}
n, p, q, x, y = map(int, input().split())
def find(n, p, q, x, y):
    if n in A:
        return A[n]
    else:
        a = 0
        b = 0
        if n//p-x not in A:
            if n//p-x <= 0:
                A[n//p-x] = 1
            else:
                A[n//p-x] = find(n//p-x, p, q, x, y)
        
        if n//q-y not in A:
            if n//q-y <= 0:
                A[n//q-y] = 1
            else:
                A[n//q-y] = find(n//q-y, p, q, x, y)
        a = A[n//p-x]
        b = A[n//q-y]
        return a+b
print(find(n, p, q, x, y))