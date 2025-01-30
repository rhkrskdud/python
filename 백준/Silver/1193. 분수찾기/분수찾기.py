#네 저는 병신입니다
n = int(input())

#몇번째 대각선인지
count1 = 1

result = 0
#(n*(n+1))/2 --> n까지의 합
#count값 까지의 합 --> count번째 대각선
#count값을 늘려가면서 찾음..
while (count1*(count1+1))//2 <n:
    count1 += 1
    
#몇번째 자리인지..
#count2에 그 전 대각선 원소까지의 합을 빼면 자릿수가 나옴
count2 = n - ((count1-1)*(count1))//2

#대각선이 어느 방향인지
#짝수면
if count1 % 2 == 0:
    result =f"{count2}/{count1-count2+1}"
else:
    result = f"{count1-count2+1}/{count2}"
    

print(result)
        
    
    
    
        