#An Animal Contest 3 P1 - Monkey Shopping
#https://dmoj.ca/problem/aac3p1

x = input().split()

def solve():
    if int(x[0]) < int(x[1]) and int(x[2]) < int(x[3]):
        print("Go to the department store")
    elif int(x[0]) < int(x[1]):
        print("Go to the grocery store")
    elif int(x[2]) < int(x[3]):
        print("Go to the pharmacy")
    elif int(x[0]) >= int(x[1]) and int(x[2]) >= int(x[3]):
        print("Stay home")
solve()


