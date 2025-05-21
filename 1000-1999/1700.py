input = open(0).readline
# page fault optimal algorithm...?
N, K = map(int, input().split())
plug = [*map(int, input().split())]

future = dict() # 미래시

for i in range(K-1, -1, -1):
    if plug[i] in future: future[plug[i]].append(i)
    else: future[plug[i]] = [-1, i]

memory = []
m_set = set() # 중복 무시 빠른 찾기
length = 0 # 메모리 현재 길이
cnt = 0
for i in range(K):
    current = plug[i]
    if length < N:
        # 안쓰고 있고 자리 남아있으면 집어넣음
        if current not in m_set:
            memory.append(current)
            m_set.add(current)
            length += 1
        future[current].pop()
    else:
        # print(m_set, memory)
        # 있으면 생략
        if current in m_set:
            future[current].pop()
            continue
        change = 0
        latest_position = i
        for j in range(N):
            if future[memory[j]][-1] == -1: # 더이상 나오지 않을 때
                latest_position = future[memory[j]][-1]
                change = j
                break
            elif future[memory[j]][-1] > latest_position: # 현재 가장 늦는 것
                latest_position = future[memory[j]][-1]
                change = j
            # print(change, future[memory[j]], i)
        # 메모리 집합 갱신
        m_set.remove(memory[change])
        m_set.add(plug[i])
        # page fault 교체
        memory[change] = plug[i]
        future[memory[change]].pop()
        cnt += 1
    # print(memory)
        
print(cnt)
                
