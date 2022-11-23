#April Fools' Day Contest 1 P1 - Sample Case
#https://dmoj.ca/problem/afd1p1

x = int(input())

for i in range(x):
    z = input().split()
    if int(z[0]) < 1000000000:
        if int(z[1]) < 1000000000:
            print(int(z[0])+int(z[1]))

#Works 