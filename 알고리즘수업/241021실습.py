def find_max(arr):
    m = arr[0]
    for i in range(1, len(arr)):
        if m < arr[i]: m = arr[i]
    return m


def gcd(a, b):
    if a < b: a,b = b,a
    while b!=0:
        r = a%b
        a,b = b,r
    return a
# print(gcd(9, 5))

def sequential_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key : return i
    return -1
# print(sequential_search([1,2,3,4,5], 3))
# print(sequential_search([1,2,3,4,5], 6))

def binary_digits(n):
    cnt = 1
    while n>1:
        cnt = cnt+1
        n//=2
    return cnt


def binary_digits_1(n):
    # need to reverse in this
    binary = ''
    while n>1:
        binary += str(n%2)
        n//=2
    binary += str(n)
    return binary[::-1]

def binary_digits_2(n):
    # don't need to reverse in here~
    binary = ''
    while n>1:
        binary = str(n%2)+binary
        n//=2
    binary = str(n)+binary
    return binary

def binary_digits_3(n): # more short!!!!!
    b=''
    while n:
        if n&1:b='1'+b
        else:b='0'+b
        n>>=1
    return b
# print(binary_digits_3(10))

def factorial_cnt(n): return n+1

def hanoi_count(n):
    # 재귀에 따라 문제의 개수가 늘어나면 그만큼 지수승으로 늘어난다.
    # 하나씩 줄어든다고 하면 팩토리얼의 경우 linear, 선형적으로 줄어든다.
    # 하노이는 작은문제 두개씩 분할. 어떤건 세개씩이라 3^n이 된다....!!!!
    # 이에 따른 성능분석이 달라질 수 있다.....
    if n==1: return 1
    else: return 2*hanoi_count(n-1)+1

def fast_hanoi(n): return 2**n-1

# for i in range(1,5):
#     print(i, end=' ')
#     print(hanoi_count(i))

# print(fast_hanoi(20))

def selection_sort(arr):
    # 선택정렬의 핵심은 find Max(or Min)
    n = len(arr)
    for i in range(n-1):
        least = i
        # find max
        for j in range(i+1, n):
            if arr[j] < arr[least]: least = j
        arr[least], arr[i] = arr[i], arr[least]
        # print step
        print(f"step {i} : {arr}")
    return arr

# print(selection_sort([5,3,8,4,9,1,6,2,7]))

def string_matching(t, p):
    # O(n*m). 이 루프에 대한 설명 필요
    # 최악의 경우 outer n, inner m번 도는데 이중루프 구조라 n*m번 돈다. T(n) = n*m이 되서 O(n*m)이 된다.
    n = len(t)
    m = len(p)
    for i in range(n-m+1):
        j = 0
        while j<m and p[j] == t[i+j]:
            j += 1
        if j==m:
            return 1
    return -1

# 리포트 거리 구하기 해밍 거리 등...
# 최근접 점의 쌍의 거리 문제 -> 복잡도 분석? 이중루프. n번 두번되서 n^2. 진짜 자세하게 하려면 시그마 넣고 T(n) 쓰고... 하는게 맞는데...
# 루프의 개수를 세는 게 n과 관련이 있는지 중요. range(i, n+1) 번처럼.
def closest_pair(p):
    n = len(p)
    mindist = float('inf')
    for i in range(n-1):
        for j in range(i+1, n):
            dist = p[i]**2+p[j]**2 #원래는 euclidean distance 구해야 한다!!!
            if dist < mindist:
                mindist = dist
    return mindist**0.5 #마찬가지다! 여기 그냥 mindist 들어와야 한다!!

def dfs(graph, start, visited):
    # dfs bfs 안써놔도 어떤게 dfs인지 알 수 있어야 한다.
    if start not in visited:
        visited.append(start)
        print(start, end=' ')
        nbr = graph[start] - visited
        for v in nbr:
            dfs(graph, v, visited)

def bfs(graph, start):
    import queue
    visited = {start}
    q = queue.Queue()
    q.put(start)
    while not q.empty():
        v = q.get()
        print(v, end=' ')
        nbr = graph[v] - visited
        for u in nbr:
            visited.add(u)
            q.put(u)
