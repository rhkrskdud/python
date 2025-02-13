n = int(input())
arr1 = list(map(int, input().split()))

m = int(input())
arr2 = list(map(int, input().split()))
"""
시간초과남.. 딕셔너리 이용
result = []

for i in arr2:
    if i in arr1:
        result.append(arr1.count(i))
    else:
        result.append(0)

for i in result:
    print(i, end=" ")
"""
count_arr = {}

for i in arr1:
    if i in count_arr:
        count_arr[i] += 1
    else:
        count_arr[i] = 1

for i in arr2:
    if count_arr.get(i) == None:
        print(0, end=" ")
    else:
        print(count_arr.get(i), end=" ")
