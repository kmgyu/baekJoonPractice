s = input()
ans = ""
u = ['C','P','C','U']
for word in s:
    if not u: break
    if word == u[-1]:
        u.pop()
        ans += word
if ans == "UCPC": print("I love UCPC")
else:print("I hate UCPC")