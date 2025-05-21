def lcs(a, b):
    m, n = len(a), len(b)
    prev = [0] * (n + 1)
    max_length = 0

    for i in range(1, m + 1):
        curr = [0] * (n + 1)
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                curr[j] = prev[j - 1] + 1
                if curr[j] > max_length: max_length = curr[j]
            else: curr[j] = 0
        prev = curr
    return max_length

input = open(0).readline
a = input().strip()
b = input().strip()

print(lcs(a, b))

# 투포인터를 이용해 더 빠르고 쉽게 풀 수 있다.
# fuuuck