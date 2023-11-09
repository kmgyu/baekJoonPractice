a, b = input().split()
answer = 10e9
for i in range(len(b)-len(a)+1):
    cnt = 0
    for j in range(i, len(a)+i):
        if a[j-i] != b[j]: cnt+=1
    answer = min(cnt, answer)
print(answer)