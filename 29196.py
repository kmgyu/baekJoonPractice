from math import gcd

s = input()
n = float(s)
k = int(s[2:])
p = 10**len(s[2:])
s = gcd(k, p)
k //= s
p //= s
print(k,p)
if abs(n-k/p) <= 1e-6:
    print("YES")
    print(k, p)
else:
    print("NO")