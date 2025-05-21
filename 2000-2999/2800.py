def dfs(pairs, i):
    if i == pair_l:
        if not pairs: return []
        ans = ''
        for j in range(L):
            if j in pairs: continue
            ans += s[j]
        return [ans]
    pairs_1 = set([*pairs, *idx_pair[i]])
    return dfs(pairs_1, i+1) + dfs(pairs, i+1)


s = input().strip()
L = len(s)

stack = []
idx_pair = []

for i in range(L):
    if s[i] == '(': stack.append(i)
    elif s[i] == ')':
        idx_pair.append((stack.pop(), i))

pair_l = len(idx_pair)
# print(pair_l, idx_pair)
answer = set(dfs(set(), 0)) # 중복 가능. ex : ((0/(0)))
print(*sorted(answer), sep="\n")