
def factorial(n):
    if n == 2:
        return 2
    return n*factorial(n-1)

def power(a,b):
    result = 1
    while b > 0:
        if b % 2 != 0:
            result = (result * a) % mod
        b //= 2
        a = (a * a) % mod

    return result

mod = int(1e9)+7
n, k = map(int, input().split())
nums = list(map(int, input().split()))

no = set()
cnt = 0
length = len(nums)
for i in range(n):
    for j in range(i+1, n):
        if (nums[i]+nums[j]) % k == 0:
            cnt += (2**(length-2))
            no.add(nums[i])
            no.add(nums[j])
sub = power(2, len(no)-2) - 2
print((power(2, length) - cnt - (length + 1) + sub)%mod)



# print(2**n - ((2**(len(no)-2)) * (2**(n-len(no)))))