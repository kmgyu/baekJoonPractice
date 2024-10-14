from itertools import permutations
permutations


def solve(d, k):
    for i in range(k//2, k):
        rev_fibo = [k, i]
        for j in range(d-2):
            rev_fibo.append(rev_fibo[-2] - rev_fibo[-1])
            if rev_fibo[-1] < 1 or rev_fibo[-2] < rev_fibo[-1]: break
        else:
            return rev_fibo[-2:]

d, k = map(int, input().split())

print(*solve(d, k)[::-1], sep='\n')