n = int(input())

result = []

arr = list(map(int, input().split()))

for i in arr:
    sibal = [j for j in range(1,i+1) if i%j==0]
    
    if len(sibal) == 2:
        result.append(1)

print(len(result))