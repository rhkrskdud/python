N, B = input().split()
B = int(B)

#진법 변환 방법(모르겠어서 찾아봄..)
#모든 n진법은 자리 수에 따라 제곱 수가 올라간다
# 1의 자리 수: n^0
# 10의 자리 수: n^1
# 100의 자리 수: n^2
#따라서 진법 변환 계산을 할 때는 맨 오른쪽 자리(1의 자리)부터 거꾸로 각 자리의 수와 
#n진법의 자릿수를 곱하고 그 값을 전체에 더한 것으로 구할 수 있다.

arr = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
       'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
       'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
       'U', 'V', 'W', 'X', 'Y', 'Z']
#arr = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

result = 0
for i in range(len(N)):
    result += arr.index(N[i]) * (B**(len(N)-i-1))
    
print(result)
    