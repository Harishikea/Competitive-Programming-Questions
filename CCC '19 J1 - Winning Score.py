#CCC '19 J1 - Winning Score
a = int(input())
aa = int(input())
aaa = int(input())

A = (a * 3) + (aa * 2) + (aaa * 1)

t = int(input())
tt = int(input())
ttt = int(input())

T = (t * 3) + (tt * 2) + (ttt * 1)

if A > T:
  print("A")
if A < T:
  print("B")
if A == T:
  print("T")