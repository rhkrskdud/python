import sys
input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))

arr1 = sorted(set(arr))

compression = {v: i for i, v in enumerate(arr1)}

result = [compression[x] for x in arr]

print(*result)