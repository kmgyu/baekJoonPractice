# 11375
# 2188
# 두가지 문제 참고

# 2188
def match(cow):
    for room in rooms[cow]:
        if not matched[room]: # 매칭 안되있으면 바로 이어버리기
            matched[room] = cow
            return True
    # 바로 잇는게 불가능할 경우에 대한 추가적인 탐색? 같은 것
    # 뭐라 말하지 으아악
    for room in rooms[cow]:
        if visited[room]: continue
        visited[room] = True
        if match(matched[room]): # matched를 위쪽 for문으로 넘겨버렸다..
            matched[room] = cow
            return True
    return False

# 11375
def dfs(current):
    for job in graph[current]:
        if visited[job]: continue
        visited[job] = True
        # 연결되지 않았거나, matched[job]노드 재탐사시
        # 다른 경로 존재 시(visited 안겹치면서 다른 경로)
        if not matched[job] or dfs(matched[job]):
            matched[job] = current
            return True
    return False
