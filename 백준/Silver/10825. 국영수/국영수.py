n = int(input())

# 그 key = lambda x: (x[1], x[2], x[3], x[0])

arr = [input().split() for _ in range(n)]


# 근데 lambda자리에 arr가 들어가야하지 ㅇ낳나여
# arr = sorted(arr, key=lambda x: (x[1], x[2], x[3], x[0]))
# 근데 국어는 감소하는 순인데
# ??

arr = sorted(arr, key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))


for i in range(n):
    print(arr[i][0])
