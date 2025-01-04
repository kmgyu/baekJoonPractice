a, b = map(int, input().split()) #진법
m = int(input())
num = 0
nums = list(map(int,input().split()))
for i in range(m):
    num += nums[i] * (a**(m-i-1))
ans = []
while num >= b:
    temp = num%b
    ans.append(temp)
    num //= b
ans.append(num)
ans.reverse()

print(*ans)

