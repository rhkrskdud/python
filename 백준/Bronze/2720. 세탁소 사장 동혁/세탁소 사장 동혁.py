#아 센트네 ..시ㅂr
n = int(input())

coins = [25, 10, 5, 1]
arr = [[0 for _ in range(4)] for _ in range(n)]

for i in range(n):
    a = int(input())
    for j in range(len(coins)):
        arr[i][j] = a // coins[j]
        a = a - (coins[j]*(a//coins[j]))

for i in range(n):
    for j in range(len(coins)):
        print(arr[i][j],end=" ")
    print("")
    