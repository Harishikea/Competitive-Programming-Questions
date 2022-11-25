#https://dmoj.ca/problem/gfssoc16j2
#GFSSOC '17 J2 - Admission Average

y = 0
for i in range(6):
    x = int(input())
    y = x + y
z = int(input())
h = int(input())
rr = y / 6 + z

if rr >= h:
    print('yes')
elif rr < h:
    print('no')