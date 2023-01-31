#CCC '16 J2 - Magic Squares
#https://dmoj.ca/problem/ccc16j2

A = input().split()
B = input().split()
C = input().split()
D = input().split()

x = int(A[0]) + int(A[1]) + int(A[2]) + int(A[3])
xx = int(B[0]) + int(B[1]) + int(B[2]) + int(B[3])
xxx = int(C[0]) + int(C[1]) + int(C[2]) + int(C[3])
xxxx = int(D[0]) + int(D[1]) + int(D[2]) + int(D[3])
#
y = int(A[0]) + int(B[0]) + int(C[0]) + int(D[0])
yy = int(A[1]) + int(B[1]) + int(C[1]) + int(D[1])
yyy = int(A[2]) + int(B[2]) + int(C[2]) + int(D[2])
yyyy = int(A[3]) + int(B[3]) + int(C[3]) + int(D[3])

if x == xx == xxx == xxxx == y == yy == yyy == yyyy:
    print("magic")
else :
    print("not magic")
