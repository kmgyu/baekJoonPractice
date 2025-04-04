N, D, K = map(int, input().split())
s = [*map(int, input().split())]
stars = [0] * N
cnt = 0
for day in range(D):
    for star in range(N):
        stars[star] += s[star]
        if stars[star] + s[star] > K and day < D-1:
            stars = [0] * N
            cnt += 1
            break  
    
print(cnt)