import sys
input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))

arr1 = sorted(set(arr))
#딕셔너리 방식은 한번 매핑해두면 값을 찾는데 걸리는 시간이 O(n) 이기 때문이다..
compression = {v: i for i, v in enumerate(arr1)}

result = [compression[x] for x in arr]

print(*result)