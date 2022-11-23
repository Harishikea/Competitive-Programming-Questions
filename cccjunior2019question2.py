#CCC Junior, quesiton 2 (2019) - Time to Decompress

x = 0 
count = 0 
i = int(input())

while x < 1:
    count = count + 1
    z = input().split()
    print(z[1]*int(z[0]))

    if count==i:
        x = x + 1