#CCC '14 J3 - Double Dice
#https://dmoj.ca/problem/ccc14j3

Antonia = 100
David = 100

x = int(input())
for i in range(x):
    games = input()
    if int(games[0])>int(games[2]):
        Antonia = Antonia - int(games[0])
    if int(games[0])<int(games[2]):
        David = David - int(games[2])
print(David)
print(Antonia)
    

