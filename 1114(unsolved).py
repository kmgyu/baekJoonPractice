def solve():
    l,k,c = map(int, input().split())
    cutpoints = sorted(set(map(int, input().split())))+[l]
    k=len(cutpoints)
    
    # 매개변수 탐색
    def check(tgt):
        # 오른쪽부터 선형 탐색, target보다 클 경우 잘라내면서 이동
        right = l
        cnt = c
        for i in range(k-1, -1, -1):
            if cnt==0: break
            if right-cutpoints[i] > tgt:
                if cutpoints[i+1] - cutpoints[i] > tgt:
                    return -1
                cnt -= 1
                right = cutpoints[i+1]
        
        if cnt: right = cutpoints[0]
        
        if right > tgt: return -1
        else: return right

    start, end = l//(c+1), l
    mid, pnt = 0, 0

    # 이분탐색
    while start < end:
        mid = (start + end) // 2
        pnt = check(mid)
        # print(start, end, mid, pnt)
        if pnt > 0: end = mid
        else: start = mid+1
    # 작은 것부터이므로, 가장 작은 절단 점 출력
    print(start, check(start))
solve()