import sys
N = int(sys.stdin.readline())
num = [int(sys.stdin.readline()) for i in range(N)]
count = [0] * (max(num)+1)

for i in num:
    count[i] += 1

for i in range(1, len(count)):
    count[i] += count[i-1]

result = [0] * len(num)
for i in num:
    idx = count[i]
    result[idx-1] = i
    count[i] -= 1
print(*result, sep="\n")

# 딕셔너리로 구현
# import sys
# N = int(sys.stdin.readline())
# count = dict()
# for i in range(N):
#     a = int(sys.stdin.readline())
#     try:
#         count[a] += 1
#     except:
#         count[a] = 1
#
# for i in sorted(count.keys()):
#     for j in range(count[i]):
#         print(i)