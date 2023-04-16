#10972
n = int(input())
nums = list(map(int, input().split()))

def next_permutation():
    i = n-1
    while i>0 and nums[i-1] >= nums[i]: i -= 1
    if i <= 0:
        print(-1)
        return
    
    j = n-1
    while nums[j] <= nums[i-1]: j -= 1
    
    nums[i-1], nums[j] = nums[j], nums[i-1]
    j = n-1
    while i < j:
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1
    print(*nums)
    
#함수의 원리
#맨 뒤부터 내림차순으로 부분을 찾는다. (내림차순부터 오름차순 정렬이라)
#그 둘을 기억하고, 앞에 있는 녀석보다 큰녀석 더 있는지 찾는다.
#찾았을 때, 이놈이 i보다 크면 j를 기억하고 i부터 뒤집는다.
#뒤집으면 내림차순된걸 오른차순으로 뒤집어줘야 한다!
#그래야 가장 가까운 값이 되기때문!
#https://blogshine.tistory.com/122 참고
next_permutation()