#https://dmoj.ca/problem/acc7p1

n = int(input())

for i in range(n):
    curr = int(input())
    if curr == 2:
        print(2)
    else:
        print(curr-1)