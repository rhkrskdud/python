n, m = map(int, input().split())
board = [input().strip() for _ in range(n)]

min_count = 10000

for i in range(n - 7):
    for j in range(m - 7):
        w_start = 0
        b_start = 0

        for k in range(8):
            for l in range(8):
                if (k + l) % 2 == 0:
                    if board[i + k][j + l] != "W":
                        w_start += 1
                    if board[i + k][j + l] != "B":
                        b_start += 1
                else:
                    if board[i + k][j + l] != "B":
                        w_start += 1
                    if board[i + k][j + l] != "W":
                        b_start += 1

        min_count = min(min_count, w_start, b_start)

print(min_count)
