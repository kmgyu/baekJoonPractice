N, D, K = map(int, input().split())
s = [*map(int, input().split())]
stars = [0] * N
cnt = 0
for day in range(D):
    for star in range(N):
        stars[star] += s[star]
        if stars[star] + s[star] > K:
            stars = [0] * N
            cnt += 1
            break

print(cnt)
# 이게 아니라고...? 에? 예???