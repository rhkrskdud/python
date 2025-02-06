n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

arr.sort(key = lambda x:(x[0],x[1])) # 파이썬 내 기능인 lambda 사용
#arr[0]번쨰 요소부터 정렬 같으면 arr[1] 번째 요소로 정렬

for i in range(n):
    for j in range(2):
        print(arr[i][j],end=" ")
    print("")