#나 == 멍청이그냥바보도 아니고 씹멍청이
n = int(input())

start=2

for i in range(n):
    start = start + start - 1
    
print(start**2)
    