# https://jhhope1.tistory.com/24

import math
n, p, v = map(int, input().split())
dp = list()
def solve_k(n, p, v, k):
    fact = math.pow(n,1.0/k)
    # since fact was rounded down above, we now increase
    # some factors by 1 to have them multiply to at least n
    incr = 0
    while pow(fact + 1, incr) * pow(fact, k - incr) < n:
        incr += 1
    # the answer is /sum(factors)*p + k * v
    return (k * fact + incr) * p + k * v

def solve(n, p, v):
    if n == 1:
        return 0
    result = solve_k(n, p, v, 1)
    for k in range(2, n):
        r = solve_k(n,p,v,k)
        result = min(result, r)
    return result

print(int(solve(n,p,v)))
