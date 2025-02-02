arr = list(map(int, input().split()))

if max(arr) < sum(arr) - max(arr):
    print(sum(arr))
else:
    max_index = arr.index(max(arr))
    arr[max_index] = sum(arr) - max(arr) - 1 
    print(sum(arr))
