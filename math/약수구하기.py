n, k = map(int, input().split())
prime = []
for i in range(1, int(n/2)):
    if n%i==0:
        prime.append(i)
print(prime)
if n > 2:
    prime.append(n)
if len(prime) < k:
    print(0)
else:
    print(prime[k-1])