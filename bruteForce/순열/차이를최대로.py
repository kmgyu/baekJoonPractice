from itertools import permutations
n = int(input())
ans = 0
for i in permutations(list(map(int,input().split()))):
    temp = 0
    for j in range(n-1):
        temp += abs(i[j] - i[j+1])
    ans = max(ans, temp)
print(ans)