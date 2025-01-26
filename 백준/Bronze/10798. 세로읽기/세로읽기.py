arr = [input().strip() for _ in range(5)]

max_ = max(len(i) for i in arr)

new =""

for j in range(max_):
    for i in arr:
        if j<len(i):
            new += i[j]
            
print(new)