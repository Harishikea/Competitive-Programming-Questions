#CCC '20 J1 - Dog Treats
#https://dmoj.ca/problem/ccc20j1

S = int(input())
M = int(input())
L = int(input())

x = 1 * S + 2 * M + 3 * L

if x >= 10: 
    print("happy")
if x < 10:
    print("sad")