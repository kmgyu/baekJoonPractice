n, k = map(int, input().split())
people = list(map(int, input().split()))
people.append(people[n-1])
result = float('inf')

height = [abs(people[0] - people[1])]
for i in range(1, n):
    l = abs(people[i] - people[i-1])
    r = abs(people[i] - people[i+1])
    height.append(max(l, r))

start = 0
end = max(height)

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for i in range(n):
        cnt += (height[i] > mid)
    if cnt <= k:
        result = min(result, mid)
        end = mid - 1
    else:
        start = mid + 1
# search(0, result)
print(result)