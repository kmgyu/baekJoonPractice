from itertools import combinations

N= int(input())
result = []

for i in range(1, 11):
    for j in combinations(range(10), i):
        num = ''.join(map(str, j))[::-1]
        result.append(int(num))

result.sort()
if N >= len(result): print(-1)
else: print(result[N])

# reference
# https://velog.io/@sugyeonghh/%EB%B0%B1%EC%A4%80-1038-%EA%B0%90%EC%86%8C%ED%95%98%EB%8A%94-%EC%88%98Python
#  복잡하게 해결하려다 결국 써버렸다...