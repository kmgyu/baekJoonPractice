def check(idx):
    sum_ = 0
    for i in range(idx, -1, -1):
        sum_ += result[i]
        if sum_ == 0 and a[i][idx] != 0:
            return False
        elif sum_ > 0 and a[i][idx] <= 0:
            return False
        elif sum_ < 0 and a[i][idx] >= 0:
            return False
    return True

def solve(idx):
    if idx == n:
        return True
    if a[idx][idx] == 0:
        result[idx] = 0
        return solve(idx+1)
    for i in range(1, 11):
        result[idx] = a[idx][idx]*i
        if check(idx) and solve(idx+1):
            return True
    return False

n = int(input())
ai = list(input())
a = [[0]*n for i in range(n)]
for i in range(n):
    for j in range(i, n):
        tmp = ai.pop(0)
        if tmp == '+': a[i][j] = 1
        elif tmp == '-': a[i][j] = -1

result = [0] * n
solve(0)
print(' '.join(map(str, result)))