n = int(input())

arr = []

for _ in range(n):
    a, b = input().split()
    arr.append([int(a), b])

#arr = arr.sort(key = lambda x:(x[0]))
arr = sorted(arr, key = lambda x:(x[0]))

for i in range(n):
    for j in range(2):
        print(arr[i][j], end=" ")
    print("")