import bisect

def query(start, end, level):
    cnt = 0
    for i in range(level, 6):
        if not logs[i]: continue
        start_idx = bisect.bisect_left(logs[i], start)
        end_idx = bisect.bisect_right(logs[i], end)
        cnt += end_idx - start_idx
    return cnt

input = open(0).readline

N, Q = map(int, input().split())

# 레벨 별로 분리
logs = [[] for _ in range(6)]
for _ in range(N):
    time_str, level = input().split("#")
    logs[int(level)-1].append(time_str)

for i in range(6): logs[i].sort()

results = []
for _ in range(Q):
    start_time, end_time, level = input().split("#")
    results.append(query(start_time, end_time, int(level)-1))

print("\n".join(map(str, results)))