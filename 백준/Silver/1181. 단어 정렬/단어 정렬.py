n = int(input())

arr = [input() for _ in range(n)]
#흠 sort랑 sorted의 차이

arr = sorted(set(arr), key=lambda x:(len(x),x))

for i in arr:
    print(i)