#4673번

nums = list(range(1, 10001))
non_self = {2}
for _ in range(1, 10001):
    temp = list(str(_))
    sum_ = _
    for i in range(len(temp)):
        sum_ += int(temp[i])
    non_self.add(sum_)
nums = list((set(nums) - non_self))
nums.sort()
print(*nums)


""" 다른 사람꺼 돚거함. 함수 정의는 배워야 할듯.
def d(n):
    n = n + sum(map(int,str(n)))
    return n

notSelfNumber = []
for i in range(1,10001):
    notSelfNumber.append(d(i))
    
for i in range(1,10001):
    if i not in notSelfNumber:
        print(i)
"""