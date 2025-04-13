day = [0,31,28,31,30,31,30,31,31,30,31,30,31]
x,y=map(int,input().split())
ans = 0
for i in range(x):ans += day[i]
ans += y-1
d = ['MON','TUE','WED','THU','FRI','SAT','SUN']
print(d[ans%7])