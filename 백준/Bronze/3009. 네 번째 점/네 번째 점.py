a, b =map(int, input().split())
x, y =map(int, input().split())
z, r =map(int, input().split())

if a == x:
    print(z, end=" ")
elif a == z:
    print(x, end=" ")
else:
    print(a, end=" ")

    
if b == y:
    print(r)
elif y == r:
    print(b)
else:
    print(y)
