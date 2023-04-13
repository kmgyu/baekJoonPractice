n = int(input())
k = len(str(n))
ans = 0
for i in range(k):
    if n < 9*(10**i) :
        break
    n -= 9*(10**i)
    ans += 9*(10**i)*(i+1)
ans += k*n
print(ans)
# 6 * 2 + 9
#21 * 3 + 90 * 2 + 9
#자릿수 - 1 나누고 이거 기준으로하면됨.
#9씩 빼주기
