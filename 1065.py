#1065번
#수열 판별 먼저
def seq_dcm(num):
    discriminant = True
    n = set()
    for i in range(1, len(num)):
        temp = int(num[i]) - int(num[i-1])
        n.add(temp)
    if len(n) > 1:
        discriminant = False
    return discriminant

X = int(input())
count = 0
for i in range(1, X+1):
    if seq_dcm(str(i)):
        count += 1
print(count)