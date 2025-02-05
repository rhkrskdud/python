a, b = map(int, input().split())
c = int(input())
n = int(input())

if(a<= c) and(a*n + b <= c*n):
    print(1)
else:
    print(0)