def solve():
    def find(n):
        if parent[n] == n:
            return n
        parent[n] = find(parent[n])
        return parent[n]
    
    F = int(input())
    nets = [] # edge 저장
    # set 이용할 수도 있을 거 같지만 여기선 인덱스 번호 기억해야 해서 이걸로 함.
    name_idx = dict() # 이름 to 번호 변환.
    name_l = 0 # 이름 수 저장용
    for i in range(F): # 이름을 번호로 변환 및 엣지 추가
        user1, user2 = input().split()
        if user1 not in name_idx:
            name_idx[user1] = name_l
            name_l += 1
        if user2 not in name_idx:
            name_idx[user2] = name_l
            name_l += 1
        nets.append((name_idx[user1], name_idx[user2]))
    parent = list(range(name_l))
    counter = [1] * (name_l) # 각 인덱스별 친구 카운터.
    
    # 네트워크에서 판별.
    # 0을 출력하는 게 아니라 음.. 최초로 나온 매칭 출력하는? 거였다.
    for net in nets:
        con1, con2 = min(net), max(net)
        c1_idx = find(con1)
        c2_idx = find(con2)
        c1_idx, c2_idx = min(c1_idx, c2_idx), max(c1_idx, c2_idx)
        if c1_idx != c2_idx:
            # con1, con2 기준이 아니라 idx 즉 조상 기준으로 연결해줘야 했다...
            counter[c1_idx] += counter[c2_idx]
            parent[c2_idx] = c1_idx
        print(counter[c1_idx])
        
input = open(0).readline
T = int(input())

for _ in range(T):
    solve()
