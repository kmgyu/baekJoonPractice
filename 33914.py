from collections import defaultdict
x, y = map(int, input().split())

fact = defaultdict(int)
fact[0] = 1
fact[1] = 1
fact[2] = 2
def factorial(end):
    if end in fact: return fact[end]
    
    for i in range(3, end+1):
        if i in fact: continue
        fact[i] = fact[i-1]*i
        # fact[i] %= mod
    return fact[end]

mod = 1_000_000_007

if x%2: print(0)
elif x == 0: print(1)
else:
    c1 = x//2 # case 1
    c2 = (y-c1)//3 # case 2
    if c2 < 0: print(0); exit()
    c1n = (3**c1) % mod
    a1 = (factorial(c1+c2) // (factorial(c2)*factorial(c1))) % mod

    # print(fact[500] * fact[1500])
    # print(fact[2000], a1)
    print(c1n * a1 % mod)
    