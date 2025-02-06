n = int(input())

arr =[]

for i in range(n//5 +1):
    for j in range(n//3 +1):
        if 5*i + j*3 == n:
            arr.append(i+j)
if arr:
    print(min(arr))
else:
    print(-1)
            