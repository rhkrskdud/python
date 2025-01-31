m = int(input())
n = int(input())

arr = []

for i in range(m, n + 1):
    sibal = [j for j in range(1, i + 1) if i % j == 0]

    if len(sibal) == 2:
        arr.append(i)

        
if len(arr) == 0:
    print(-1)
else:
    print(sum(arr))
    print(arr[0])
