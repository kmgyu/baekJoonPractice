n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
visited = [False] * n
temp = []

def dfs():
    if len(temp) == m:
        print(*temp)
        return
    remember_me = 0
    for i in range(n):
        if not visited[i] and remember_me != nums[i]:
            visited[i] = True
            temp.append(nums[i])
            remember_me = nums[i]
            dfs()
            visited[i] = False
            temp.pop()

dfs()

# 기존 n과 m 문제를 푼 방식에서 조금 다양한 장치를 더 추가해야 된다.

# remember_me 변수로 중복된 수열을 출력하는 것을 방지하고,

# visited로 방문해야 될 숫자를 구별한다.