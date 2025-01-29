from collections import deque
N, B = map(int, input().split())

arr = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
       'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
       'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
       'U', 'V', 'W', 'X', 'Y', 'Z']

#10진법의 수를 n 진법으로 바꾸는 법
#10 진법의 수를 n으로 나눈 나머지를 구해서 변환
aaa = deque()
while(True):
    if N == 0:
        break
    a = N % B
    b = N // B
    N = b
    aaa.appendleft(arr[a])
    
print("".join(aaa))
    
    