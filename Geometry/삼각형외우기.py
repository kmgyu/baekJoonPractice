r = set()
s = 0
a = ['Equilateral', 'Isosceles', 'Scalene']
for i in range(3):
    t = int(input())
    s+=t
    r.add(t)
if s != 180:
    print('Error')
else:
    print(a[len(r)-1])