n = int(input())

if n == 1:
    print(0)
else:
    arr = [list(map(int, input().split())) for _ in range(n)]
    min_x, max_x = arr[0][0], arr[0][0]
    min_y, max_y = arr[0][1], arr[0][1]
    
    for i in range(1, n):
        min_x = min(min_x, arr[i][0])
        max_x = max(max_x, arr[i][0])
        min_y = min(min_y, arr[i][1])
        max_y = max(max_y, arr[i][1])
            
    print((max_x - min_x)*(max_y - min_y))
        


            