import sys
input = sys.stdin.readline

N = int(input().strip())
nums = [input().strip() for _ in range(N)]
numz = [list(num) for num in nums]

def founder(nums, N):
    exceptor = set()
    for i in range(N):
        exceptor.add(nums[i][0])

    cnt = []
    while True:
        tmp = []
        for i in range(N):
            if nums[i]: tmp.append(nums[i].pop())
        if not tmp: break
        cnt.append(tmp)

    # 역순으로 만든 뒤 기수가 가치가 됨.
    strval = dict()
    for i in range(len(cnt)):
        for char in cnt[i]:
            if char in strval: strval[char] += 10**i
            else: strval[char] = 10**i

    strval2 = list(zip(strval.keys(), strval.values()))
    strval2.sort(key=lambda x: x[1])

    choice = set(i for i in range(9, 9-len(strval2), -1))

    for i in range(len(strval2)):
        if strval2[i][0] in exceptor:
            strval[strval2[i][0]] = min(choice-set([0]))
        else:
            strval[strval2[i][0]] = min(choice)
        choice.remove(strval[strval2[i][0]])
    return strval

def operator(strval, nums):
    res = 0
    for num in nums:
        for i in range(len(num)):
            res += strval[num[i]]*(10**(len(num)-i-1))
    return res


strval = founder(numz, N)
print(operator(strval, nums))
