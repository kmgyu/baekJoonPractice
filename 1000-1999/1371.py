import sys

text = sys.stdin.read()
text = text.replace('\n', '').replace(' ', '')
    
cnt = dict()
for char in text:
    if char not in cnt: cnt[char] = 0
    cnt[char] += 1

s = sorted(cnt.items(), key=lambda x:(-x[1], x[0]))
l = len(s)
idx = 0
while idx < l:
    print(s[idx][0], end='')
    if idx == l-1 or s[idx][1] != s[idx+1][1]: break
    idx += 1