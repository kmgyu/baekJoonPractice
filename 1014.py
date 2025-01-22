# https://nerogarret.tistory.com/33
# https://eine.tistory.com/entry/%EB%B0%B1%EC%A4%80-1014%EB%B2%88-%EB%AC%B8%EC%A0%9C-%EC%BB%A8%EB%8B%9D-%ED%92%80%EC%9D%B4

def seat_check(seats, bit, width):
    for i in range(width):
        if seats[i] == 'x' and bit & (1 << i): return False
    return True

# adjacency check (rows)
def adj_check(bit, width):
    for i in range(width-1):
        val = 3 << i
        if (bit & val) == val: return False
    return True

# check with front
def bits_check(bit, fbit, width):
    for i in range(width):
        if (1 << i) & fbit:
            if i > 0 and ((1 << (i-1)) & bit): return False # 왼쪽 뒤에 앉음
            if (i << (i+1)) & bit: return False # 오른쪽 뒤에 앉음
    return True

def solve(N, M, desk):
    ans = 0
    dp = [[0 for _ in range(2**M)] for _ in range(N+1)]
    
    bits = []
    for bit in range(2**M):
        if adj_check(bit, M):
            cnt = 0
            for i in range(M):
                if (1<<i) & bit: cnt += 1
            bits.append((bit, cnt))
    
    for i in range(N):
        for bit in bits:
            if not seat_check(desk[i], bit[0], M): continue
            for fbit in bits:
                if bits_check(bit[0], fbit[0], M):
                    dp[i][bit[0]] = max(dp[i][bit[0]], dp[i-1][fbit[0]] + bit[1])
                    ans = max(ans, dp[i][bit[0]])
    print(ans)


input = open(0).readline
T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    desk = [input().strip() for _ in range(N)]
    solve(N, M, desk)

