a, b = map(int, input().split())

def prime_filter(n):
    prime = [True] * (n + 1)
    prime[0] = prime[1] = False
    for i in range(2, int(n**0.5)+1):
        if prime[i]:
            for j in range(i*i, n + 1, i):
                prime[j] = False
    
    return [i for i in range(n + 1) if prime[i]]

primes = prime_filter(b)

def prime_factor(n):
    factor = []
    num = n
    for p in primes:
        if num < p: break
        while num % p == 0:
            factor.append(p)
            num //= p
    return len(factor)


prime_set = set(primes)

cnt = 0
for num in range(a, b+1):
    if prime_factor(num) in prime_set:
        cnt += 1

print(cnt)