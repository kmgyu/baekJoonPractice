A = {0:1}
n, p, q = map(int, input().split())

def find(n, p, q):
    if n in A:
        return A[n]
    else:
        A[n//p] = find(n//p, p, q)
        A[n//q] = find(n//q, p, q)
        return A[n//p] + A[n//q]

print(find(n, p, q))