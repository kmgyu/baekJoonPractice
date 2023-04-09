n = int(input())
ans = 1
for i in range(2, n+1):
    ans *= i
ans = str(ans)
count = 0
for i in range(len(ans)-1, 0, -1):
    if ans[i] == "0":
        count += 1
    else:
        break
print(count)