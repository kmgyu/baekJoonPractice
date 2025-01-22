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
        if (bit & val) == val:
            return False
    return True

# check with front
def bits_check(bit, fbit, width):
    for i in range(width):
        if (1 << i) & fbit:
            if i > 0 and ((1 << (i-1)) & bit):
                return False # 왼쪽 뒤에 앉음
            if (1 << (i+1)) & bit:
                return False # 오른쪽 뒤에 앉음
    return True

def solve():
    N, M = map(int, input().split())
    desk = ['']+[input().strip() for _ in range(N)]
    ans = 0
    dp = [[0 for _ in range(1<<M)] for _ in range(N+1)]
    
    bits = []
    for bit in range(1<<M):
        if adj_check(bit, M):
            cnt = bin(bit).count('1')
            bits.append((bit, cnt))
    
    for i in range(1,N+1):
        for bit, cnt in bits:
            if not seat_check(desk[i], bit, M): continue
            for fbit, _ in bits:
                if bits_check(bit, fbit, M):
                    dp[i][bit] = max(dp[i][bit], dp[i-1][fbit] + cnt)
                    ans = max(ans, dp[i][bit])
    print(ans)


input = open(0).readline
T = int(input())

for _ in range(T):
    solve()

