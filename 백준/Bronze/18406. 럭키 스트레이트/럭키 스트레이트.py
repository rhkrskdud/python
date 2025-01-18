# n자릿수 기준 반으로 나눠서 왼쪽부분합 == 오른쪽부분합

import sys
from collections import deque

dq = deque()  # 덱생성
n = sys.stdin.readline().rstrip()

for i in n:
    dq.append(i)

left = 0
right = 0

while len(dq) != 0:
    left += int(dq.popleft())
    right += int(dq.pop())


if left == right:
    print("LUCKY")
else:
    print("READY")
