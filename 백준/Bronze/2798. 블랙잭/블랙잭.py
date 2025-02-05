#3개씩 다 돌아야함
#1 2 잡고 345 , 13 잡고 45 , 14 잡고 5

n, m = map(int, input().split())
arr = list(map(int, input().split()))

max_ = 0

for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1,n):
            if max_ < arr[i] + arr[j] + arr[k] and arr[i] + arr[j] + arr[k] <= m:
                max_ = arr[i] + arr[j] + arr[k]

print(max_)
            