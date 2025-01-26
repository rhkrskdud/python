arr = [[0 for _ in range(100)] for _ in range(100)]

n = int(input())

for i in range(n):
    x,y = map(int, input().split())
    for i in range(10):
        for j in range(10):
            arr[x+i][y+j] = 1
            
count = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] == 1:
            count += 1
            
print(count)
            