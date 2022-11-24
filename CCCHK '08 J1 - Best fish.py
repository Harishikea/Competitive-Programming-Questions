#CCCHK '08 J1 - Best fish
#https://dmoj.ca/problem/ccc19j2

n = int(input())
sum1 = 0
sum2 = 0
for i in range (n):
  p = input().split()
  y = int(p[0])*int(p[1])
  if y > sum1:
    sum1 = y
  
u = int(input())
for i in range (u):
  ll = input().split()
  er = int(ll[0])*int(ll[1])
  if er > sum2:
    
    sum2 = er

if sum1 > sum2:
  print("Casper")
elif sum1 < sum2:
  print("Natalie")
elif sum1 == sum2:
  print("Tie")