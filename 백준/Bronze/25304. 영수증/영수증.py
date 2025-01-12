total = int(input())
n =  int(input())

sum = 0

for i in range(0,n):
    a,b = map(int, input().split())
    sum = sum + (a*b)
    
if total == sum:
    print("Yes")
else:
    print("No")