n, k = map(int, input().split())
num = list(map(int, input().split()))
minus = [0] * 100 #키차이 카운터
for i in range(1, n):
    minus[abs(num[i]-num[i-1])] += 1
ans = 0
temp = sum(minus)
for i in range(100):
    temp -= minus[i]
    ans = i
    if temp > 0 and temp + 1 <= k:
        break
    elif temp == 0:
        break
print(ans)
#틀렸쒀!