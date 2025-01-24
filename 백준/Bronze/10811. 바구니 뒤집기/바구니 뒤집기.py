n, m = map(int, input().split())

arr=[i+1 for i in range(n)]

for _ in range(m):
    i, j = map(int, input().split())
    while i<j:
        arr[i-1], arr[j-1] = arr[j-1], arr[i-1]
        i = i+1
        j= j-1
        
print(*arr)