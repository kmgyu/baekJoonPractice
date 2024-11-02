def cut(length):
    global longest
    if longest > length:
        return 10001, 0

    cur_len = 0
    count = 0
    for piece_len in pieces:
        cur_len += piece_len
        if cur_len > length:
            cur_len = piece_len
            count += 1

    return count, cur_len if count == c else pieces[-1]

l,k,c = map(int, input().split())
cutpoints = [0]+sorted(set(map(int, input().split())))+[l]
pieces = [cutpoints[i+1] - cutpoints[i] for i in range(1, k+1)]
longest = max(pieces)

start, end = 0, l
ans_piece, ans_len = 0,0

while start <= end:
    mid = (start + end) // 2
    cnt, pt = cut(mid)
    if cnt <= c:
        ans_pt = pt
        ans_len = mid
        end = mid-1
    else:
        start = mid+1
print(ans_len, ans_pt)