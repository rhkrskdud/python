arr = list(map(int, input().strip()))

arr.sort(reverse=True)

for i in arr:
    print(i, end="")