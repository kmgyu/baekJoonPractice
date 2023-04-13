e, s, m = map(int, input().split())
k = [1,1,1]
cnt = 1
while True:
    if k[0] == e and k[1] == s and k[2]==m:
        break
    k[0] = k[0]%15 +1
    k[1] = k[1]%28 +1
    k[2] = k[2]%19 +1
    cnt += 1
print(cnt)