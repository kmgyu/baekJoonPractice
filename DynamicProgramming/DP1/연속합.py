#1912
n = int(input())
nums = list(map(int, input().split()))
dp = 0
ans = -10e9
for num in nums:
    dp = max(num+dp, num)
    ans = max(ans, dp)
print(ans)
#dp를 리스트로 만들수도 있지만 굳이... 안할수도있었다...흑흑흑
#길이 구하고 그거의 합구하는거임! 최고합!
