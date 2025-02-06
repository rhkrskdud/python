n =int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

arr.sort(key = lambda x:(x[1],x[0]))

for i in range(n):
    for j in range(2):
        print(arr[i][j], end=" ")
    print("")