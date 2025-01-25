arr = [list(map(int, input().split())) for _ in range(9)]

max=0
row=0
col=0

for i in range(9):
    for j in range(9):
        if arr[i][j]>=max:
            max = arr[i][j]
            row = i +1
            col = j +1

print(max)
print(row, col)