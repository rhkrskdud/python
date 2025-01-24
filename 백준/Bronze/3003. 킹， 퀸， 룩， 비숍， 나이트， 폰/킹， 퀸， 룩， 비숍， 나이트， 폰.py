a=[1,1,2,2,2,8]

arr = list(map(int,input().split()))

for i in range(6):
    a[i] = a[i]-arr[i]
    
print(*a)
    