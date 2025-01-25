from collections import deque
import sys

input = sys.stdin.readline


def turn(direc, D):
    if D == "D":
        direc = (direc + 1) % 4
    else:
        direc = (direc - 1) % 4
    return direc


def move(direc):
    direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    return direction[direc]


# 초기 방향
direc = 0  # 이게 동쪽

# NxN크기의 보드판 만듦
N = int(input().rstrip())
board = [[0 for _ in range(N)] for _ in range(N)]

# 사과 위치 설정
K = int(input())
for _ in range(K):
    row, col = map(int, input().split())
    board[row - 1][col - 1] = 1

# 뱀의 이동경로
L = int(input().rstrip())

# 뱀의 처음 위치
c_x = 0
c_y = 0

count = 0

tailremover = deque()
tailremover.append((0,0))

#TLqkf wlsWK whwrkxek....
sibal = deque()

for _ in range(L):
    X, D = input().split()
    X = int(X)
    sibal.append((X,D))

while True:
    count += 1
    # 뱀이 움직인다
    dx, dy = move(direc)
    c_x += dx
    c_y += dy
    # 움직인 위치가 벽이면 끝
    if c_x < 0 or c_y < 0 or c_x >= N or c_y >= N:
        break
    # 움직인 위치가 뱀이면 끝
    if board[c_x][c_y] == "*":
        break
    # 움직인 위치에 사과가 있으면 꼬리 그대로.
    if board[c_x][c_y] == 1:
        board[c_x][c_y] = "*"
        tailremover.append((c_x,c_y))
    # 사과가 아니면 꼬리삭제 후 그 자리를 다시 저장
    else:
        board[c_x][c_y] = "*"
        x_, y_ =tailremover.popleft()
        board[x_][y_] = 0
        tailremover.append((c_x,c_y))

    if sibal and count == sibal[0][0]:
        X_, D_ = sibal.popleft()
        direc = turn(direc, D_)


print(count)