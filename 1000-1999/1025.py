N, M = map(int, input().split())
S = [input() for _ in range(N)]

ans = -1

def sqrt_check(num):
    if int(num**0.5)**2 == num or int(num**0.5+1)**2 == num:
        return num
    else: return -1

for n in range(N):
    for m in range(M):
        for r_step in range(-N, N):
            for c_step in range(-M, M):
                sq = ''
                if r_step == c_step == 0: continue

                r_cur = n
                c_cur = m
                while 0 <= r_cur < N and 0 <= c_cur < M:
                    sq += S[r_cur][c_cur]
                    r_cur += r_step
                    c_cur += c_step
                    v = sqrt_check(int(sq))
                    ans = max(ans, v)
print(ans)