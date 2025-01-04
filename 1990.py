def prime(n):
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

a, b = map(int, input().split())
nums = []
for i in [5, 7, 11]:
    if a <= i <= b: nums.append(i)

for num in range(10, int(1e5)+1):
    nums.append(int(str(num)+str(num)[::-1][1:]))

for i in nums:
    if i < a: continue
    if i > b: break
    if prime(i):
        print(i)

print(-1)