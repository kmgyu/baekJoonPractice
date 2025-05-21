#a^b 10827번
a, b = input().split()
decP = len(a) - a.index(".") - 1 #decimal point :: 10e-decP
a = a.replace('.','')
ans = str(int(a)**int(b))
idx = len(ans) - (decP*int(b)+1)
if idx < 0:
    ans = "0." + "0"*(-idx-1) + ans
else:
    ans = ans[:idx+1] + "."+ ans[idx+1:]
print(ans)