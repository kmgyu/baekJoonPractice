#대칭확인 -> 소수 확인
n = int(input())

def Prime(x):
    for i in range(2,int(x*(0.5))+1):
        if x % i == 0: return False
    return True
result = 0
for i in range(n,100001):
    if i == 1: continue
    if str(i) == str(i)[::-1]:
        if Prime(i) == True:
            result = i
            break
if result == 0: # 최대값일경우 최대값을 넘는 소수판별을 따로 해줌.
    result = 1003001
print(result)