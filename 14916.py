m = int(input())
if m == 1 or m == 3: print(-1)
else:
    ans = 0
    ans += m//5
    m %= 5
    if m%2 == 1: ans += 2
    print(ans+m//2)
