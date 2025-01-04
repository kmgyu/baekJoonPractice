import sys
input = sys.stdin.readline

t = int(input())
for l in range(t):
    n = int(input())
    clothes = dict()
    for i in range(n):
        name, category = input().split()
        if category in clothes:
            clothes[category] += 1
        else:
            clothes[category] = 2

    ans = 1
    for i in clothes.values():
        ans *= i
    print(ans-1)
