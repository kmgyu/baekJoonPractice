d = {str(i): i for i in range(10)}
d = dict(**d, **{chr(i+55): i for i in range(10, 36)})
r_d = {k:v for k, v in enumerate(d)}


N=int(input())

def priority_change(nums):
    prior = {k : [] for k in d.keys()}
    # 우선순위 계산을 위해 각 수 별로 계산.
    # Z로 바꿀 경우, 값이 어떻게 되는지 집계하고 우선순위를 정한다.
    # 더 확실한 방법.
    
    for num in nums:
        l = len(num)
        for i in range(l): # i : num에서 자릿수
            if num[i] == 'Z': continue
            # zero fill
            idx = len(prior[num[i]]) # idx : 우선순위 정하는 거에서 인덱스 길이
            # 주의 : l 기준으로 채워야 됨.
            if idx < l: # 채울 자릿수 부족함
                while idx < l:
                    prior[num[i]].append(0)
                    idx+=1
            prior[num[i]][l-i-1] += 35-d[num[i]] # Z로 바꾼다면 얼마나 커지는지 시뮬레이션 (증가량 기준으로 해야 한다.)
    
    
    for key in prior:
        prior[key] = summation(prior[key], []) # 자릿수만 계산하기
        s = 0
        p_k_l = len(prior[key])
        for i in range(p_k_l): # 아니 parse 안돌려서 안뒤집혀있네 그냥 죽여라
            s += prior[key][i] * (36**(i)) # 귀찮은데 그래도 36진수 해주자... 10진수하면 또 틀릴듯.
        prior[key] = s
    
    
    prior = sorted(prior.items(), key=lambda x: -x[1]) # 우선순위는 큰 것부터, 수는 작은 것 부터
    
    
    for e in prior[:K]:
        d[e[0]] = 35


def summation(num1, num2):
    result = []
    l1, l2 = len(num1), len(num2)
    if l1 < l2:
        num1, num2 = num2, num1
        l1, l2 = l2, l1
    
    up = 0 # 자리올림
    idx = 0
    while idx < l2:
        current = up + num1[idx] + num2[idx]
        up = current // 36
        result.append(current % 36)
        idx += 1
    
    while idx < l1:
        current = up + num1[idx]
        up = current // 36
        result.append(current % 36)
        idx += 1
    
    if up: result.append(up)
    return result

def parse(s):
    num = []
    for c in s[::-1]:
        num.append(d[c])
    return num

def reverse(l):
    result = ''
    for e in l:
        result = r_d[e] + result
    return result

nums = []
for _ in range(N):
    s = input()
    nums.append(s)

K = int(input())

priority_change(nums)

answer = []
for i in range(N):
    answer = summation(parse(nums[i]), answer)

print(reverse(answer))

