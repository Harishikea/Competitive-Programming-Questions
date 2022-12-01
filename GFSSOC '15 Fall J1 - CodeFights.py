#GFSSOC '15 Fall J1 - CodeFights
#https://dmoj.ca/problem/gfssoc2j1


A = int(input())
N = int(input())

for i in range (N):
    K= int(input())
    S = abs(A - K)
    if S <=100:
        print('fite me! >:3')
    else:
        print("go away! 3:<")